### Unit 1.4 Print Odds
for num in range(0, 100):
    if num % 2 == 1:
        print num


### Unit 1.5 FizzBuzz
n = 15
for num in range(1, n+1):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


### Unit 1.6 Find the smallest number
# Psuedo code
# let smallest = first
# for i in deck:
#     if i < smallest:
#         smallest = i
# solution
arry = [2, 4, 6, 8, 1, 3]
smallest = arry[0]
for i in arry:
    if i < smallest:
        smallest = i
print (smallest)



### Unit 1.7
## 1 reverse the string
# example input: hello
# example output: olleh
## Easy
first_string = "hello"
end_string = ""
for letter in first_string:
    end_string = letter + end_string
print(end_string)

## Using extended slice syntax
txt = "slice" [::-1]
print(txt)

## Using reversed
txt = "".join(reversed("reversed"))
print(txt)

## Using recursion
str = "recursion"
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
print(reverse(str))
# Explanation : In the above code, string is passed as an argument to a recursive function to reverse the string. In the function, the base condition is that if the length of the string is equal to 0, the string is returned. If not equal to 0, the reverse function is recursively called to slice the part of the string except the first character and concatenate the first character to the end of the sliced string.



## 2 Sum of array
arry3 = [1, 2, 3]
sum3 = 0
for num in arry3:
    sum3 += int(num)
print(sum3)

print(sum(arry3))


## 3 Find the largest
arry2 = [1, 2, 3]
largest = arry2[0]
for i in arry2:
    if i > largest:
        largest = i
print largest
