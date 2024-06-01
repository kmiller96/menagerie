import random

import requests


CREDENTIALS = {"username": "bob", "password": "1234"}

# -- Randomly authenticate -- #
authenticate = bool(random.randint(0, 1))

if authenticate:
    print("Authenticating user...")

    response = requests.post("http://localhost:8000/auth/login", json=CREDENTIALS)
    print(response.json())

    response = requests.get("http://localhost:8000/", cookies=response.cookies)
    print(response.json())

else:
    print("Skipping authentication...")

    response = requests.get("http://localhost:8000/")
    print(response.json())
