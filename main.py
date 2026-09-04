# 1
import modules

a = 10
b = 5
print("Addition:", modules.add(a, b))
print("Subtraction:", modules.subtract(a, b))
print("Multiplication:", modules.multiply(a, b))
print("Division:", modules.divide(a, b))




#2
import modules

text = input("Enter a string: ")

print("Reverse:", modules.reverse_string(text))
print("Vowels:", modules.count_vowels(text))
print("Uppercase:", modules.uppercase_string(text))

#3Generate 5 Random Integers
import random
for i in range(5):
    print(random.randint(1, 100))



#4.display current date and time
from datetime import datetime
now = datetime.now()
print("Current Date and Time:", now)
print("Date:", now.date())
print("Time:", now.time())




#5.Find Factorial Using Math Module
import math
n = int(input("Enter a number: "))
print("Factorial:", math.factorial(n))



#7.from calculator import add, subtract, multiply
from modules import add, subtract, multiply
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))



#8. Shuffle a List Using Random Module
import random
numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)
random.shuffle(numbers)
print("Shuffled List:", numbers)




#9.Calculate Difference Between Two Dates
from datetime import date
date1 = date(2026, 1, 1)
date2 = date(2026, 9, 4)
difference = date2 - date1
print("Difference in days:", difference.days)




#10. List Files in a Directory Using OS Module
import os
folder = "."
files = os.listdir(folder)
print("Files in directory:")
for file in files:
    print(file)
