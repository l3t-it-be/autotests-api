from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    Предоставляет доступ к эндпоинтам, не требующим авторизации.
    Наследуется от базового APIClient.
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создает нового пользователя через API.

        :param request: Словарь с данными для создания пользователя.
                Должен содержать поля email, password, first_name, last_name и middle_name.
        :return httpx.Response: Ответ от сервера в виде объекта httpx.Response.
                В случае успеха вернется статус 200 Created.
                При ошибке валидации - 422 Validation Error.
                Если пользователь уже существует - 403 Access Forbidden.
        """

        return self.post('/api/v1/users', json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request).text
        return CreateUserResponseSchema.model_validate_json(response)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
