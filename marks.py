# Student Marks Analyzer

name = input("Enter student name: ")

total_marks = 500
obtained_marks = int(input("Enter obtained marks out of 500: "))

percentage = (obtained_marks / total_marks) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

result = (
    "Student Name: " + name + "\n"
    "Obtained Marks: " + str(obtained_marks) + "\n"
    "Percentage: " + str(percentage) + "%\n"
    "Grade: " + grade
)

file = open("output.txt", "w")
file.write(result)
file.close()

print("Result saved successfully!")
