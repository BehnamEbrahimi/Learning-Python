# LBYL (Non-Pythonic)
person = {'name': 'Ben', 'age': '33', 'job': 'developer'}
if 'name' in person and 'age' in person and 'job' in person:
    print(f'I am {person["name"]}. I am {person["age"]} and I am a {person["job"]}')
else:
    print('Missing some keys')

# EAFP (Pythonic)
try:
    print(f'I am {person["name"]}. I am {person["age"]} and I am a {person["job"]}. {person["fake"]}')
except KeyError as e:
    print(f'Missing {e} key')
