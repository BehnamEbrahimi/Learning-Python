import os

print(os.getcwd())  # prints the current working directory
print(os.__file__) # __file__ method shows the directory where the standard library is.
print(dir(os))  # shows all the methods and attributes

os.chdir('c:\\Users\\LENOVO\\Desktop\\Python\\new')
print(os.getcwd())
os.chdir('c:\\Users\\LENOVO\\Desktop\\Python\\')
print(os.listdir())  # prints all the files and directories as a list > iterable
os.mkdir('new folder')  # creates the directory
os.makedirs('new_new\\new2')  # better choice: creates all the required directories
os.rmdir('new folder')  # better choice: deletes just the bottom directory
os.removedirs('new_new\\new2')  # removes all the directories
os.rename('new', 'new_renamed')
os.rename('new_renamed', 'new')

print(os.stat('new'))  # return size, modification time (in time stamp),...
import datetime
mod_time = os.stat('new').st_mtime
print(datetime.date.fromtimestamp(mod_time))  # human readable format

for dirpath, dirnames, filename in os.walk('c:\\Users\\LENOVO\\Desktop\\Python'):  # os.walk() is a generator and returns a tuple and travers all the folders. it is useful for search
    print('current path:', dirpath)
    print('directories:', dirnames)
    print('files:', filename)

print(os.environ.get('Temp'))  # IMPORTANT: the value of environment variable. this is very useful for hiding secret passwords and informations

print(os.path.join(os.environ.get('Temp'), 'test.txt'))  # os.path.join() method takes two paths and return the concatination of them and you dont have to worry about the \
print(os.path.basename('c:\\Users\\LENOVO\\Desktop\\Python.py'))  # returns the basename. the path does not have to exist
print(os.path.dirname('c:\\Users\\LENOVO\\Desktop\\Python.py'))  # returns the dirname. the path does not have to exist
print(os.path.split('c:\\Users\\LENOVO\\Desktop\\Python.py'))  # returns a tuple. the path does not have to exist
print(os.path.splitext('c:\\Users\\LENOVO\\Desktop\\Python.py'))  # returns a tuple of base and the extension
print(os.path.exists('c:\\Users\\LENOVO\\Desktop\\fake'))  # checks if a path exists
print(os.path.isdir('c:\\Users\\LENOVO\\Desktop\\Python\\intro.py'))  # checks if the path is a directory
print(os.path.isfile('c:\\Users\\LENOVO\\Desktop\\Python\\intro.py'))  # checks if the path is a file
