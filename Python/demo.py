# cSpell:ignore tusha tushar
# file = open("C:\\Users\\tusha\\Desktop\\JU 2nd Year\\Python\\tushar.txt.txt", "r")

# content = file.read()

# print(content)

# file.close()

file = open(r"C:\\Users\\tusha\\Desktop\\JU 2nd Year\\Python\\tushar.txt", "w")

file.write("Hello, This is python file handling.\n")
file.write("\nWelcome to python programming.\n")

file.close()

print("Data written successfully to the file.")