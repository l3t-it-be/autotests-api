from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """

    course_id: str


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка упражнений.
    """

    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание упражнения.
    """

    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str | None
    max_score: int | None
    min_score: int | None
    order_index: int | None
    description: str | None
    estimated_time: str | None


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление упражнения.
    """

    exercise: ExerciseSchema
