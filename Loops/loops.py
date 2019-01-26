# for loops
nums = [1, 2, 3, 4]
for num in nums:
    print(num)
# break. breaks the loop
print('------')
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
# continue. skips to the next iteration
print('------')
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)
# nested loops
for num in nums:
    for letter in 'abc':
        print(str(num) + letter)
# range function
for i in range(10):  # 0 to 9
    print(i)
for i in range(1, 11):  # 1 to 10
    print(i)

# while loops
x = 0
while x < 10:
    print(x)
    x += 1
# infinite loop
x = 0
while True:
    print(x)
    x += 1
    if x == 5:
        break

