# -------------------------------
# Day 6 - Python While Loop Practice
# -------------------------------


# 1. Print numbers from 1 to 10 using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1


# 2. Print numbers from 10 to 1 using a while loop
i = 10
while i >= 1:
    print(i)
    i -= 1


# 3. Print even numbers from 1 to 20 using while
i = 2
while i <= 20:
    print(i)
    i += 2


# 4. Take a number from the user and print its multiplication table
n = int(input("Enter a number for multiplication table: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


# 5. Find the sum of numbers from 1 to n
n = int(input("Enter a number: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# 6. Reverse a number using while
num = int(input("Enter a number to reverse: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)


# 7. Count the number of digits in a number
num = int(input("Enter a number to count digits: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)


# 8. Keep asking user for numbers until 0 is entered and find the sum
total = 0
num = int(input("Enter number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))

print("Total Sum =", total)