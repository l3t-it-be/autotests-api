from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    Описание структуры пользователя.
    """

    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """

    user: User


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

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
