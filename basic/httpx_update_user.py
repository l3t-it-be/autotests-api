import httpx

from tools.fakers import fake

create_user_payload = {
    'email': fake.email(),
    'password': fake.password(),
    'lastName': fake.last_name(),
    'firstName': fake.first_name(),
    'middleName': fake.middle_name(),
}
create_user_response = httpx.post(
    'http://localhost:8000/api/v1/users', json=create_user_payload
)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

login_payload = {
    'email': create_user_payload['email'],
    'password': create_user_payload['password'],
}
login_response = httpx.post(
    'http://localhost:8000/api/v1/authentication/login', json=login_payload
)
login_response_data = login_response.json()
print('Login data:', login_response_data)

update_user_headers = {
    'Authorization': f'Bearer {login_response_data["token"]["accessToken"]}'
}

update_user_payload = {
    'email': fake.email(),
    'password': create_user_payload['password'],
    'lastName': create_user_payload['lastName'],
    'firstName': create_user_payload['firstName'],
    'middleName': create_user_payload['middleName'],
}

update_user_response = httpx.patch(
    f'http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}',
    headers=update_user_headers,
    json=update_user_payload,
)
print(
    f'Update user status code: {update_user_response.status_code}\n'
    f'Updated user data: {update_user_response.json()}'
)
