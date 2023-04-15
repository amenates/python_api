from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Ответ не в JSON формате. Текст ответа "{response.text}"'

        assert name in response_as_dict, f'Ответ JSON не имеет ключ "{name}"'
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Ответ не в JSON формате. Текст ответа "{response.text}"'

        assert name in response_as_dict, f'Ответ JSON не имеет ключ "{name}"'

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Ответ не в JSON формате. Текст ответа "{response.text}"'

        for name in names:
            assert name in response_as_dict, f'Ответ JSON не имеет ключ "{name}"'

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Неожиданный status code! Ожидаемый: " \
                                                             f" {expected_status_code}. Актуальный: {response.status_code}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Ответ не в JSON формате. Текст ответа "{response.text}"'

        assert name not in response_as_dict, f'В ответе JSON не должно быть ключа "{name}". Но он присутствует'