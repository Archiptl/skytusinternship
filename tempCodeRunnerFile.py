import csv
file = open("data.csv", "r")
reader = csv.reader(file)
for row in reader:
    print(" | ".join(row))
file.close()
