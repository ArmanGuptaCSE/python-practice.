#TYPE CASTING PRACTICE

#QUESTION 1:Take a number as string input, convert it to integer, and print the number plus 5.
a= input("enter the number :")
print(type(a))
a=int(a)
print(type(a))
print("sum=",a+5)

#QUESTION 2:Take an integer input, convert it to float, and print the result.
b = 5
b= float(b)
print(b)

#QUESTION 3:Take a float number as input, convert it into integer, and print the result
c = float(input("enter the number:"))
print(type(c))
c = int(c)
print(type(c))

#QUESTION 4: Take two numbers as input (strings), convert them into integers, and print their sum.
num1= input(" enter your first number")
num2= input(" enter your second number")
num1 = int(num1)
num2 = int(num2)
sum= num1+num2
print(sum)

#QUESTION 5: Take two decimal numbers as string input, convert them to float, and print their product
A=2.5
B= 3.0
A = float(A)
B = float(B)

#QUESTION 6: Take age as string input, convert it to integer, and print the age after 5 years
age= input("enter your age")
age = int(age)
after_5years= age+5
print("the age after 5 years is :",after_5years)

#QUESTION 7: Take three numbers as input, convert them to integers, and print the average as float.
x=5
y=8
z=9
x = int(x)
y = int(y)
z = int(z)
average = (x+y+z)/3
average = float(average)
print("the average is",average)

#QUESTION 8:Take seconds as string input, convert it to integer, and print the minutes
seconds = input(" enter the seconds")
seconds= int(seconds)
minutes = seconds/60
minutes = float(minutes)
print("the minutes are",minutes)
