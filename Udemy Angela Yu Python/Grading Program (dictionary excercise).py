student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key, value in student_scores.items(): #iterates through the dictionary
    if value < 100:
        student_grades[key] = "Outstanding" #adds current key and new value in the dict with this to the empty string, student_grades.
    if value < 90:
        student_grades[key] = "Exceeds Expectations"
    if value < 80:
        student_grades[key] = "Acceptable"
    if value < 70:
        student_grades[key] = "Fail"

print(student_grades)

for key in student_grades:
    print(f"{key}'s grade: {student_grades[key]}") #access the value of the current the key.