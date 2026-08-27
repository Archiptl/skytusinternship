#1.function to check num is prime or not.
def num(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n %i ==0:
            return True
number=int(input("Enter your number :"))
if num(number):
    print("Prime number")
else:
    print("Not prime number")        




#2.reverse string
def reverse(s):
    return s[::-1]
string=input("enter your string :")
print("reverse string :",reverse(string))



#3.find fectorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
num = int(input("Enter your number: "))
print(factorial(num))



#4.calculate simple interest
def interest(p,r,t):
    si=(p*r*t)/100
    return si
p=float(input("enter principal:"))
r=float(input("enter rate:"))
t=float(input("enter time:"))
print("Simple rate:",interest(p,r,t))



#5.word is palindrome
def palindrome(word):
    return word == word[::-1]
word = input("Enter a word: ")
if palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")



#6.count vowels in a string
from collections import Counter
def vowel_breakdown(s):
    counts = Counter(c for c in s.lower() if c in "aeiou")
    return counts
text = "The quick brown fox jumps over the lazy dog"
print(vowel_breakdown(text))




#7.marge two lists.
def merge_lists(list1, list2):
    return list1 + list2
a = [1, 2, 3]
b = [4, 5, 6]
result = merge_lists(a, b)
print(result)




#8.GCD of two num
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(12, 18))





#9.area of rectangles
def area_rectangle(length, width):
    return length * width
length = 10
width = 5
print("Area of rectangle:", area_rectangle(length, width))





#10.armstrong num
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num
num = int(input("Enter a number: "))
if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")