from typing import Optional, List, Dict, Any
from urllib.parse import urlparse
from .core.request import (
    send_request_to_gemini_api,
    register_user_api,
    clear_user_context_api,
    list_models_api
)


class Client:
    """Клиент для работы с Gemini API через FastAPI сервер.
    
    Пример использования:
        >>> client = Client(
        ...     server_url="http://10.61.17.80:8000",
        ...     user_id=123,
        ...     password="your_password"
        ... )
        >>> response = client.generate("Привет!")
        >>> print(response.get("answer"))
    """
    
    def __init__(
        self,
        server_url: str,
        user_id: int,
        password: str,
        auto_register: bool = True
    ):
        """Инициализация клиента.
        
        Args:
            server_url: Базовый URL сервера (например, "http://10.61.17.80:8000")
            user_id: ID пользователя
            password: Пароль пользователя
            auto_register: Автоматически регистрировать пользователя при создании клиента
            
        Raises:
            ValueError: Если server_url имеет неверный формат
        """
        self._validate_url(server_url)
        self.server_url = server_url.rstrip('/')
        self.user_id = user_id
        self.password = password
        self.generate_endpoint = f"{self.server_url}/generate"
        
        if auto_register:
            self.register()
    
    @staticmethod
    def _validate_url(url: str) -> None:
        """Валидация URL сервера.
        
        Args:
            url: URL для проверки
            
        Raises:
            ValueError: Если URL имеет неверный формат
        """
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                raise ValueError(f"Неверный формат URL: {url}")
            if result.scheme not in ('http', 'https'):
                raise ValueError(f"URL должен использовать http или https: {url}")
        except Exception as e:
            if isinstance(e, ValueError):
                raise
            raise ValueError(f"Неверный формат URL: {url}") from e
    
    def register(self) -> Optional[Dict[str, Any]]:
        """Регистрирует пользователя на сервере.
        
        Returns:
            Словарь с результатом регистрации или None в случае ошибки
            
        Example:
            >>> result = client.register()
            >>> if result:
            ...     print("Регистрация успешна")
        """
        return register_user_api(
            base_url=self.server_url,
            user_id=self.user_id,
            password=self.password
        )
    
    def generate(
        self,
        message_text: str,
        file_paths: Optional[List[str]] = None,
        flag_search: bool = False,
        system_instruction: str = "",
        model_name: str = "Gemini 2 Flash"
    ) -> Optional[Dict[str, Any]]:
        """Генерирует ответ с помощью Gemini API.
        
        Args:
            message_text: Текст сообщения для обработки
            file_paths: Список путей к файлам (по умолчанию [])
            flag_search: Флаг поиска (по умолчанию False)
            system_instruction: Системная инструкция (по умолчанию "")
            model_name: Название модели (по умолчанию "Gemini 2 Flash")
        
        Returns:
            Ответ от API в виде словаря или None в случае ошибки
        """
        if file_paths is None:
            file_paths = []
        
        return send_request_to_gemini_api(
            server_url=self.generate_endpoint,
            user_id=self.user_id,
            password=self.password,
            model_name=model_name,
            text=message_text,
            system_instruction=system_instruction,
            flag_search=flag_search,
            file_paths=file_paths
        )
    
    def clear_context(self) -> Optional[Dict[str, Any]]:
        """Очищает контекст диалога пользователя.
        
        Returns:
            Словарь с результатом очистки или None в случае ошибки
        """
        return clear_user_context_api(
            base_url=self.server_url,
            user_id=self.user_id,
            password=self.password
        )
    
    def list_models(self) -> Optional[Dict[str, Any]]:
        """Получает список доступных моделей.
        
        Returns:
            Словарь со списком моделей или None в случае ошибки
        """
        return list_models_api(base_url=self.server_url)
    
    def get_answer(self, message_text: str, **kwargs) -> Optional[str]:
        """Удобный метод для получения только текста ответа.
        
        Args:
            message_text: Текст сообщения
            **kwargs: Дополнительные параметры для generate()
        
        Returns:
            Текст ответа или None в случае ошибки
            
        Example:
            >>> answer = client.get_answer("Привет!")
            >>> print(answer)
        """
        if not message_text or not message_text.strip():
            return None
            
        result = self.generate(message_text, **kwargs)
        if result and isinstance(result, dict):
            return result.get("answer")
        return None
