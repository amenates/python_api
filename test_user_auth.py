import pytest
import requests

class TestAuthPositive:
    # Позитивный тест на авторизацию:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response_one = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert 'auth_sid' in response_one.cookies, 'There is no auth cookie in the response'
        assert 'x-csrf-token' in response_one.headers, 'There is no user id in the response'
        assert 'user_id' in response_one.json(), 'There is no user id in the response'

        auth_sid = response_one.cookies.get('auth_sid')
        token = response_one.headers.get('x-csrf-token')
        user_id_from_auth_method = response_one.json()['user_id']

        response_two = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token':token},
            cookies={'auth_sid':auth_sid}
        )

        assert 'user_id' in response_two.json(), 'There is no user id in the second response'
        user_id_from_check_method = response_two.json()['user_id']

        assert user_id_from_auth_method == user_id_from_check_method, 'Юзеры не совпадают'

    exclude_params = [
        ('no_cookie'),
        ('no+token')
    ]

    # Негативный тест на авторизацию
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response_one = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert 'auth_sid' in response_one.cookies, 'There is no auth cookie in the response'
        assert 'x-csrf-token' in response_one.headers, 'There is no user id in the response'
        assert 'user_id' in response_one.json(), 'There is no user id in the response'

        auth_sid = response_one.cookies.get('auth_sid')
        token = response_one.headers.get('x-csrf-token')

        if condition == 'no_cookie':
            response_two = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={'x-csrf-token':token},
            )
        else:
            response_two = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={'auth_sid':auth_sid}
            )

        assert 'user_id' in response_one.json(), 'Нет юзера с таким id во втором запросе'

        user_id_from_check_method = response_two.json()['user_id']

        assert user_id_from_check_method == 0, f'Юзер авторизован с параметрами {condition}'

