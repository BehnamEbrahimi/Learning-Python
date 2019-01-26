# conditionals
if True:
    print('The conditional is True')

if 1 == 1:
    print('You are a genius')

# if-else
if 1 != 1:
    print('never executed')
else:
    print('this')

# it is like a switch case in Java
language = 'Java'
if language == 'Python':
    print('the language is Python')
elif language == 'C#':
    print('the language is C#')
elif language == 'JavaScript':
    print('the language is JavaScript')
else:
    print('it might be Java')

# and or not
user = 'admin'
logged_out = False
if user == 'admin' and (not logged_out):
    print('Admin Page')
else:
    print('Bad Creds')

# "is" comparison against ==
# "is" checks if two objects are the same in memory (same id and value)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
print(id(a), id(b))
b = a
print(a is b)  # True

# False Values: everything else is evaluated True
# False
# None
# Zero of any numeric type # important: -1 is True
# Any empty sequence. For example, '', (), [], set().
# Any empty mapping. For example, {}.
condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
