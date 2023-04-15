from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ
        register_data = self.prepare_registration_data()

        response_one = MyRequests.post('/user/', data=register_data)

        Assertions.assert_code_status(response_one, 200)
        Assertions.assert_json_has_key(response_one, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response_one, 'id')

        # АВТОРИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ
        login_data = {
            "email": email,
            "password": password
        }

        response_two = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response_two, 'auth_sid')
        token = self.get_header(response_two, 'x-csrf-token')

        # РЕДАКТИРОВАНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ
        new_name = "Changed Name"

        response_three = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response_three, 200)

        # ПОЛУЧЕНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЯ
        response_four = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response_four,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )