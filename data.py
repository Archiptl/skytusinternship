#1.Create a tuple with 5 numbers.
tuple=(12,25,25,2,5,26)
print(tuple)


#2.Access the third element in a tuple.
tuple=("hi","hello","bye","hie")
print(tuple[3])


#3.Unpack a tuple into separate variables.
tuple=("hi","hello","bye","hie")
(hi,hello,bye,hie)=tuple
print(hi)
print(hello)
print(bye)
print(hie)




#4.Create a set of 5 fruits.
fruit=("banana","apple","kiwi","orange","cherry")
print(fruit)



#5.Add a new fruit to the set.
fruit=("banana","apple","kiwi","orange","cherry")
fruit=fruit+("green apple",)
print(fruit)


#6.Remove an element from a set.
fruit=("banana","apple","kiwi","orange","cherry")
fruit = tuple(x for x in fruit if x != "kiwi")
print(fruit)


#7.Find union of two sets.
fruit1 = {"banana", "apple", "kiwi"}
fruit2 = {"orange", "cherry", "kiwi"}
fruit = fruit1.union(fruit2)
print(fruit)



#8.Find intersection of two sets.
fruit1 = {"banana", "apple", "kiwi"}
fruit2 = {"orange", "cherry", "kiwi"}
fruit = fruit1.intersection(fruit2)
print(fruit)



#9.Check if one set is subset of another.
fruit1 = {"banana", "apple", "kiwi"}
fruit2 = {"orange", "cherry", "kiwi"}
print(fruit1.issubset(fruit2))

#11. Convert a list with duplicate values into a set to remove duplicates.
fruit = ["banana", "apple", "kiwi", "apple", "banana"]
fruit_set = set(fruit)
print(fruit_set)


#12.Create a dictionary storing student names and marks.
students = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}
print(students)



#13. Add a new key-value pair to an existing dictionary.
students = {
    "Rahul": 85,
    "Amit": 90
}
students["Priya"] = 78
print(students)




#14. Delete a key-value pair from a dictionary.
students = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}
del students["Amit"]
print(students)





#15. Merge two dictionaries into one.
student1 = {
    "Rahul": 85,
    "Amit": 90
}
student2 = {
    "Priya": 78,
    "Neha": 88
}
student1.update(student2)
print(student1)



#16. Check if a key exists in a dictionary.
students = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}
print("Rahul" in students)




#17. Count word frequency in a given string using a dictionary.
text = "apple banana apple kiwi banana apple"
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)




#18. Find the key with the maximum value in a dictionary.
marks = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}
highest = max(marks, key=marks.get)
print(highest)





#19. Reverse keys and values in a dictionary.
students = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}
reversed_dict = {}

for key, value in students.items():
    reversed_dict[value] = key
print(reversed_dict)




#20. Update the value for a specific key.
students = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}
students["Rahul"] = 95
print(students)


#21. Convert a list of tuples into a dictionary.
students = [
    ("Rahul", 85),
    ("Amit", 90),
    ("Priya", 78)
]
students_dict = dict(students)
print(students_dict)