import csv

file = open("Admission.csv","r")
reader = csv.reader(file)

print("Records from the file are below : ")

for i in reader:
    print(i)

file.close()    