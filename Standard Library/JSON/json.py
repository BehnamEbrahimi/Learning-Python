# json object {} json array [] json datatypes= "text", 12, null, true
import json  # json files are used for fetching data from online apis or configurations
people_string = '''
{
    "people":[
        {
            "name": "Ben Abe",
            "phone": "615-555-7154",
            "emails": ["benabe@gmail.com", "ben.abe@bogusemail.com"],
            "has_license": true
        },
        {
            "name": "John Doe",
            "phone": "444-555-5555",
            "emails": ["johnny@gmail.com", "john.doe@bogusemail.com"],
            "has_license": false
        }
    ]
}
'''
# conversion table
# JSON    Python
# object  dict
# array   list
# string  unicode
# number (int)    int, long
# number (real)   float
# true    True
# false   False
# null    None
data = json.loads(people_string)  # load string into a json object and return a dictionary
print(data['people'][0]['name'])  # how to access values in json

for person in data['people']:
    del(person['phone'])
new_string = json.dumps(data, indent=2, sort_keys=True)  # it converts a json object to a string. the optional field of indent is to prettify the output string. the optional field of sort_keys, sorts the string alphabetically
print(new_string)

#-----working with json files
with open('states.json') as f:
    data = json.load(f)  # it does not have s (which stands for string)

for state in data['states']:
    print(state['name'])
for state in data['states']:
    del(state['area_codes'])

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2) # it does not have s
