# json into a python dictionary (vice - versa)
import json

# sample json
userJson = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse to dict
user = json.loads(userJson)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJson = json.dumps(car)

print(carJson)
