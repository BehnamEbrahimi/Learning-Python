# # Sets: unordered and without duplicate
cs_courses = {'History', 'Math', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Math', 'Design'}

print(cs_courses)  # each time you run, the order will change
print('History' in cs_courses)  # return True
print(cs_courses.intersection(art_courses))  # intersection of two sets.
print(cs_courses.union(art_courses))  # union of two sets.
print(cs_courses.difference(art_courses))  # difference of two sets.

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()

# Adding a member to the set
art_courses.add('Painting')
print(art_courses)

# Set Comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# converting a list to a set. conventional way:
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
# converting a list to a set using set comprehensions:
my_set = {n for n in nums}
print(my_set)
