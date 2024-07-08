import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, jsonify, request
from flask_cors import CORS
import time
from flask_migrate import Migrate
from models import db, QRCode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daraja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

consumer_key = "DKmoDUw4M4Ynk6RyFB0SkIxseZNdOXV4sSmhoFAEgi88kvYv"
consumer_secret = "b3lv2UvzmQDF7Pq9Bl85rAjGXcbV4GpBchi2Fok5REcQ8BUMAoxk1TeVnjYjbDYt"

access_token = None
token_expiry = 0

def get_access_token():
    global access_token, token_expiry
    if not access_token or time.time() > token_expiry:
        url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        data = response.json()
        access_token = data.get('access_token')
        token_expiry = time.time() + int(data.get('expires_in', 3600))
    return access_token, int(token_expiry - time.time())

@app.route('/get_token', methods=['GET'])
def get_token():
    token, expires_in = get_access_token()
    return jsonify({"access_token": token, "expires_in": expires_in})

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    token, _ = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = request.json
    print("Request Payload:", payload)
    url = "https://sandbox.safaricom.co.ke/mpesa/qrcode/v1/generate"
    response = requests.post(url, headers=headers, json=payload)
    
    print("Response Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:", response.text)
    
    if response.status_code == 200:
        qr_data = QRCode(
            MerchantName=payload.get('MerchantName'),
            RefNo=payload.get('RefNo'),
            Amount=payload.get('Amount'),
            TrxCode=payload.get('TrxCode'),
            CPI=payload.get('CPI'),
            Size=payload.get('Size')
        )
        db.session.add(qr_data)
        db.session.commit()
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to generate QR code", "details": response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
