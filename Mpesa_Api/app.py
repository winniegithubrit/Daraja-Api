import requests
from requests.auth import HTTPBasicAuth

consumer_key = "DKmoDUw4M4Ynk6RyFB0SkIxseZNdOXV4sSmhoFAEgi88kvYv"
consumer_secret = "b3lv2UvzmQDF7Pq9Bl85rAjGXcbV4GpBchi2Fok5REcQ8BUMAoxk1TeVnjYjbDYt"

def get_access_token():
  url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
  access_token = response.json().get('access_token')
  return access_token

print(get_access_token())
