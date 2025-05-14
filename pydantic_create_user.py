from pydantic import BaseModel, EmailStr, ConfigDict, Field
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Модель данных пользователя.

    Атрибуты:
    id: Уникальный идентификатор пользователя
    email: Электронная почта пользователя
    last_name: Фамилия пользователя
    first_name: Имя пользователя
    middle_name: Второе имя пользователя
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя.

    Атрибуты:
    email: Электронная почта пользователя
    password: Пароль пользователя
    last_name: Фамилия пользователя
    first_name: Имя пользователя
    middle_name: Второе имя пользователя
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя.

    Атрибуты:
    user: JSON c данными созданного пользователя:
        id: Уникальный идентификатор пользователя
        email: Электронная почта пользователя
        last_name: Фамилия пользователя
        first_name: Имя пользователя
        middle_name: Второе имя пользователя
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    user: UserSchema
