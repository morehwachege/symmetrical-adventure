import requests

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer krmXX8F7hE8ioGxaIQrcF5Y1248J'
}

payload = {
    "ShortCode": 174379,
    "ResponseType": "Completed",
    "ConfirmationURL": "https://mydomain.com/confirmation",
    "ValidationURL": "https://mydomain.com/validation",
  }

response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, data = payload)
print(response.text.encode('utf8'))