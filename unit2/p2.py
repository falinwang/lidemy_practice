### Unit2.5 find the second largest

arr = [2, 7, 5, 8, 4]
max = arr[0]
max2 = 0

for i in arr:
    # print(i)
    if i > max:
        max2 = max
        # print('max2=', max2)
        max = i
        # print('max=', max)
    elif i > max2:
        max2 = i
        # print('max2=', max2)
        # print('max=', max)

print("final max2 =", max2)

####

first = -2147483648
second = -2147483648
for i in range(0, len(arr)):
    if (arr[i] > first):
        second = first
        first = arr[i]
    elif (arr[i] > second and arr[i] != first):
        second = arr[i]

print("The second largest element is", second)

### Unit2.6 Capitalize all the letters in a string
# ASCII https://zh-yue.wikipedia.org/wiki/ASCII
# A = 65, Z = 90, a = 97, z = 122
# ASCII to int: ord('a') = 97
# int to string str(chr(97)) = 'a'
# Input: Wolverine
# OUTPUT: WOLVERINE

## Psuedo code
# tell if it is lower case
# if not - omit
# if yes - transfer

origin = "Wolverine"
ans = ""
for l in origin:
    # if it is lower case
    if ord(l) <= 122 and ord(l) > 97:
        # if yes: minus 32 to upper case
        ans = ans + str(chr(ord(l) - 32))
    # if not: as original
    else:
        ans = ans + l
print(ans)

# OR using .upper() function
print(origin.upper())

### Unit2.7 Delete specifit letter in a string

str1 = "apple"
letter1 = "l"
str2 = ""
for l in str1:
    if l != letter1:
        # if yes: add it, if not, omit it
        str2 = str2 + l
print(str2)


### Unit2.8 Project 2
# 1. Find the second smallest
# 2. lower case to upper case and vise versa
# 3. Print the factor numbers
