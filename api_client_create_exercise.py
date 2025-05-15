from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password='string',
    last_name='string',
    first_name='string',
    middle_name='string',
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email, password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename='image.png', directory='courses', upload_file='./testdata/files/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)
print('Create file data:', create_file_response.model_dump(by_alias=True))

create_course_request = CreateCourseRequestSchema(
    title='Автоматизация тестирования API с Python. Расширенный',
    max_score=938,
    min_score=830,
    description='Погружение в профессию QA Automation Engineer с использованием '
    'актуальных технологий: HTTPX, Pydantic, Allure, Pytest',
    estimated_time='4 weeks',
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id,
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)
print('Create course data:', create_course_response.model_dump(by_alias=True))

exercises_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestSchema(
    title='Практика использования API-клиентов',
    course_id=create_course_response.course.id,
    max_score=15,
    min_score=0,
    order_index=10,
    description='Добавить билдер для клиента ExercisesClient. '
    'Написать скрипт api_client_create_exercise.py для создания задания',
    estimated_time='20-60 minutes',
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
print('Create exercise data:', create_exercise_response.model_dump(by_alias=True))
