

def avg_of_marks_and_grade():
    subjects = ["math", "chemi", "physi"]
    total = 0
    for sub in subjects:
        marks = int(input(f"Enter the marks for {sub}: "))
        total += marks
    average = total / len(subjects)
    print("Average marks:", average)

    # Grade
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
        
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'

    print("Grade:", grade)


avg_of_marks_and_grade()
