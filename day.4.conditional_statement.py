#CONDITIONAL STATEMENTS PRACTICE


#QUESTION 1: Write a Python program to take a number from the user and check whether it is positive, negative, or zero.
a= int(input("enter the number:"))
if a>0:
    print("the number is positive")
elif a<0:
    print("the number is negative")
elif a==0:
    print("enter the digit is zero")

#QUESTION 2:Write a Python program to take a number from the user and check whether the number is even or odd.
b= int(input("enter the number:"))
if b%2 ==0:
    print("the number entered is even")
else:
    print("enterd number is odd")

#QUESTION 3: Write a Python program to take two numbers from the user and print the largest number.
num1= int(input("enter the 1st number"))
num2 = int(input("enter the 2nd number"))
if num1>num2:
    print("the 1st number is greater than 2nd number")
else:
    print("the 2nd number is greater than 1st number")

#QUESTION 4: Write a Python program to take three numbers from the user and print the largest among them
x= int(input("enter your 1st number:"))
y= int(input("enter your 2nd number:"))
z= int(input("enter your 3rd number:"))
if x>y and x>z:
    print("x is greater among all")
elif y>x and y>z:
    print("y is greater among all")
elif z>x and z>y:
    print("z is greater among all")

#QUESTION 5: Write a Python program to take age as input and check whether the person is eligible for voting (age ≥ 18).
age = int(input("kindly enter your age:"))
wait = 18 - age
if age>= 18:
    print("you are eligible to vote")
else:
    print("kindly wait for",wait,"years")

#QUESTION 6 :Write a Python program to take a number from the user and check whether it is divisible by both 5 and 11
A = int(input("enter your number which you want to check :"))
if A%5==0 and A%11 ==0:
    print("the entered number is divisible by both")

#QUESTION 7 :Write a Python program to take a year as input and check whether it is a leap year or not
year = int(input(" enter the year you want to check:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("the year is a leap year")

#QUESTION 8: Write a simple login system
#where the username is "admin" and the password is "1234" and check whether the entered credentials are correct or not
username = input("please enter youur username :")
password = int(input("please enter your password :"))
if username=="admin" and password== 1234:
    print("THANKYOU FOR LOGGING IN")
    