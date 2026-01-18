# Student Marks Analyzer using Functions and Loops

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def analyze_student():
    name = input("Enter student name: ")
    obtained_marks = int(input("Enter obtained marks out of 500: "))

    total_marks = 500
    percentage = (obtained_marks / total_marks) * 100
    grade = calculate_grade(percentage)

    result = (
        "Student Name: " + name + "\n"
        "Obtained Marks: " + str(obtained_marks) + "\n"
        "Percentage: " + str(round(percentage, 2)) + "%\n"
        "Grade: " + grade + "\n"
        "-------------------------\n"
    )

    file = open("output.txt", "a")
    file.write(result)
    file.close()

    print("Result saved!\n")


def main():
    while True:
        analyze_student()
        choice = input("Do you want to add another student? (yes/no): ")
        if choice.lower() != "yes":
            break

    print("All student results saved in output.txt")


main()
