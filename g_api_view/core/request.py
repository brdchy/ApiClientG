import requests
import os
from typing import List, Optional, Dict, Any


def send_request_to_gemini_api(
    server_url: str,
    user_id: int,
    password: str,
    model_name: str,
    text: Optional[str],
    system_instruction: Optional[str],
    flag_search: Optional[bool],
    file_paths: List[str]
) -> Optional[Dict[str, Any]]:
    """
    Отправляет POST-запрос с текстом и файлами на FastAPI сервер (/generate).

    Args:
        server_url: Полный URL эндпоинта /generate.
        user_id: ID пользователя.
        password: Пароль пользователя.
        text: Текстовое сообщение (может быть None).
        system_instruction: Системная инструкция (может быть None).
        flag_search: Флаг поиска Google (может быть None).
        file_paths: Список путей к локальным файлам для отправки.

    Returns:
        Словарь с JSON-ответом сервера или словарь с ошибкой.
    """
    request_data: Dict[str, Any] = {
        'user_id': str(user_id),
        'password': str(password),
        'model_name': str(model_name)
    }
    
    if text is not None:
        request_data['user_message_text'] = text
    if system_instruction is not None:
        request_data['system_instruction'] = system_instruction
    if flag_search is not None:
        request_data['flag_search'] = flag_search

    files_to_send = []
    opened_files = []

    try:
        for file_path in file_paths:
            if not os.path.exists(file_path):
                continue
            try:
                file_obj = open(file_path, 'rb')
                opened_files.append(file_obj)
                file_name = os.path.basename(file_path)
                files_to_send.append(('files', (file_name, file_obj)))
            except Exception as e:
                for f_obj in opened_files:
                    f_obj.close()
                return {"error": "FileError", "detail": f"Ошибка открытия файла {file_path}: {e}"}

        response = requests.post(
            server_url,
            data=request_data,
            files=files_to_send,
            timeout=30
        )

        try:
            response_json = response.json()
            return response_json
        except requests.exceptions.JSONDecodeError:
            return {
                "error": "JSONDecodeError",
                "detail": response.text,
                "status_code": response.status_code
            }

    except requests.exceptions.RequestException as e:
        return {"error": "RequestException", "detail": str(e)}
    finally:
        for f in opened_files:
            try:
                f.close()
            except Exception:
                pass


def register_user_api(base_url: str, user_id: int, password: str) -> Optional[Dict[str, Any]]:
    """
    Отправляет POST-запрос для регистрации пользователя (/register).

    Args:
        base_url: Базовый URL сервера (например, "http://127.0.0.1:8000").
        user_id: ID пользователя.
        password: Пароль пользователя.

    Returns:
        Словарь с JSON-ответом сервера или None/словарь с ошибкой.
    """
    payload = {"user_id": user_id, "password": password}
    endpoint = "/register"
    url = f"{base_url}{endpoint}"
    try:
        response = requests.post(url, json=payload, timeout=30)
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {
            "error": "JSONDecodeError",
            "detail": response.text,
            "status_code": response.status_code
        }
    except requests.exceptions.HTTPError as http_err:
        try:
            return http_err.response.json()
        except requests.exceptions.JSONDecodeError:
            return {
                "error": "HTTPError",
                "detail": http_err.response.text,
                "status_code": http_err.response.status_code
            }
    except requests.exceptions.RequestException as e:
        return {"error": "RequestException", "detail": str(e)}


def clear_user_context_api(base_url: str, user_id: int, password: str) -> Optional[Dict[str, Any]]:
    """
    Отправляет POST-запрос для очистки контекста пользователя (/clear_context) с аутентификацией.

    Args:
        base_url: Базовый URL сервера.
        user_id: ID пользователя.
        password: Пароль пользователя.

    Returns:
        Словарь с JSON-ответом сервера или None/словарь с ошибкой.
    """
    payload = {"user_id": user_id, "password": password}
    endpoint = "/clear_context"
    url = f"{base_url}{endpoint}"
    try:
        response = requests.post(url, json=payload, timeout=30)
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {
            "error": "JSONDecodeError",
            "detail": response.text,
            "status_code": response.status_code
        }
    except requests.exceptions.HTTPError as http_err:
        try:
            return http_err.response.json()
        except requests.exceptions.JSONDecodeError:
            return {
                "error": "HTTPError",
                "detail": http_err.response.text,
                "status_code": http_err.response.status_code
            }
    except requests.exceptions.RequestException as e:
        return {"error": "RequestException", "detail": str(e)}


def list_models_api(base_url: str) -> Optional[Dict[str, Any]]:
    """
    Отправляет POST-запрос для получения списка доступных моделей (/list_models).
    Не требует аутентификации.

    Args:
        base_url: Базовый URL сервера (например, "http://127.0.0.1:8000").

    Returns:
        Словарь с JSON-ответом сервера (содержит список моделей в ключе 'models')
        или словарь с информацией об ошибке.
        Успешный ответ обычно имеет статус 200 и выглядит как {'models': [...], 'status_code': 200}.
        Ошибка может вернуть словарь с ключами 'error', 'detail', 'status_code'.
    """
    endpoint = "/list_models"
    url = f"{base_url}{endpoint}"

    try:
        response = requests.post(url, json={}, timeout=30)
        
        try:
            response_json = response.json()
            if isinstance(response_json, dict):
                response_json['status_code'] = response.status_code
            return response_json
        except requests.exceptions.JSONDecodeError:
            return {
                "error": "JSONDecodeError",
                "detail": response.text,
                "status_code": response.status_code
            }

    except requests.exceptions.RequestException as e:
        return {"error": "RequestException", "detail": str(e)}