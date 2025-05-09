import httpx

# fmt: off
payload = {'email': 'test_user@gmail.com',
           'password': '1234_test_user'}
# fmt: on

login_response = httpx.post(
    'http://localhost:8000/api/v1/authentication/login', json=payload
)
token_data = login_response.json()
print(token_data)

access_token = token_data['token']['accessToken']

user_url = 'http://localhost:8000/api/v1/users/me'
headers = {'Authorization': f'Bearer {access_token}'}

user_response = httpx.get(user_url, headers=headers)
user_response.raise_for_status()

assert user_response.status_code == 200, 'Failed to get user data'
user_data = user_response.json()
print(user_data, user_response.status_code, sep='\n')
