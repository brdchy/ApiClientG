# g-api-view

Клиент для работы с Gemini API через FastAPI сервер.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Установка

### Установка из GitHub (после создания тега)

```bash
pip install git+https://github.com/Viktor3911/ApiClientG.git@v0.1.0
```

Или для установки последней версии из ветки main:

```bash
pip install git+https://github.com/Viktor3911/ApiClientG.git
```

### Установка из локальной директории (для разработки)

```bash
pip install -e .
```

## Использование

### Простой способ - через класс Client

```python
from g_api_view import Client

# Создание клиента (автоматически регистрирует пользователя)
client = Client(
    server_url="http://10.61.17.80:8000",
    user_id=123,
    password="your_password"
)

# Генерация текста
response = client.generate("Привет, как дела?")
print(response.get("answer"))

# Или получить только текст ответа
answer = client.get_answer("Напиши историю про Машу")
print(answer)

# Очистка контекста
client.clear_context()

# Получение списка доступных моделей
models = client.list_models()
print(models)
```

### Без автоматической регистрации

```python
from g_api_view import Client

client = Client(
    server_url="http://10.61.17.80:8000",
    user_id=123,
    password="your_password",
    auto_register=False  # Отключить автоматическую регистрацию
)

# Регистрация вручную
registration_result = client.register()
print(registration_result)
```

### Использование с файлами

```python
from g_api_view import Client

client = Client(
    server_url="http://10.61.17.80:8000",
    user_id=123,
    password="your_password"
)

# Генерация с файлами
response = client.generate(
    message_text="Проанализируй эти файлы",
    file_paths=["/path/to/file1.pdf", "/path/to/file2.jpg"],
    model_name="Gemini 2 Flash",
    flag_search=True,
    system_instruction="Ты помощник для анализа документов"
)
```

### Старый способ (для обратной совместимости)

```python
import g_api_view

# Настройка через settings.py (не рекомендуется)
print(g_api_view.reg())
print(g_api_view.generate(message_text='ку'))
g_api_view.clear_context()
```

## Параметры Client

- `server_url` (str): Базовый URL сервера (обязательно)
- `user_id` (int): ID пользователя (обязательно)
- `password` (str): Пароль пользователя (обязательно)
- `auto_register` (bool): Автоматически регистрировать пользователя при создании (по умолчанию True)

## Методы Client

- `register()` - Регистрация пользователя на сервере
- `generate(message_text, file_paths=None, flag_search=False, system_instruction="", model_name="Gemini 2 Flash")` - Генерация ответа
- `get_answer(message_text, **kwargs)` - Получить только текст ответа
- `clear_context()` - Очистка контекста диалога
- `list_models()` - Получение списка доступных моделей

## Требования

- Python >= 3.7
- requests >= 2.32.3

## Лицензия

MIT
