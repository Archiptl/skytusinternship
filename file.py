#1.read a file and display its contents.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()




#2. Count the number of lines in a file
file = open("data.txt", "r")
lines = file.readlines()
print("Number of lines:", len(lines))
file.close()



#3.Count how many times each word appears in a file
file = open("data.txt", "r")
words = file.read().split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
for word, times in count.items():
    print(word, ":", times)
file.close()




#4.Write 5 user-entered sentences to a file
file = open("sentences.txt", "w")
for i in range(5):
    sentence = input("Enter sentence: ")
    file.write(sentence + "\n")
file.close()
print("nice")





#5.Append a list of strings to an existing file
file = open("data.txt", "a")
strings = ["Hello", "Python", "Programming", "File Handling"]
for text in strings:
    file.write(text + "\n")
file.close()
print("Strings appended successfully.")




#6.Print only lines containing a specific word
file = open("data.txt", "r")
word = input("Enter word to search: ")
for line in file:
    if word in line:
        print(line, end="")
file.close()




#7.Replace a specific word and save changes
file = open("data.txt", "r")
content = file.read()
old = input("Enter word to replace: ")
new = input("Enter new word: ")
content = content.replace(old, new)
file.close()
file = open("data.txt", "w")
file.write(content)
file.close()
print("Word replaced successfully.")





#8.Merge two text files into a third file
data = open("data.txt", "r")
file2 = open("file2.txt", "r")
file3 = open("merged.txt", "w")
file3.write(data.read())
file3.write("\n")
file3.write(file2.read())
data.close()
file2.close()
file3.close()
print("Files merged successfully.")





#9.Read a CSV file and display its content in formatted way
import csv
file = open("data.csv", "r")
reader = csv.reader(file)
for row in reader:
    print(" | ".join(row))
file.close()





#10.Back up a file by copying its contents into another file
source = open("data.txt", "r")
backup = open("file2.txt", "w")
backup.write(source.read())
source.close()
backup.close()
print("Backup created successfully.")