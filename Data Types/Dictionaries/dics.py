# key and value
student = {'name': 'Ben', 'age': 30, 'courses': ['Math', 'Art'], 100: 500}
print(student)
print(student['age'])
print(student[100])  # the key can be any immutable data type
print(student.get('age'))  # the get method is like the above line except if the key does not exist, it returns None instead of error
print(student.get('pay'))
print(student.get('pay', 'Not found'))  # setting a default value

# adding a value
student['phone'] = '555 - 555 - 5555'

# updating a value
student['name'] = 'john'

# updating multiple values
student.update({'name': 'Michael', 'age': 25, 'Pay': 50000})
print(student)

# deleting a value
del student[100]
print(student)
pay = student.pop('Pay')
print(student)

# length of a dict
print(len(student))

# getting all the keys and the values
print(student.keys())
print(student.values())
print(student.items())  # this is useful for looping through. because if we use lopp without any method, we just loop through the keys:
for key in student:
    print(key)
# but
for key, value in student.items():
    print(key, value)

# empty dictionary
empty_dic = {}

# sorting a dictionary
student = {'name': 'Ben', 'age': 30, 'courses': ['Math', 'Art'], '100': 500}
s_student = sorted(student)  # it returns a list of keys sorted alphabetically
print(s_student)

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros). this is the conventional method:
my_dict = {}
for name, hero in zip(names, heros):
    if name !='Peter':
        my_dict[name] = hero
print(my_dict)
# using dictionary comprehension
my_dict = {name: hero for name, hero in zip(names, heros) if name!='Peter'}
print(my_dict)
