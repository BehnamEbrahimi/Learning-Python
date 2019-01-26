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

# built-in functions
print(list_1)
print(min(list_1))
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
