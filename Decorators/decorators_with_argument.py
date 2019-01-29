def prefix_decorator(prefix):  # to add parameters to decorator function we add another level and pass the parameters to it. now the inner functions have access to that enclosing variable(s) and  we must return the decorator function unexecuted. finally, we replace the @decorator_function with @ prefix_decorator
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('Log:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)
