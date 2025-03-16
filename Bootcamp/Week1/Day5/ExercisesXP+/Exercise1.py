#!/usr/bin/python3

# Exercise 1 : Student Grade Summary
#Instructions
#
#You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that
#  calculates the average grade for each student, assigns a letter grade, and determines the class average.
#
#
#Initial Data:
#
#
#student_grades = {
#    "Alice": [88, 92, 100],
#    "Bob": [75, 78, 80],
#    "Charlie": [92, 90, 85],
#    "Dana": [83, 88, 92],
#    "Eli": [78, 80, 72]
#}
#
#
#Requirements:
#
#    Calculate the average grade for each student and store the results in a new dictionary called student_averages.
#    Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
#        A: 90 and above
#        B: 80 to 89
#        C: 70 to 79
#        D: 60 to 69
#        F: Below 60
#    Calculate the class average (the average of all students’ averages) and print it.
#    Print the name of each student, their average grade, and their letter grade.
#
#Hints:
#
#    Use loops to iterate through the student_grades dictionary.
#    You may use sum() and len() functions to help calculate averages.
#    Initialize empty dictionaries for student_averages and student_letter_grades before filling them with data.

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}
class_average = 0
for name, grandes in student_grades.items():
    grades_sum = int(sum(grandes)/len(grandes))
    class_average += grades_sum

    if grades_sum >= 90:
        letter = "A"
    elif grades_sum >= 80:
        letter =  "B"
    elif grades_sum >= 70:
        letter =  "C"       
    elif grades_sum >= 60:
        letter =  "D"
    else:
        letter =  "F"          
    student_averages[name] =  letter
    student_letter_grades[name] = [grades_sum, letter]
    #        A: 90 and above
#        B: 80 to 89
#        C: 70 to 79
#        D: 60 to 69
#        F: Below 60

    print(f"Name: {name}")
    print(f"Average: {grades_sum}")

print(student_averages)
print(f"Class average: {class_average/len(student_averages)}")
print(f"Student letter grades: {student_letter_grades}")
