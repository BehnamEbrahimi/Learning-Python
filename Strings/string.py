print('Hello World')

# variables in Python should be written all lowercase
# variables shold be descriptive as possible
my_message = 'Hello World'
print(my_message)

# if the string contains '
my_message = "Ali's Book"
my_message = 'Ali\'s Book'  # using escape characters

# multiple lines with """
my_message = """Hello world!
I am here"""
print(my_message)

# length of a string by len() function
my_message = "Hello world!"
print(len(my_message))

# accessing each character
print(my_message[0])

# string slicing: the first index is inclusive but the other index is exclusive
print(my_message[0:5])

# the first or the last index can be left off
print(my_message[1:])

# methods
print(my_message.lower())
print(my_message.upper())
print(my_message.count('l'))
print(my_message.find('world'))  # returns the index of first match
print(my_message.replace('world', 'universe'))  # the original string will not be affected in any of the methods

# dir function" all the methods proveided for a variable
# print(dir(my_message))

# string concatenation
greeting = 'Hello'
name = 'Ben'
message = greeting + ', ' + name + '. Welcome!'  # this method is not recommended in Python. instead use formatted string or f string.
print(message)

# string formatting
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# f string <---Best method, because you can use methods in place holder
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# more information about strings
# print(help(str))
# print(help(str.lower))
