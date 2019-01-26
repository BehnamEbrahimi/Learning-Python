# int and float
num = 3
print(type(num))  # returns int
num = 1.5
print(type(num))  # returns float

print(3 / 2)  # returns 1.5
print(3 // 2)  # returns floor division
print(3**2)  # power
print(3 % 2)  # remainder. especially useful to check even and odd number

num += 1  # increment by one
print(num)

# built-in functions
print(abs(-2))
print(round(1.6))
print(round(3.141592, 3))  # the second argument is the decimals

# comparisons (all the below are True):
# 2==2
# 3!=2
# 3>2
# 2<3
# 3>=2
# 2<=3
print(3 > 2)

# casting
num_1 = '1'
num_2 = '2'
print(num_1 + num_2)  # string concatination
print(int(num_1) + int(num_2))  # casting
