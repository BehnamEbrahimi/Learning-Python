first_name = 'Ben'
last_name = 'Abe'

sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)

sentence = f'My name is {first_name.upper()} {last_name}'  # better method
print(sentence)

person = {'name': 'Jenn', 'age': 23}
sentence = f"My name is {person['name']} and i am {person['age']}"  # for dictionaries be very careful with " and '
print(sentence)

calculation = f'4 times 11 is equal to {4*11}'  # inside f string we can do calculations
print(calculation)

for n in range(1, 11):
    sentence = f'The value is {n:02}'  # zero padding
    print(sentence)

pi = 3.14159265
sentence = f'Pi is equal to {pi:.3f}'  # 3 decimal places
print(sentence)

from datetime import datetime
birthday = datetime(1990, 1, 1)
print(f'My birthday is on {birthday:%B %d, %Y}') # the date formats can be found in Python documentations
