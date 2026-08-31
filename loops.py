#1.print number 1 to 10.
for i in range(1,11):
    print(i)


while True:
    bal=200
    am=float(input("amount : "))
    if am<=0:
        print("pese nahi he")
    else:
        bal+=am    
        print("aavi gaya")
        print(bal)
        break


#2.display multiplication for given table.
num=int(input("Enter your number :"))
for i in range(1,11):
 print(f"{num} x {i} = {num * i}")





#3.find fectorial of num.
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")



#4.generate first n fibonacci number.
n = int(input("Enter the value of n: "))
a, b = 0, 1
series = []
for _ in range(n):
    series.append(a)
    a, b = b, a + b
print(f"First {n} Fibonacci numbers:")
print(series)



#5.check if number is prime.
num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")




#6. Program to reverse a number
num = int(input("Enter a number: "))
temp = abs(num)
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if num < 0:
    reversed_num = -reversed_num
print(f"Reversed number: {reversed_num}")



#7Count digits in a number
def count_digits(n):
    n = abs(n)  # handle negative numbers
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count




#8. Sum of even numbers between 1 and 100
total = sum(num for num in range(1, 101) if num % 2 == 0)
print("Sum of even numbers:", total)



#9. Print a pyramid pattern
n = 5  
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

