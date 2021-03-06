# lists are mutable but tuples are immutable
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'  # because lists are mutable, by changing the value of list_1, list_2 will be changed accordingly

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# the line below can not run because, tuples can not be changed
# tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# sorting tuples, the sort() method is not working for tuples but sort function works
tup = (9, 1, 8, 2, 7, 3, 6, 5, 4)
s_tup = sorted(tup)  # it returns a list!
print(s_tup)
