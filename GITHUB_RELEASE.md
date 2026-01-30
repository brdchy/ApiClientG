# Инструкция по публикации пакета на GitHub для установки через pip

## Шаг 1: Подготовка репозитория

1. Убедитесь, что все изменения закоммичены:
```bash
git add .
git commit -m "Подготовка к релизу v0.1.0"
```

2. Отправьте изменения на GitHub:
```bash
git push origin main
```

## Шаг 2: Создание тега (tag)

### Вариант 1: Через командную строку

1. Создайте аннотированный тег:
```bash
git tag -a v0.1.0 -m "Релиз версии 0.1.0"
```

2. Отправьте тег на GitHub:
```bash
git push origin v0.1.0
```

Или отправить все теги сразу:
```bash
git push origin --tags
```

### Вариант 2: Через веб-интерфейс GitHub

1. Перейдите на страницу репозитория на GitHub
2. Нажмите на "Releases" в правой части страницы (или перейдите по ссылке `https://github.com/yourusername/ApiClientG/releases`)
3. Нажмите "Create a new release"
4. В поле "Choose a tag" введите `v0.1.0` (или выберите существующий)
5. Заполните заголовок и описание релиза
6. Нажмите "Publish release"

## Шаг 3: Установка пакета

После создания тега, пакет можно установить через pip:

### Установка конкретной версии:
```bash
pip install git+https://github.com/yourusername/ApiClientG.git@v0.1.0
```

### Установка последней версии из ветки main:
```bash
pip install git+https://github.com/yourusername/ApiClientG.git
```

### Установка из приватного репозитория:
```bash
pip install git+https://github.com/yourusername/ApiClientG.git@v0.1.0
# Или с токеном доступа:
pip install git+https://YOUR_TOKEN@github.com/yourusername/ApiClientG.git@v0.1.0
```

## Шаг 4: Обновление версии для нового релиза

При создании нового релиза:

1. Обновите версию в `setup.py`:
```python
version="0.2.0",  # или другая версия
```

2. Обновите версию в `pyproject.toml`:
```toml
version = "0.2.0"
```

3. Обновите версию в `g_api_view/__init__.py`:
```python
__version__ = '0.2.0'
```

4. Создайте новый тег:
```bash
git add .
git commit -m "Версия 0.2.0"
git tag -a v0.2.0 -m "Релиз версии 0.2.0"
git push origin v0.2.0
```

## Важные замечания

- **Версионирование**: Используйте семантическое версионирование (Semantic Versioning):
  - MAJOR.MINOR.PATCH (например, 1.0.0)
  - MAJOR - несовместимые изменения API
  - MINOR - новая функциональность с обратной совместимостью
  - PATCH - исправления ошибок

- **Теги должны начинаться с 'v'**: Например, `v0.1.0`, `v1.0.0` и т.д.

- **Имя репозитория**: Замените `yourusername/ApiClientG` на реальное имя вашего репозитория

- **Для публикации в PyPI**: Если хотите публиковать в PyPI (чтобы устанавливать просто `pip install g-api-view`), нужно:
  1. Создать аккаунт на PyPI
  2. Собрать пакет: `python setup.py sdist bdist_wheel`
  3. Загрузить: `twine upload dist/*`
