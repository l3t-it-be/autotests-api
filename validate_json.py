from jsonschema import validate, ValidationError

# fmt: off
schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  },
  "required": ["name"]
}

data = {
  "name": "John Doe",
  "age": 30
}
# fmt: on

try:
    validate(instance=data, schema=schema)
    print('Данные соответствуют схеме.')
except ValidationError as e:
    print(f'Ошибка валидации: {e.message}')
