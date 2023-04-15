# python_api

<b>Запуск тестов:</b><br>
python -m pytest test_name.py

<b>Запуск определенного теста:</b><br>
python -m pytest test_name.py -k test_negative_auth_check

<b>Запуск теста из другой директории:</b><br>
python -m pytest -s tests/test_name.py