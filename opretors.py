#1. remainder of two number 
num1=float(input("Enter the num1 :"))
num2=float(input("Enter the num2 :"))
remainder=num1%num2
print("Remainder :",remainder)



#2.check even or odd num
num=int(input("Enter the num :"))
if num%2==0:
    print("even")
else :
    print("odd")



#3.compare tow num and print larger
num1=int(input("Enter the num1 :"))
num2=int(input("Enter the num2 :"))
print(max(num1,num2))



#4.cal square and cube of number
num=int(input("Enter the number :"))
square=num**2
print("square :",square)
cube=num**3
print("cube :",cube)



#5.check two num are equal
num1=int(input("Enter the num1 :"))
num2=int(input("Enter the num2 :"))
if num1==num2:
    print("are equal")
else:
    print("are not equal")



#6.print true both are positive else false
num1=int(input("Enter the num1 :"))
num2=int(input("Enter the num2 :"))
if num1 and num2>0:
 print("True")
else:
   print("False")



#7.convert float into integer
num=float(input("Enter the num :"))
print(int(num))



#8.
num=input("Enter the num :")
data=int(num)
num2=data*10
print(num2)



#9.AND & OR condition
age=20
marks=75
if age >=18 and marks>=50:
   print("eligible")

age=20
marks=75
if age >=18 or marks>=50:
   print("eligible")   




#10.
num1=float(input("Enter the num1 :"))
num2=float(input("Enter the num2 :"))
remainder=num1%num2
print("Remainder :",remainder)
quotient=num1//num2
print("quotient :",quotient)   
