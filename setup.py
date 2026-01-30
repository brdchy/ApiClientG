from setuptools import setup, find_packages
import os

# Чтение README.md с обработкой ошибок кодировки
long_description = ""
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    try:
        with open(readme_path, "r", encoding="utf-8") as fh:
            long_description = fh.read()
    except UnicodeDecodeError:
        try:
            with open(readme_path, "r", encoding="utf-8-sig") as fh:
                long_description = fh.read()
        except Exception:
            long_description = "Клиент для работы с Gemini API через FastAPI сервер"

# Чтение requirements.txt с обработкой ошибок
requirements = ["requests>=2.32.3"]
requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
if os.path.exists(requirements_path):
    try:
        with open(requirements_path, "r", encoding="utf-8") as fh:
            requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    except (UnicodeDecodeError, FileNotFoundError):
        try:
            with open(requirements_path, "r", encoding="utf-8-sig") as fh:
                requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
        except Exception:
            requirements = ["requests>=2.32.3"]

setup(
    name="g-api-view",
    version="0.2.1",
    author="Viktor3911",
    author_email="your.email@example.com",
    description="Клиент для работы с Gemini API через FastAPI сервер",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Viktor3911/ApiClientG",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)
