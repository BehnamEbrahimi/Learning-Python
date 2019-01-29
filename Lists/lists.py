#
courses = ['Math', 'Physics', 'Art', 'Chemistry']
print(courses)
print(len(courses))  # returns number of members
print(courses[1])  # returns the second place (index = 1)
print(courses[-1])  # returns the last item. It is better way to access the last item.
print(courses[0:2])  # list slicing.
print(courses[1:])  # just like strings, the first or second indexes can be left off

# adding an item
courses.append('Computer')  # adds to the end of the list
courses.insert(0, 'Geology')  # the first argument is the index to be inserted
print(courses)

# adding items of another list. if you use "insert method" or "append method, you will have a nested list!
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.extend(list_2)
print(list_1)

# remove values
courses.remove('Math')
courses.pop()  # removes the last item and returns the last item
course = courses.pop()
print(course)
print(courses)

# sorting lists
courses.reverse()  # reversing
print(courses)
courses.sort()  # sorting alphabetically or ascending
print(courses)
courses.sort(reverse=True)  # sorting descending
print(courses)
print(sorted(courses))  # does not change the original
print(courses)
li = [9, 1, 8, 2, 7, 3, 6, 5, 4]
s_li = sorted(li)  # it returns a sorted list and the original is untouched
print(s_li, li)
li.sort()  # the original will be afected. it returns None
print(li)
s_li = sorted(li, reverse=True)  # descending order
print(s_li)
li.sort(reverse=True)  # descending order
print(li)
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)  # sorting based on absolute value. key takes a function
print(s_li)

# built-in functions
print(list_1)
print(min(list_1)) # min function takes any iterable such as list
print(max(list_1))
print(sum(list_1))

# find index of a certain value
print(courses.index('Geology'))
print('Art' in courses)  # returns True
print('Math' in courses)  # returns False

# for loop
for item in courses:  # a list can be used in a for loop
    print(item)

# enumerate function: returns both index and value
for index, course in enumerate(courses):
    print(index, course)
for index, course in enumerate(courses, start=1):  # changing the starting index
    print(index, course)

# converting a list to string with join function
converted_str = ', '.join(courses)
print(converted_str)

# converting a string to a list with split method
print(converted_str.split(', '))

# Empty Lists
empty_list = []
empty_list = list()

# list slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9 : positive index
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 : negative index
# list[start:end:step]
print(my_list[-8:6])  # we can combine positive and negative index
print(my_list[0:-1: 2]) # every other value
print(my_list[::-1])  # it is like reverse. by leaving out the start and end it starts from the beginning to the end

# list comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = [n for n in nums]  # instead of writing for loop and appending each value
print([n for n in nums])

# I want 'n*n' for each 'n' in nums
my_list = [n * n for n in nums]  # instead of writing for loop and appending each value
print(my_list)
# Using a map + lambda
my_list = list(map(lambda n: n * n, nums))  # map runs everything in the list through a certain function and returns an iterable so we need to cast it to a list. lambda is an anonymous function. of course the list comperehension is more readable
print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
my_list = [n for n in nums if n % 2 == 0]  # instead of writing for loop and appending each value
print(my_list)
# Using a filter + lambda
my_list = list(filter(lambda x: x % 2 == 0, nums))  # filter runs everything in the list through a certain function and returns the original value as an iterable if the function evaluates as True. of course list comperehension is more readable
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = [(letter, num) for letter in 'abcd' for num in range(4)] # instead of writing nested for loop and appending each value
print(my_list)
