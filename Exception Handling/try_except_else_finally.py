# most of the time we use just the first two blocks
try:
    # f = open('test.txt')
    # var = bad_var
    if True:
        raise Exception # manually raise an exception
except FileNotFoundError:  # it is better to be specific as possible
    print('sorry. cant find the file')  # if try block fails
except Exception as e:  # catch a lot of excceptions
    print('sorry. sth went wrong:' + str(e))  # if try block fails
else:  # no exception. it runs if try blocks throws no exceptions.
    print(f.read())
    f.close()
finally:  # no matter what, this block will be executed regardless of the code successfully running. like closing down a database
    pass
