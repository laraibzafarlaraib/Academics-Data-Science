import random

# Declare a list of 30 elements and initialize them randomly
marks_list = [random.randint(1, 100) for _ in range(30)]

# Print the original marks in a single line
print("Original marks: ", end="")
for mark in marks_list:
    print(mark, end=" ")
print()

# Count the number of pass students and calculate the sum of their marks
num_pass = 0
pass_sum = 0
for mark in marks_list:
    if mark >= 50:
        num_pass += 1
        pass_sum += mark

# Calculate and print the average of pass students
if num_pass > 0:
    pass_avg = pass_sum / num_pass
    print(f"Pass average: {pass_avg:.2f}")

# Print the marks of fail students in a single line
print("Fail marks: ", end="")
for mark in marks_list:
    if mark < 50:
        print(mark, end=" ")
print()

# Print the marks of students with above average in a single line
if num_pass > 0:
    above_avg_marks = [mark for mark in marks_list if mark > pass_avg]
    print("Above average marks: ", end="")
    for mark in above_avg_marks:
        print(mark, end=" ")
    print()

# Print the marks of students with below average in a single line
if num_pass > 0:
    below_avg_marks = [mark for mark in marks_list if mark < pass_avg]
    print("Below average marks: ", end="")
    for mark in below_avg_marks:
        print(mark, end=" ")
    print()
