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

# Else clauses on loops
my_list = [1, 2, 3, 4]

for i in my_list:
    print(i)
    if i == 5:
        break
else:  # else in for-loop means no break meaning: if there is no break, else block will be executed
    print('Hit the For/Else Statement!')
    
# finder example for for-else
def find_index(to_search, target):
  for i, value in enumerate(to_search):
    if value == target:
      break
  else:
    return -1
  return i

my_list = ['Corey', 'Rick', 'John']
index_location = find_index(my_list, 'Steve')

print 'Location of target is index: {}'.format(index_location)

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
# while-else
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 8:
        break
else:
    print('Hit the While/Else Statement!')
