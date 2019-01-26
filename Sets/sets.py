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
