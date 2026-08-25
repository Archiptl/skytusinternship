#1. take a string input and print its length.
string=input("Enter the string :")
print("length",len())



#2. sentence in to lowercase.
string=input("Enter the sentence :")
print(string.lower())



#3.replace space with underscore
string=input("Enter the sentence :")
print(string.replace(" ","_"))



#4.extract the first and last character of a string.
string=input("Enter your string :")
print("First:",string[0])
print("Last:",string[-1])



#5.reverse a string using slicing
string=input("Enter your string :")
print(string[::-1])



#6.count how many time a letter appears in a in a string.
string=input("Enter your string :")
letter=input("Enter your letter : ")
print(string.count(letter))



#7.Check if a word is present in a sentence.
sentence =input("Enter your sentence :")
word=input("Enter your word :")
if word in sentence :
    print("word is present")
else:
    print("word is not present ")



#8.Take name & age and print using f-string formatting.
name=input("enter your name:")
age=int(input("enter your age :"))
print(f"my name is {name} and my age is {age}")



#9.Remove extra spaces from the start and end of a string.
string = input("Enter a string: ")
print(string.strip())



#10.Join a list of words into a single string with - between them.
word = ["hi","go","nice"]
result='-'.join(word)
print(result)



#11.Create a list of your 5 favorite movies.
movie = ["kkr","kgf","dangal","kgf2","etha"]
print(movie)


#12.Add a new movie to the list.
movie = ["kkr","kgf","dangal","kgf2","etha"]
movie.append("kkr2")
print(movie)



#13.Remove the first movie from the list.
movie = ["kkr2","kgf","dangal","kgf2","etha"]
movie.pop(0)
print(movie)


#14.Sort a list of numbers in ascending order
num=[25,36,58,5,8,56,56]
num.sort()
print(num)



#15.Reverse a list.
num=[25,36,58,5,8,56,56]
num.reverse()
print(num)



#16.Find the largest number in a list.
num=[25,36,58,5,8,56,56]
print("largest:",max(num))


#17.Merge two lists into one.
list1=[26,38,36]
list2=[91,39,88]
list3=list1+list2
print(list3)


#18.Access the last element of a list without using index number.
num=[25,36,58,5,8,56,56]
print(num.pop(0))


#19.Create a nested list and access a specific inner element.
num=[[12,43][23,23]]
print(num[0][3])

#20.Count how many times an element appears in a list.
string=input("Enter your string :")
letter=input("Enter your letter : ")
print(string.count(letter))
