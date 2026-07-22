#!/usr/bin/env python3
from faker import Faker

fake = Faker()

# def create_grade_report(student_grades):
#     with open('grade_report.txt', 'w') as gr:
#         for grade in student_grades:
#                 gr.write(grade + "\n")
# if __name__ == "__main__":
#     student_grades = []
#     grade = input("Student name, grade: ")
#     while grade:
#         student_grades.append(grade)
#         grade = input("Student name, grade: ")
        
#     create_grade_report(student_grades)

print(fake.job())