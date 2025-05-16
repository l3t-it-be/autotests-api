from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    token_type: str
    access_token: str
    refresh_token: str


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """

    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """

    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)
