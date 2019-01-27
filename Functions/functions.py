# functions. DRY:Do not Repeat Yourself
def blank_func():  # does nothing and returns no errors
    pass


def hello_func():
    print('Hi, Stranger')


hello_func()  # calling a function


def greeting_func(name):  # function with argument
    print(f'Hi, {name}')


greeting_func('Ben')


def hi_func(name):  # function with return value
    return f'Hi, {name}'


print(hi_func('Ben').upper())  # the returned value is a string, so we can use any string method


def my_func(name='stranger'):  # the default value makes the argument unnecessary
    return f'Hi, {name}'


print(my_func('Ben'))
print(my_func())


def greetings(greeting, name='stranger'):
    return f'{greeting}, {name}'


print(greetings('Hello'))
print(greetings('Hello', 'Ali'))  # order matters
print(greetings('Hello', name='Ali'))  # order matters
print(greetings(greeting='Hello', name='Ali'))  # order does not matter
print(greetings(name='Ali', greeting='Hello'))  # order does not matter

# *args for positional arguments, **kwargs for keyword arguments


def func(*args, **kwargs):  # accepts arbitary number of values as input
    print(args)  # returns a tuple of args
    print(kwargs)  # returns a dictionary of kwargs


func('Ben', 'John', level=30, gender='male')

names = ['Ben', 'John']
info = {'level': 30, 'gender': 'male'}
func(names, info) # In this way we cannot pass the arguments  as the above example
func(*names, **info) # unpacks the list as positional arguments and unpacks the dic as kwargs
