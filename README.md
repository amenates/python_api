# python_api

### Запуск тестов

    python -m pytest test_name.py

### Запуск определенного теста

    python -m pytest test_name.py -k test_negative_auth_check

### Запуск теста из другой директории

    python -m pytest tests/test_name.py

### Запуск теста с выводом в консоль print()
ключ -s дает возможность вывести print() в консоль

    python -m pytest -s tests/test_name.py

### Запуск всех тестов в директории

    python -m pytest tests/

---

## Allure report

### Запуск теста с записью отчета в Allure

    python -m pytest --alluredir=test_results/ tests/test_user_auth.py

### Генерация отчета Allure

    allure serve test_results/

---

## Работа с различными окружениями


### Установка окружения (через терминал git не работает)
В командной строке для windows: 

    set ENV=prod

В командной строке для macOS и Linux:

    export ENV=prod

### Просмотр установленного окружения

    echo %ENV%


