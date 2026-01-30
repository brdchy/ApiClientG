"""
Пример использования g-api-view клиента
"""
from g_api_view import Client

# Создание клиента с автоматической регистрацией
client = Client(
    server_url="http://10.61.17.80:8000",
    user_id=123,
    password="your_password"
)

# Пример 1: Простая генерация текста
print("=== Пример 1: Простая генерация ===")
response = client.generate("Привет, как дела?")
if response and response.get("answer"):
    print(f"Ответ: {response.get('answer')}")
print()

# Пример 2: Получение только текста ответа
print("=== Пример 2: Получение только текста ===")
answer = client.get_answer("Напиши короткую историю про Машу")
if answer:
    print(f"Ответ: {answer}")
print()

# Пример 3: Генерация с дополнительными параметрами
print("=== Пример 3: Генерация с параметрами ===")
response = client.generate(
    message_text="Расскажи о Python",
    model_name="Gemini 2 Flash",
    flag_search=True,
    system_instruction="Ты опытный программист"
)
if response and response.get("answer"):
    print(f"Ответ: {response.get('answer')}")
print()

# Пример 4: Получение списка моделей
print("=== Пример 4: Список моделей ===")
models = client.list_models()
if models and models.get("models"):
    print("Доступные модели:")
    for model in models.get("models", []):
        print(f"  - {model.get('model_name')}")
print()

# Пример 5: Очистка контекста
print("=== Пример 5: Очистка контекста ===")
result = client.clear_context()
if result:
    print("Контекст очищен")
print()

# Пример 6: Клиент без автоматической регистрации
print("=== Пример 6: Ручная регистрация ===")
client2 = Client(
    server_url="http://10.61.17.80:8000",
    user_id=456,
    password="another_password",
    auto_register=False
)
registration = client2.register()
if registration:
    print(f"Регистрация: {registration}")
