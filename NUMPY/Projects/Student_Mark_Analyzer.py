'''
Build a system that stores marks of students in different subjects and gives insights like:

Student-wise and subject-wise averages

Top scorers in each subject

Subject in which a student scored the best

Class topper
'''

import numpy as np

# Rows = students, Columns = subjects (Math, Science, English, History)
marks = np.array([
    [85, 92, 78, 90],   # Student 1
    [76, 88, 85, 83],   # Student 2
    [90, 91, 92, 89],   # Student 3
    [69, 72, 65, 70],   # Student 4
    [88, 85, 80, 87]    # Student 5
])

student_names = ["Alice", "Bob", "Charlie", "David", "Eva"]
subject_names = ["Math", "Science", "English", "History"]

#Print Overall Average Marks
print("Overall average mark of class: ",np.mean(marks))

#Subject-Wise Averages
for i in range(len(subject_names)):
    avg=np.mean(marks[:,i])
    print(f"Average of subject {subject_names[i]} is {avg}")

#Student-Wise Averages
for i in range(len(student_names)):
    avg = np.mean(marks[i,:])
    print(f"Average marks of {student_names[i]} is {avg}")

#Topper of each subject
for i in range(len(subject_names)):
    toper = np.argmax(marks[:,i])
    print(f"Topper of the subject {subject_names[i]} is {student_names[toper]}")

#Best of each student
for i in range(len(student_names)):
    best = np.argmax(marks[i,:])
    print(f"{student_names[i]} is best in {subject_names[best]}")

#Class Topper (Overall Total)
total_scores = np.sum(marks, axis=1)
topper_index = np.argmax(total_scores)
print(f"\n🎓 Class Topper: {student_names[topper_index]} with total {total_scores[topper_index]} marks")

