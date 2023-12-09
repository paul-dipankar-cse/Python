import csv

file = open("Admission.csv","w")
writer = csv.writer(file)
writer.writerow(["Admission Number","Name","Class"])

record = []

option= "Y"
while option == "Y" or option == "y":
    adm = input("Enter Admission Number : ")
    name = input("Enter Your Name : ")
    cl = input("Enter Your Class with Section : ")
    myList = [adm,name,cl]
    record.append(myList)
    option = input("Do You Want to enter more records ? (Y/N) : ")

for i in record:
    writer.writerow(i)

file.close()