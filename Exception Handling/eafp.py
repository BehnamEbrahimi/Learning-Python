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

# Race Condition
import os
my_file = "/tmp/test.txt"

# Race Condition. after chechking, the connection may be disrupted and file might be not accessiblle
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File can not be accessed')

# No Race Condition. 
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())
