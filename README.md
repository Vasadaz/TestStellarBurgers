# Тестовый проект Stellar Burgers

Автоматизированные UI-тесты сервиса **Stellar Burgers** (учебный проект Яндекс.Практикума) на связке **Python + Selenium + Pytest** по паттерну **Page Object Model (POM)**.

## Технологии

| Компонент | Технология | Версия |
|---|---|---|
| Язык | Python | 3.14 |
| Тестовый фреймворк | pytest | 9.1.1 |
| Браузерная автоматизация | Selenium | 4.47.0 |
| Браузер | Google Chrome | 151 |

## Структура проекта

```
TestStellarBurgers/
├── conftest.py                    # фикстуры pytest
├── pytest.ini                     # конфигурация pytest и маркеры
├── requirements.txt               # зависимости
├── data/                          # тестовые данные и URL
│   ├── __init__.py
│   ├── urls.py                    # константы маршрутов
│   └── test_data.py               # тестовые данные и генераторы
├── locators/                      # локаторы элементов
│   ├── __init__.py
│   ├── main_locators.py
│   ├── login_locators.py
│   ├── register_locators.py
│   ├── forgot_password_locators.py
│   ├── profile_locators.py
│   └── header_locators.py
├── pages/                         # Page Object-классы
│   ├── __init__.py
│   ├── base_page.py               # базовый класс страницы
│   ├── main_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── forgot_password_page.py
│   ├── profile_page.py
│   └── header.py
└── tests/                         # тестовые наборы
    ├── __init__.py
    ├── test_register.py
    ├── test_login.py
    ├── test_profile.py
    ├── test_navigation.py
    └── test_constructor.py
```

## Слои проекта

### 1. data/ — данные

- **urls.py** — базовый URL и маршруты: `LOGIN_PAGE`, `REGISTER_PAGE`, `FORGOT_PASSWORD_PAGE`, `PROFILE_PAGE`.
- **test_data.py** — валидные/невалидные значения (`VALID_NAME`, `VALID_PASSWORD`, `SHORT_PASSWORD`, `EXPECTED_PASSWORD_ERROR`) и функция `generate_email()` для уникальной почты.

### 2. locators/ — локаторы

Каждый файл содержит класс с XPath-локаторами соответствующей страницы или шапки:

| Класс | Назначение |
|---|---|
| `MainPageLocators` | кнопка входа, заголовок конструктора, табы разделов |
| `LoginPageLocators` | поля email/пароля, кнопка «Войти», ссылка восстановления |
| `RegisterPageLocators` | поля формы, кнопка регистрации, ошибка пароля |
| `ForgotPasswordPageLocators` | ссылка «Войти» |
| `ProfilePageLocators` | поля профиля, кнопка «Выход» |
| `HeaderLocators` | логотип, «Конструктор», «Личный кабинет» |

### 3. pages/ — Page Objects

**BasePage** — базовый класс всех страниц. Содержит:

- `find(locator)` — поиск элемента
- `click(locator)` — клик с ожиданием кликабельности
- `input_text(locator, text)` — очистка и ввод
- `get_text(locator)` / `get_attribute(locator, attr)` — чтение
- `is_displayed(locator, timeout)` — проверка видимости
- `current_url()` — текущий URL

**MainPage** — главная страница и конструктор:

| Метод | Назначение |
|---|---|
| `click_login_button()` | открыть форму входа |
| `is_constructor_loaded()` | проверка загрузки конструктора |
| `click_tab(tab_locator)` | перейти в раздел ингредиентов |
| `is_tab_active(tab_locator)` | активен ли раздел |

**LoginPage** — форма входа:

| Метод | Назначение |
|---|---|
| `input_email()` / `input_password()` | ввод креденшелов |
| `click_login()` / `login()` | отправка формы |
| `is_login_button_displayed()` | проверка формы |
| `click_recover_link()` | переход к восстановлению |
| `wait_for_current_url(url)` | ожидание URL |
| `open_login_via_*()` | статические точки входа в логин |

**RegisterPage** — форма регистрации:

| Метод | Назначение |
|---|---|
| `fill_name()` / `fill_email()` / `fill_password()` | ввод данных |
| `click_register()` / `register()` | отправка формы |
| `get_error_text()` / `is_error_displayed()` | работа с ошибкой пароля |
| `wait_for_login_page()` | ожидание перехода на вход |
| `click_login_link()` | переход ко входу |

**ProfilePage** — личный кабинет:

| Метод | Назначение |
|---|---|
| `click_logout()` | выход из аккаунта |
| `get_profile_email()` / `get_profile_name()` | чтение данных профиля |
| `is_logout_displayed()` | признак авторизации |
| `wait_until_loaded()` | ожидание загрузки профиля |

**Header** — шапка сайта:

| Метод | Назначение |
|---|---|
| `click_profile_button()` | переход в ЛК |
| `click_constructor_button()` | переход в конструктор |
| `click_logo()` | клик по логотипу |

**ForgotPasswordPage** — восстановление пароля:

| Метод | Назначение |
|---|---|
| `click_login_link()` | ссылка «Войти» |

### 4. conftest.py — фикстуры

| Фикстура | Назначение |
|---|---|
| `driver` | браузер Chrome с `implicitly_wait(5)`, закрытие через `quit()` |
| `registered_user` | регистрация пользователя через UI, возвращает `email`/`password`/`name` |

## Тестовые наборы

### test_register.py

| Тест | Проверка |
|---|---|
| `test_successful_registration` | успешная регистрация → переход на вход |
| `test_registration_with_short_password_shows_error` | ошибка при пароле короче 6 символов |

### test_login.py

| Тест | Проверка |
|---|---|
| `test_login_from_different_entry_points` (параметризован) | вход через 4 точки: главная, «Личный кабинет», регистрация, восстановление пароля |

### test_profile.py

| Тест | Проверка |
|---|---|
| `test_transition_to_profile` | переход в ЛК, наличие кнопки «Выйти» и корректный URL |
| `test_logout_from_profile` | выход по кнопке «Выход» → форма входа |

### test_navigation.py

| Тест | Проверка |
|---|---|
| `test_navigate_to_constructor_via_button` | переход в конструктор по кнопке «Конструктор» |
| `test_navigate_to_constructor_via_logo` | переход в конструктор по логотипу |

### test_constructor.py

| Тест | Проверка |
|---|---|
| `test_section_navigation_to_buns` | переход в раздел «Булки» |
| `test_section_navigation_to_sauces` | переход в раздел «Соусы» |
| `test_section_navigation_to_fillings` | переход в раздел «Начинки» |

## Маркеры

В `pytest.ini` объявлены маркеры:

```ini
smoke: Критические сценарии (регистрация и вход)
regression: Полный регрессионный набор
```

## Установка и запуск

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Chromedriver

Версия `chromedriver` должна совпадать с установленной версией Google Chrome. Драйвер должен находиться в `PATH` системы.

Скачать нужную версию: [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).

### 3. Запуск тестов

```bash
# весь набор
pytest

# конкретный файл
pytest tests/test_login.py

# по маркеру
pytest -m smoke

# подробный вывод
pytest -v --tb=long
```