student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for scores in student_scores:
    if student_scores[scores] >= 91:
        student_grades[scores] = "Outstanding"
    elif student_scores[scores] >= 81 and student_scores[scores] <= 90:
        student_grades[scores] = "Exceeds Expectations"
    elif student_scores[scores] >= 71 and student_scores[scores] <= 80:
        student_grades[scores] = "Acceptable"
    else:
        student_grades[scores] = "Fail"
        
print(student_grades)