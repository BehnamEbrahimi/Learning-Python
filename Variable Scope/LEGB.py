# scope of the variables
"""
LEGB
order of variables in Python
Local--> Enclosing -->Global --> Built-in
"""
# local variables: varibles defined in a function
# Enclosing variables: local variables of the enclosing function
# Global variables: variables defined in the module or explicitly declared global
# Built-in: just names predefined in Python

x = 'global_x'
y = 'global_y'
w = 'global_w'


def test(p):
    global w  # do not overuse global keyword
    global v
    x = 'local_x'
    z = 'local_z'
    w = 'local_w'
    v = 'local_v'
    print(x)  # there is local x, so it returns local_x
    print(y)  # because there is no local y, Python looks for global y
    print(w)  # by global keyword we can access global variables
    print(v)  # variable v is defined globally inside a function for the first time
    print(p)


test('local_p')
print(x)  # local x does not live here
# print(z) # error! the local variable does not live outside the function
# print(p)  # error! the local variable does not live outside the function

import builtins
print(dir(builtins))  # returns a list of attributes of a given object
m = min([1, 2, 3])  # if we had defined a min function or variable, Python will use that instead
print(m)
min = 4
print(min)

# Enclosing variables: for nested functions


def outer():
    x = 'outer x'  # local to outer function
    y = 'outer y'
    w = 'outer w'

    def inner():
        x = 'inner x'  # local to inner function
        z = 'inner z'
        nonlocal w  # it changes the scope to the local scope of the enclosing variable
        w = 'inner w'
        print(x)
        print(y)  # because there is no local y, it returns the value of the enclosing variable
        print(w)
    inner()
    print(x)
    print(y)
    print(w)  # by using nonlocal keyword, just like what we did with global variable, we changed w from inner function
    # print(z) # error
