from clients.courses.courses_client import CreateCourseRequestDict, get_courses_client
from clients.exercises.exercises_client import (
    CreateExerciseRequestDict,
    get_exercises_client,
)
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import (
    get_public_users_client,
    CreateUserRequestDict,
)
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password='1234qwerty',
    lastName='Filonov',
    firstName='Nikita',
    middleName='string',
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'], password=create_user_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename='image.png', directory='courses', upload_file='./testdata/files/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(
    title='Автоматизация тестирования API с Python. Расширенный',
    maxScore=938,
    minScore=830,
    description='Погружение в профессию QA Automation Engineer с использованием '
    'актуальных технологий: HTTPX, Pydantic, Allure, Pytest',
    estimatedTime='4 weeks',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id'],
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

exercises_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestDict(
    title='Практика использования API-клиентов',
    courseId=create_course_response['course']['id'],
    maxScore=15,
    minScore=0,
    orderIndex=10,
    description='Добавить билдер для клиента ExercisesClient. '
    'Написать скрипт api_client_create_exercise.py для создания задания',
    estimatedTime='20-60 minutes',
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
