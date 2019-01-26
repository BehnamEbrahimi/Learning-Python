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