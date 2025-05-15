from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания пользователя.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """

    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr | None
    last_name: str | None
    first_name: str | None
    middle_name: str | None


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """

    user: UserSchema
