# TestStellarBurgers

Проект для тестирования сайта [Stellar Burgers](https://stellarburgers.education-services.ru/) для заказа бургеров.


## Структура проекта
```shell
stellar_burgers_tests/
├── conftest.py                  # драйвер, base_url
├── pytest.ini
├── requirements.txt
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── main_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── forgot_password_page.py
│   └── profile_page.py
├── locators/
│   ├── __init__.py
│   ├── main_locators.py
│   ├── login_locators.py
│   ├── register_locators.py
│   ├── forgot_password_locators.py
│   ├── profile_locators.py
│   └── header_locators.py
├── data/
│   ├── urls.py
│   ├── credentials.py           # статичные тестовые данные (email/пароль)
│   └── test_data.py             # имена, пароли, сообщения об ошибках
└── tests/
    ├── __init__.py
    ├── test_register.py
    ├── test_login.py
    ├── test_profile.py
    ├── test_navigation.py
    └── test_constructor.py
```

- pytest tests/test_register.py -v
pytest tests/test_login.py -v
pytest tests/test_profile.py -v
pytest tests/test_navigation.py -v
pytest tests/test_constructor.py -v
