import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestAuthPositive(BaseCase):
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    def setup_method(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response_one = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        self.auth_sid = self.get_cookie(response_one, 'auth_sid')
        self.token = self.get_header(response_one, 'x-csrf-token')
        self.user_id_from_auth_method = self.get_json_value(response_one, 'user_id')

    def test_auth_user(self):
        response_two = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid': self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response_two,
            'user_id',
            self.user_id_from_auth_method,
            'ID-юзеров не совпадают'
        )

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == 'no_cookie':
            response_two = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={'x-csrf-token': self.token},
            )
        else:
            response_two = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={'auth_sid': self.auth_sid}
            )

        Assertions.assert_json_value_by_name(
            response_two,
            'user_id',
            0,
            f'Юзер авторизован с параметрами {condition}'
        )