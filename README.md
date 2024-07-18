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
# C2B RESPONSE
{
    "OriginatorCoversationID": "1c5b-4ba8-815c-ac45c57a3db01618715",
    "ResponseCode": "0",
    "ResponseDescription": "Success"
}
# C2B PAYLOAD
{
    "ShortCode": 600990,
    "ResponseType": "Completed",
    "ConfirmationURL": "https://mydomain.com/confirmation",
    "ValidationURL": "https://mydomain.com/validation"
  }
# B2C BODY
{
    
    "InitiatorName": "testapi",
    "SecurityCredential": "aiRoYxO9YtXMozPgfQ6D68Ot+U6f5CcePmxy2J1v8ZQfYpOdudK5+58lGZ+ez0glLTQ1HEWrpuYj2kkEGHFlpv4MNY+uZoTRr6KTm0/3Y8yCN1hF7fkj3p/6dbAlP2b7uYM++8azfC8IFQZHfp/wOKaJ2DhcNak7CbOWZb2LrE7KXpSx02KMDMnIq2vhn/3ylcgn9owMUJAOiCfFHm4u6F7PzHjAdYbskA6D4KjLbqZd8UhSj1BbdCqi1rJeZJ3NatFqbTPohxpVxzIaWX16LnMATE5aMWLnSTwO5GqOKm5l5IZXnGB5flMDSsLoiYTMerZJEDvXoUAptJpLWeV4TQ==",
    "CommandID": "SalaryPayment",
    "Amount": 10,
    "PartyA": 600999,
    "PartyB": 254797594751,
    "Remarks": "Test remarks",
    "QueueTimeOutURL": "https://mydomain.com/b2c/queue",
    "ResultURL": "https://mydomain.com/b2c/result",
    "Occasion": "Done"
  }
  # B2C RESPONSE
  {
    "ConversationID": "AG_20240718_20101288e3f15d4b3e79",
    "OriginatorConversationID": "1c5b-4ba8-815c-ac45c57a3db01619036",
    "ResponseCode": "0",
    "ResponseDescription": "Accept the service request successfully."
}
# TRANSACTION STATUS BODY AND RESPONSE
{
    "Initiator": "testapi",
    "SecurityCredential": "ckUeqimPlWQ7Z7gzyBTMWaKktb1pJjalJSn0RuiL/3aY0OWZTlltTRbCb3ZoaB8WfaNIT8yAk5re7d7SJ+vz+BS4wDUqyYSSAclA0nx07Chjkul9dRrkOjoEP4uMkVSv48Wa0Wu03B3LJjeMY7d4NTRC7QF3VTEf5Z/lSA+tPZL+OglJXtcEiv2ZqnRcJKIG7gy4EmZt4Zqq73urtRSzGVECOXdS9pvqAbLAMVBY19hPsJMCbwfewHeQkCMSriJMAB0lV9UXFANM7iBQYYgzVaI5LdMCxplFsDRj7mBkm9S2SeM3p0g8PjWj4S1oNEd9aN5s7wfKlozHA25Crs4u3g==",
    "CommandID": "TransactionStatusQuery",
    "TransactionID": "OEI2AK4Q16",
    "PartyA": 600995,
    "IdentifierType": "1",
    "ResultURL": "https://mydomain.com/TransactionStatus/result/",
    "QueueTimeOutURL": "https://mydomain.com/TransactionStatus/queue/",
    "Remarks": "ok",
    "Occassion": "ok"
  }
  # RESPONSE 
  {
    "ConversationID": "AG_20240718_20105c44dec6cb3b05ab",
    "OriginatorConversationID": "6e86-45dd-91ac-fd5d4178ab523768826",
    "ResponseCode": "0",
    "ResponseDescription": "Accept the service request successfully."
}