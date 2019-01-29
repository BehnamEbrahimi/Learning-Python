# closures: return inner functions that remember and have access to the variables in their scope
def outer_function(message):

    def inner_function():
        print(message)
    # return inner_function() # the outer function excutes the inner function
    return inner_function  # the outer function returns the inner function without excuting it


hi_func = outer_function('Hi')  # it returns the inner function waiting to be excuted
bye_func = outer_function('Bye')

hi_func()
bye_func()
hi_func()  # it remembers the message even after excuting the outer function

# decorator is a function that takes another function as an argument, adds some kind of functionalities and returns another function without altering the source code of the original function. decorator is a closure which instead of a variable, receives the original function:


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  # to pass accept arbitary number of positional or keyword arguments for our functions
        print(f'wrapper excuted this before{original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)  # returns the wrapper function waiting to be excuted. instead of this line we usually write: @decorator_function above the display function
decorated_display()  # here it just prints another msg and then excutes the original function and returns it


@decorator_function  # the same as: display2= decorator_function(display2)
def display2():
    print('display2 function ran')


display2()

# if the original function takes some parameters


@decorator_function  # we decorate two function with same decorator function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)

# decorator class: it is like the decorator function but some people use this. i prefer the decorator function.


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):  # it implements the extra functionality as the wrapper function
        print(f'call method excuted this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)

# practical example

# from functools import wraps


def my_logger(orig_func):  # we can reuse this logging functionality with every function that we want
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    # @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):  # it shows how long  it takes to run the functions that are decorated with this function
    import time

    # @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


import time


@my_logger  # two decorators stacked together means: display_info = my_logger(my_timer(display_info)). in this way, my_timer decorator returns wrapper function, and the name of the log file will be wrapper.log. to prevent this we must preserve the information of our original function and to do that, we must import "from functools import wraps" and decorate our wrapper functions with @wraps() decorator
@my_timer
def display_info(name, age):
    time.sleep(1)  # adds 1 sec to run this function
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Tom', 22)
