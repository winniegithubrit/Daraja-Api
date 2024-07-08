import requests
from requests.auth import HTTPBasicAuth
from flask import Flask,jsonify
import time

app = Flask(__name__)

consumer_key = "DKmoDUw4M4Ynk6RyFB0SkIxseZNdOXV4sSmhoFAEgi88kvYv"
consumer_secret = "b3lv2UvzmQDF7Pq9Bl85rAjGXcbV4GpBchi2Fok5REcQ8BUMAoxk1TeVnjYjbDYt"

access_token= None
token_expiry = 0

def get_access_token():
    global access_token, token_expiry
    if not access_token or time.time() > token_expiry:
        url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        data = response.json()
        access_token = data.get('access_token')
        token_expiry = time.time() + int(data.get('expires_in', 3600))
    return access_token
print(get_access_token())
