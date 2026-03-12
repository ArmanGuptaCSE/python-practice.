# 1. Write a program to print numbers from 50 to 1 using a while loop.

i = 50
while i >= 1:
    print(i)
    i -= 1


# 2. Write a program to print the sum of all odd numbers between 1 and 100 using a while loop.

i = 1
sum = 0

while i <= 100:
    if i % 2 != 0:
        sum += i
    i += 1

print("Sum of odd numbers =", sum)


# 3. Write a program to print the first 10 multiples of 7 using a while loop.

i = 1

while i <= 10:
    print(7 * i)
    i += 1


# 4. Write a program to check whether a number is a palindrome using a while loop.

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")


# 5. Write a program to find the sum of digits of a number using a while loop.

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits =", sum)


# 6. Write a program to print Fibonacci series up to 10 terms using a while loop.

a = 0
b = 1
count = 1

while count <= 10:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1


# 7. Write a program to keep asking the user for numbers and print their sum until the user enters -1.

total = 0
num = int(input("Enter a number (-1 to stop): "))

while num != -1:
    total += num
    num = int(input("Enter a number (-1 to stop): "))

print("Total sum =", total)


# 8. Write a program to count how many even and odd numbers are entered by the user until they enter 0.

even = 0
odd = 0

num = int(input("Enter a number (0 to stop): "))

while num != 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    num = int(input("Enter a number (0 to stop): "))

print("Even numbers =", even)
print("Odd numbers =", odd)