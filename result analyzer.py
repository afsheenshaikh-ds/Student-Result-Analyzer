# Student Result Analyzer
# This program takes marks for 5 subjects and calculates total, percentage, and grade

# Get student details
name = input("Enter Student Name: ")
rollno = input("Enter Student Roll No: ")

# Get marks for 5 subjects
sub1 = float(input("Enter Subject 1 Marks: "))
sub2 = float(input("Enter Subject 2 Marks: "))
sub3 = float(input("Enter Subject 3 Marks: "))
sub4 = float(input("Enter Subject 4 Marks: "))
sub5 = float(input("Enter Subject 5 Marks: "))

# Calculate total
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
percentage = total / 5

# Assign grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

# Store marks in a list to find highest and lowest
marks = [sub1, sub2, sub3, sub4, sub5]

# Display the result
print("\n--- Student Result ---")
print("Name:", name)
print("Roll No:", rollno)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))