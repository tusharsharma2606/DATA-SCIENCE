# cSpell:ignore Rahul Akshat
import csv

file=open("C:\\Users\\tusha\\Desktop\\JU 2nd Year\\Python\\akshat.csv", "w", newline='')

writer=csv.writer(file)

writer.writerow(["Name", "Age", "City"])
writer.writerow(["Akshat", 25, "New York"])
writer.writerow(["John", 30, "Los Angeles"])
writer.writerow(["Rahul", 35, "Chicago"])

file.close()

print("CSV file created and data written successfully.")
