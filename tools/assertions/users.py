from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    UserSchema,
)
from tools.assertions.base import assert_equal


def assert_create_user_response(
    request: CreateUserRequestSchema, response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')


def assert_user(actual: UserSchema, expected: UserSchema) -> None:
    """
    Проверяет полное соответствие данных двух объектов пользователя.
    Используется для сравнения объектов UserSchema между собой.

    :param actual: Исходный объект пользователя.
    :param expected: Ожидаемый объект пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.email, expected.email, 'email')
    assert_equal(actual.first_name, expected.first_name, 'first_name')
    assert_equal(actual.last_name, expected.last_name, 'last_name')
    assert_equal(actual.middle_name, expected.middle_name, 'middle_name')


def assert_get_user_response(
    get_user_response: UserSchema, create_user_response: CreateUserResponseSchema
) -> None:
    """
    Проверяет соответствие данных пользователя между запросом и ответом.
    Сравнивает данные пользователя из ответа на GET-запрос (/users/me)
    с данными из ответа на создание пользователя POST-запрос (/users)

    :param get_user_response: Объект пользователя из GET-запроса.
    :param create_user_response: Объект ответа при создании пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_user(get_user_response, create_user_response.user)
