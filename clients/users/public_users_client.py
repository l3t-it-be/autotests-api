from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    API клиент для публичных методов работы с пользователями.
    Предоставляет доступ к эндпоинтам, не требующим авторизации.
    Наследуется от базового APIClient.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создает нового пользователя через API.

        :param request: Словарь с данными для создания пользователя.
                Должен содержать поля email, password, first_name, last_name и middle_name.
        :return httpx.Response: Ответ от сервера с результатом создания пользователя.
                В случае успеха вернется статус 200 Created.
                При ошибке валидации - 422 Validation Error.
                Если пользователь уже существует - 403 Access Forbidden.
        """

        return self.post('/api/v1/users', json=request)
