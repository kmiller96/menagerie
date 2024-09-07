import requests


print("Use the pydantic endpoint:")

response = requests.post(
    "http://localhost:8000/with/add",
    json={"a": 1, "b": 2},
)

print(response.content)

print("Use the non-pydantic endpoint:")
response = requests.post(
    "http://localhost:8000/without/add",
    json={"a": 1, "b": 2},
)

print(response.content)
