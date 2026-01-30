# Инструкция для пуша на GitHub

## Быстрый старт

```bash
# 1. Проверка статуса
git status

# 2. Добавление всех изменений
git add .

# 3. Коммит
git commit -m "Рефакторинг: подготовка к релизу v0.1.0"

# 4. Пуш на GitHub
git push origin main

# 5. Создание тега
git tag -a v0.1.0 -m "Релиз версии 0.1.0"

# 6. Пуш тега
git push origin v0.1.0
```

## Установка после пуша

```bash
pip install git+https://github.com/yourusername/ApiClientG.git@v0.1.0
```

**Важно:** Замените `yourusername/ApiClientG` на реальное имя вашего репозитория!
