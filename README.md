# Обзор проекта TestStellarBurgers

## 1. Назначение и стек

UI-автотесты сервиса **Stellar Burgers** (учебный сервис Яндекс.Практикума) на связке **Python + Selenium + Pytest** по паттерну **Page Object Model (POM)**.

| Компонент | Технология | Версия |
|---|---|---|
| Язык | Python | 3.14 |
| Тестовый фреймворк | pytest | 9.1.1 |
| Браузерная автоматизация | Selenium | 4.47.0 |
| Управление драйвером | webdriver-manager | 4.1.2 |
| Браузер | Google Chrome | 152 |

---

## 2. Дерево файлов

```
TestStellarBurgers/
├── conftest.py              # фикстуры (driver, base_url, registered_user)
├── pytest.ini               # конфигурация pytest + маркеры
├── requirements.txt         # зависимости
├── data/
│   ├── __init__.py          # экспорт констант
│   ├── urls.py              # URL сервиса
│   └── test_data.py         # тестовые данные
├── locators/
│   ├── __init__.py          # экспорт локаторов
│   ├── main_locators.py
│   ├── login_locators.py
│   ├── register_locators.py
│   ├── forgot_password_locators.py
│   ├── profile_locators.py
│   └── header_locators.py
├── pages/
│   ├── __init__.py          # экспорт page-классов
│   ├── base_page.py         # базовый класс
│   ├── main_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── forgot_password_page.py
│   ├── profile_page.py
│   └── header.py
└── tests/
    ├── __init__.py
    ├── test_register.py
    ├── test_login.py
    ├── test_profile.py
    ├── test_navigation.py
    └── test_constructor.py
```

---

## 3. Описание модулей

### 3.1 `conftest.py`

| Элемент | Тип | Назначение |
|---|---|---|
| `driver` | fixture (function) | Создаёт Chrome c чистым профилем, `--window-size`, `--disable-extensions`, `implicitly_wait(5)`. Закрывает через `quit()` |
| `base_url` | fixture | Возвращает `BASE_URL` |
| `registered_user` | fixture | Регистрирует пользователя через UI, возвращает `{email, password, name}` |

**Методы фикстур (косвенно задействованы):**
- `RegisterPage.register()` — регистрация внутри `registered_user`
- `time.time()` — генерация уникального email

### 3.2 `pages/base_page.py` — `BasePage`

Базовый класс всех страниц.

| Метод | Сигнатура | Назначение                                      |
|---|---|-------------------------------------------------|
| `__init__` | `(driver, timeout=10)` | Инициализирует `driver` и `WebDriverWait`       |
| `find` | `(locator)` | Поиск элемента                                  |
| `click` | `(locator)` | Клик по элементу                                |
| `input_text` | `(locator, text)` | Очистка и ввод текста                           |
| `get_text` | `(locator)` | Возвращает текст элемента                       |
| `is_displayed` | `(locator)` | Проверка видимости, глушит исключения → `False` |
| `current_url` | — | Текущий URL                                     |
| `get_attribute` | `(locator, attribute)` | Значение атрибута элемента                      |

### 3.3 `pages/main_page.py` — `MainPage`

| Метод | Назначение |
|---|---|
| `click_login_button` | Клик «Войти в аккаунт» |
| `is_constructor_loaded` | Проверка заголовка «Соберите бургер» |
| `click_tab` | Клик по табу ингредиента |
| `is_tab_active` | Проверка класса `current` у таба |

### 3.4 `pages/login_page.py` — `LoginPage`

| Метод | Назначение |
|---|---|
| `input_email` | Ввод email |
| `input_password` | Ввод пароля |
| `click_login` | Клик «Войти» |
| `login` | Комплекс: email + пароль + submit |
| `is_login_button_displayed` | Проверка кнопки «Войти» |
| `wait_for_current_url` | Ожидание конкретного URL |
| `click_recover_link` | Клик «Восстановить пароль» |

### 3.5 `pages/register_page.py` — `RegisterPage`

| Метод | Назначение |
|---|---|
| `fill_name` | Ввод имени |
| `fill_email` | Ввод email |
| `fill_password` | Ввод пароля |
| `click_register` | Клик «Зарегистрироваться» |
| `register` | Комплексная регистрация |
| `get_error_text` | Текст ошибки пароля |
| `is_error_displayed` | Показ ошибки пароля |
| `wait_for_login_page` | Ожидание перехода на логин |
| `click_login_link` | Клик «Войти» на форме регистрации |

### 3.6 `pages/profile_page.py` — `ProfilePage`

| Метод | Назначение |
|---|---|
| `click_logout` | Клик «Выход» |
| `get_profile_email` | Email из поля «Логин» |
| `get_profile_name` | Имя из поля «Имя» |
| `is_logout_displayed` | Проверка кнопки «Выход» |
| `wait_until_loaded` | Ожидание загрузки профиля |

### 3.7 `pages/header.py` — `Header`

| Метод | Назначение |
|---|---|
| `click_profile_button` | Клик «Личный кабинет» |
| `click_constructor_button` | Клик «Конструктор» |
| `click_logo` | Клик по логотипу |

### 3.8 `pages/forgot_password_page.py` — `ForgotPasswordPage`

| Метод | Назначение |
|---|---|
| `click_login_link` | Клик «Войти» |

### 3.9 Локаторы (`locators/*.py`)

| Класс | Локаторы |
|---|---|
| `MainPageLocators` | `LOGIN_BUTTON`, `CONSTRUCTOR_HEADER`, `BUNS_SECTION`, `SAUCES_SECTION`, `FILLINGS_SECTION` |
| `LoginPageLocators` | `EMAIL_INPUT`, `PASSWORD_INPUT`, `LOGIN_BUTTON`, `RECOVER_LINK` |
| `RegisterPageLocators` | `NAME_INPUT`, `EMAIL_INPUT`, `PASSWORD_INPUT`, `REGISTER_BUTTON`, `PASSWORD_ERROR`, `LOGIN_LINK` |
| `ForgotPasswordPageLocators` | `LOGIN_LINK` |
| `ProfilePageLocators` | `NAME_INPUT`, `EMAIL_INPUT`, `LOGOUT_BUTTON` |
| `HeaderLocators` | `LOGO`, `CONSTRUCTOR_BUTTON`, `PROFILE_BUTTON` |

---

## 4. Таблица связей

| Модуль | Импортирует |
|---|---|
| `conftest.py` | `data.urls`, `pages.register_page` |
| `pages/base_page.py` | `selenium.webdriver.*` |
| Все page-классы | `base_page.BasePage` + свой `locators` |
| `tests/test_login.py` | `MainPage`, `LoginPage`, `RegisterPage`, `ForgotPasswordPage`, `Header`, `ProfilePage` |
| `tests/test_profile.py` | `Header`, `LoginPage`, `ProfilePage`, `data.urls` |
| `tests/test_navigation.py` | `Header`, `LoginPage`, `MainPage`, `ProfilePage` |
| `tests/test_constructor.py` | `MainPage`, `MainPageLocators` |

