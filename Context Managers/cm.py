# Context Managers are for efficiently managing resources, they are very useful for files, databases and acquiring and releasing locks
f = open('sample.txt', 'w')
f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
f.close()  # we have to keep in mind to close the file

with open('sample.txt', 'w') as f:  # not only the file closed automatically, if there was any error, the file will be closed properly
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)

# writing our manual context manager by creating a class


class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # the setup of our context manager
        self.file = open(self.filename, self.mode)
        return self.file  # what we return here is the object that we will be working with in our context manager

    def __exit__(self, exc_type, exc_val, traceback):  # the teardown of our context manager. the extra parameters are there for if we throw an exception
        self.file.close()


with Open_File('Sample.txt', 'w') as f:  # the init method and the enter method will be run and the returned object of enter method will be assigned to f
    f.write('testing')
# by exiting the context manager, the exit method will be run

print(f.closed)

# writing our manual context manager by Using contextlib (better way)
from contextlib import contextmanager  # to use the contextmanager decorator


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)  # everything before yield is equivalent to enter method of the previous way (setup)
        yield f  # this part will be run in with statement
    finally:  # we will be sure that no matter what, the file will be closed
        f.close()  # equivalent to exit method (teardown)


with open_file('Sample2.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
# all the codes after the yield will be run by exiting the with-block
print(f.closed)

#### CD Example ####
import os

cwd = os.getcwd()  # setup
os.chdir('Sample-Dir-One')  # setup
print(os.listdir())
os.chdir(cwd)  # teardown

cwd = os.getcwd()  # setup
os.chdir('Sample-Dir-Two')  # setup
print(os.listdir())
os.chdir(cwd)  # teardown


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield # here we dont return anything
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
