import requests

CREDENTIALS = {"username": "bob", "password": "1234"}

response = requests.post("http://localhost:8000/auth/register", json=CREDENTIALS)
print(response.json())
