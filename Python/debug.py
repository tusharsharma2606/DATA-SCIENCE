# Get user input and convert to number
marks = int(input("Enter Marks: "))

# Conditional grading logic
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
