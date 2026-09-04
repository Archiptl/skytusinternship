#1.create a class with attribute like brand,model and speed and methods to accelerate.
class car:
    def __init__(self,brand, model, speed):
          self.brand=brand
          self.model=model
          self.speed=speed
car1=car("Tesla","Model 3",120)
print(car1.brand)
print(car1.model)
print(car1.speed)
  


#2.create BankAccount class with deposit and withdraw methods.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

person1 = BankAccount(1000)
person1.deposit(500)
person1.withdraw(200)
print(person1.balance)
        


#3.create a Student class with a method to calculate average marks.
class StudentMark:
     def __init__(self,math,phy,che,com):
          self.math=math
          self.phy=phy
          self.che=che
          self.com=com
     def avg (self):
        data=(self.math+self.phy+self.che+self.com)/4
        print("avg: ",data)
math=int(input("math : "))
phy=int(input("phy : "))
che=int(input("che : "))
com=int(input("com : "))
student1=StudentMark(math,phy,che,com)
student1.avg()





#4.create rectangle class with methods to find area and perimeter.
class Rectangle:
     def __init__(self,length,width):
          self.length=length
          self.width=width
     def area(self):
          area1=(self.length+self.width)
          print("Area of Rectangle :",area1)
     def perimeter(self):
          perimeter1=(self.length*self.width)
          print("Perimeter of Rectangle :",perimeter1)

length=int(input("Length of Rectangle :"))
width=int(input("Width of Rectangle :"))

data=Rectangle(length,width)
data.area()
data.perimeter()          



#5.create an Employee class that displays salary details.
class Employee:
     def __init__(self,salary):
          self.salary=salary
          def employee1(self):
               print("salary :",employee1)
salary=int(input("salary:"))



#6.create a Book class to store title,author,and price and display details.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book1 = Book("IT ENDS WITH US", " Colleen Hoover", 500)
book1.display_details()


#7.create a Circle class to find area and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area1 = 3.14 * self.radius * self.radius
        print("Area of Circle :", area1)

    def circumference(self):
        circumference1 = 2 * 3.14 * self.radius
        print("Circumference of Circle :", circumference1)
radius = int(input("Radius of Circle : "))

data = Circle(radius)
data.area()
data.circumference()



#8.create a Laptop class with a method to apply discount on price.
class Laptop:
    def __init__(self,current_price,discount_price):
        self.current_price = current_price
        self.discount_price=discount_price

    def _current_price(self):
        print("Current Price :",self.current_price)

    def _discount_price(self):
            print("Discount Price :",self.discount_price)

    def total_price(self):
            total_price=self.current_price - self.discount_price
            print("Pay Price :",total_price)

current_price=float(input("Current Price :"))
discount_price=float(input("Discount Price :"))
p1=Laptop(current_price,discount_price)

p1._current_price() 
p1._discount_price()
p1.total_price()  

     
     

#10.create a shop class with method to add and list products.
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product, "added to the shop.")

    def list_products(self):
        print("Products in the shop:")
        for product in self.products:
            print("-", product)
shop = Shop()
shop.add_product("Laptop")
shop.add_product("Mobile")
shop.add_product("Headphones")
shop.list_products()




#9.create a Flight class with seat booking functionality.
class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = set()

    def book_seat(self, seat_number):
        if seat_number < 1 or seat_number > self.total_seats:
            return "Invalid seat number."

        if seat_number in self.booked_seats:
            return f"Seat {seat_number} is already booked."

        self.booked_seats.add(seat_number)
        return f"Seat {seat_number} booked successfully."

    def cancel_seat(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            return f"Seat {seat_number} cancelled successfully."

        return f"Seat {seat_number} is not booked."

    def is_available(self, seat_number):
        return seat_number not in self.booked_seats

    def available_seats(self):
        return [
            seat for seat in range(1, self.total_seats + 1)
            if seat not in self.booked_seats
        ]

flight = Flight("AI101", 5)

print(flight.book_seat(2))
print(flight.book_seat(4))
print(flight.book_seat(2))

print("Available seats:", flight.available_seats())

print(flight.cancel_seat(2))
print("Available seats:", flight.available_seats())
