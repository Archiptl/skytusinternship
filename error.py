#1.Handle division by zero error.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


#2.Handle Invalid Integer Input
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: Please enter a valid integer.")



#3.Handle File Not Found Error
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")




#4. Demonstrate Multiple Exception Blocks
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except ValueError:
    print("Error: Invalid input.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")




#5. Use Finally for Resource Cleanup
file = None
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

finally:
    if file:
        file.close()
    print("File closed. Resource cleanup completed.")


#6. Create Custom
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("You are eligible.")

except InvalidAgeError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid age.")


       
#7. Handle IndexError When Accessing a List
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Please enter a valid index.")




#8. Take Two Numbers and Handle All Possible Errors
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected error:", e)




#9. Log Errors to a File Instead of Printing
import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except Exception as e:
    logging.error("An error occurred: %s", e)
    print("Error occurred. Check error.log file.")




#10. Validate Email Format and Raise Exception
import re

class InvalidEmailError(Exception):
    pass


try:
    email = input("Enter your email: ")

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format.")

    print("Valid email.")

except InvalidEmailError as e:
    print("Error:", e)        