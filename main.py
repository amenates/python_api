# from json.decoder import JSONDecodeError
import requests

# payload = {"name": "User"}

# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parsed_responce_text = response.json()
# print(parsed_responce_text["answer"])

#
# # Когда не уверены что придет JSON
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_responce_text = response.json()
#     print(parsed_responce_text)
# except JSONDecodeError:
#     print("Responce is not a JSON format")


# headers = {"some_header": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
#
# print(response.text)
# print(response.headers)


# Cookie

payload = {"login": "secret_login", "password": "secret_pass"}
response_one = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response_one.cookies.get("auth_cookie")
cookies = {}
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})

response_two = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response_two.text)