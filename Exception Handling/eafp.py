# LBYL (Non-Pythonic)
person = {'name': 'Ben', 'age': '33', 'job': 'developer'}
if 'name' in person and 'age' in person and 'job' in person: # this check is ugly
    print(f'I am {person["name"]}. I am {person["age"]} and I am a {person["job"]}')
else:
    print('Missing some keys')

# EAFP (Pythonic): it is faster (we access the object only once) and more readable.
try:
    print(f'I am {person["name"]}. I am {person["age"]} and I am a {person["job"]}. {person["fake"]}')
except KeyError as e:
    print(f'Missing {e} key')

# Non-Pythonic
my_list = [1, 2, 3, 4, 5, 6]
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist')

# Pythonic
try:
    print(my_list[7])
except IndexError:
    print('That index does not exist')
