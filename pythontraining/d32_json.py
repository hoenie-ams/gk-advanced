"""
Demo of JSON module
"""


import json

person = {
    'id': 4,
    'name': 'Peter Smith',
    'active': True,
    'email': 'peter@smith.com',
    'phone': None
}

# Output with dump or dumps (s for string)
with open("person.json", "w") as json_file:
    json.dump(person, json_file, indent=4)

# Input with load or loads (s for string)
with open("person.json", "r") as json_file:
    data = json.load(json_file)
    print(data)

print(json.dumps(person))
print(type(json.dumps(person)))
