# Daraja-Api
# payloads mpesa express payload 
{
  "BusinessShortCode": "174379",  // Merchant's Paybill or Buygoods number
  "Password": "ENCODED_PASSWORD",  // Base64 encoded password (Shortcode+Passkey+Timestamp)
  "Timestamp": "20240709174254",  // Current timestamp
  "TransactionType": "CustomerPayBillOnline",  // Type of transaction
  "Amount": "1",  // Amount to be transacted
  "PartyA": "254708374149",  // Customer's phone number (payer)
  "PartyB": "174379",  // Merchant's Paybill or Buygoods number (receiver)
  "PhoneNumber": "254708374149",  // Customer's phone number (receives STK Push prompt)
  "CallBackURL": "https://yourdomain.com/callback",  // Callback URL for the response
  "AccountReference": "Test",  // Reference for the transaction
  "TransactionDesc": "Test"  // Description of the transaction
}

# RESPONSES
{
    "CheckoutRequestID": "ws_CO_09072024181053856797594751",
    "CustomerMessage": "Success. Request accepted for processing",
    "MerchantRequestID": "c0d2-4b9a-a71a-12bae346ef6e3246223",
    "ResponseCode": "0",
    "ResponseDescription": "Success. Request accepted for processing"
}
# qr code payload 
{    
   "MerchantName":"TEST SUPERMARKET",
   "RefNo":"Invoice Test",
   "Amount":1,
   "TrxCode":"BG",
   "CPI":"373132",
   "Size":"300"
}