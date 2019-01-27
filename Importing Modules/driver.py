import my_module  # or import my_module as mm. it must be noted that the file is run upon importing and in this case print the message.

courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_module.find_index(courses, 'Math')
print(index)

# import only one function
from my_module import find_index  # in this way, we can get rid of the module name and we only imported the function
index = find_index(courses, 'Math')
print(index)

from my_module import find_index as f, test  # we can import multiple values. we can also "from my_module import *", but this is not recommended. because we now don't know which variable is from the module and which not
index = f(courses, 'Math')
print(index)
print(test)

#
import sys
print(sys.path)  # it shows the paths that Python look for a mudule when imported. the current directory is always there. if the module is not there, we can append the directory which our module is to the sys.path list:
sys.path.append('C:\\Users\\LENOVO\\Desktop\\Python\\new folder')  # the better way is to add this path to the environment variables
print(sys.path)
