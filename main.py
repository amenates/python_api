from json.decoder import JSONDecodeError
import requests

# payload = {"name": "User"}

# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parsed_responce_text = response.json()
# print(parsed_responce_text["answer"])


# Когда не уверены что придет JSON
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_responce_text = response.json()
    print(parsed_responce_text)
except JSONDecodeError:
    print("Responce is not a JSON format")
