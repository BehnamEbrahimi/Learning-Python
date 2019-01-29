def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])  # this function returns a list
print(my_nums)

# list comprehension
my_nums = [x * x for x in [1, 2, 3, 4, 5]]
print(my_nums)

# using a generator.


def square_numbers1(nums):
    for i in nums:
        yield (i * i)  # this makes it a generator. generators dont hold the whole values in memory, just one result at a time


my_nums = square_numbers1([1, 2, 3, 4, 5])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums)) error: StopIteration
for num in my_nums:  # for-loop knows where to stop iteration
    print(num)

# generator expression
my_nums = (x * x for x in [1, 2, 3, 4, 5])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums)) error: StopIteration
for num in my_nums:  # for-loop knows where to stop iteration
    print(num)

my_nums = (x * x for x in [1, 2, 3, 4, 5])
print(list(my_nums)) # by doing this (casting to the list), we lose the advantage of using generator (memory performance)
