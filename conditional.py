#1.check person is eligible to vote
age=int(input("Enter your age"))
if age>=18:
    print("Eligible of vote")
else:
    print("Not eligible of vote")


#2.Grade calculator based on marks: 90+ = A, 80+ = B, else C.
marks=int(input("Enter your mark :"))
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
else:
    print("C")



#3.Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
color=input("Enter color")
if color=="red":
    print("Stop")
elif color=="yellow":
    print("wait")
else:
    print("go")



#4.ATM withdrawal check: sufficient balance or not.
balance=float(input("enter your balance:"))
withdrawal=float(input("Enter your withdrawal amount :"))
if withdrawal >balance:
  print("not sufficient balance") 
else:
    print("sufficient balance")





#5.Check if a number is positive, negative, or zero.
num=float(input("Enter your number :"))
if num>0:
    print("positive")
elif num<0:
 print("negative")
else:
    print("zero")   



#6. Check if a number lies within a given range.
number = 7
if 1 <= number <= 10:
    print("Number is within the range")
else:
    print("Number is outside the range")         



#7.Username & password verification.
correct_username = "admin"
correct_password = "secret123"
username = input("Username: ")
password = input("Password: ")
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")



#8.Electricity bill calculator based on units consumed.
units = float(input("Enter electricity units consumed: "))
if units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = (100 * 1.50) + ((units - 100) * 2.50)
elif units <= 500:
    bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
else:
    bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)
print("Electricity Bill = ₹", bill)



#9.Simple calculator (add, subtract, multiply, divide).
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"
print("Result:", result)





#10.Check type of triangle (equilateral, isosceles, scalene).
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")  