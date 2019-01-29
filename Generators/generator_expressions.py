# generator expressions instead of generator functions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# way 1: regular genereator


def gen_func(nums):  # generator function
    for n in nums:
        yield n * n


my_gen = gen_func(nums)

for i in my_gen:
    print(i)
    
# way 2: genereator expression
my_gen = (n*n for n in nums) # for generator expression we use parentheses. this way is easier to maintain and more readable
for i in my_gen:
    print(i)
