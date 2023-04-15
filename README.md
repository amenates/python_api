# python_api

<b>Запуск тестов:</b><br>
python -m pytest test_name.py

<b>Запуск определенного теста:</b><br>
python -m pytest test_name.py -k test_negative_auth_check

<b>Запуск теста из другой директории:</b><br>
python -m pytest tests/test_name.py

<b>Запуск теста с выводом в кончаоль print()</b><br>
ключ -s дает возможность вывести print() в консоль
python -m pytest -s tests/test_name.py

<b>Запуск всех тестов в директории</b><br>
python -m pytest tests/

<br>

<b>Запуск теста с записью отчета в Allure</b><br>
python -m pytest --alluredir=test_results/ tests/test_user_auth.py

<b>Генерация отчета Allure</b><br>
allure serve test_results/

