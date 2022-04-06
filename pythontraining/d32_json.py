"""
Demo of JSON module
"""

import json

person = {
    'id': 4,
    'name': 'Patricia Kennedy',
    'active': True,
    'email': 'patricia@kennedy.org',
    'phone': None,
}

# Write with dump
with open("person.json", "w") as json_file:
    json.dump(person, json_file, indent=4)

# Read with load
with open("person.json", "r") as json_file:
    data = json.load(json_file)
    print(data)

# Write with dumps (add s for string)
json_string = json.dumps(person, indent=4)
print(json_string)

# Read with loads (add s for string)
data = json.loads(json_string)
print(data)
