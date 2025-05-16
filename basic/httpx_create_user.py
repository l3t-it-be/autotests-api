import httpx

from tools.fakers import fake

payload = {
    'email': fake.email(),
    'password': fake.password(),
    'lastName': fake.last_name(),
    'firstName': fake.first_name(),
    'middleName': fake.middle_name(),
}
response = httpx.post('http://localhost:8000/api/v1/users', json=payload)

print(response.status_code)
print(response.json())
