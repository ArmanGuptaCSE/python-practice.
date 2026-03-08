#OPERATORS PRACTISE


#QUESTION 1: Take two numbers from the user and print their sum
a = 3
b = 4
sum = a+b
print("the sum is:",sum)

#QUESTION 2: Take two numbers from the user and print their sum
a = int(input("enter your first number:"))
b = int(input("enter your second number:"))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

#QUESTION 3:Take a number from the user and print its square using operator
num1 = int(input("enter the number: "))
square = num1*num1
print(" the square of the given number :", square) 

#QUESTION 4: find the quoteint of the number taken from user divided by 2
number= float(input("enter your number: "))
x = number%2
print("the quotient is :", x)

#QUESTION 5: Take a number from the user and check even or odd
num2 = int(input(" enter the number:"))
if num2%2 == 0:
    print(" the number is even")
else:
    print("the number is odd")

#QUESTION 6: take a number and check is it multiple of 5 or not
num3 = int(input("enter the number you want to check"))
if num3%5 == 0:
    print("the number is multiple of 5")
else:
    print("the number is not multiple of 5")

#QUESTION 7: Check if the person is eligible to vote
age = int(input("enter your age:"))
if age >= 18:
    print("you can vote")
else: 
    print(" sorry! you can't vote")

#QUESTION 8: Power Calculator
base = int(input(" enter your base :"))
exponent = int(input("enter your exponent value:"))
power = base**exponent
print("the power of your numbe is :",power)


