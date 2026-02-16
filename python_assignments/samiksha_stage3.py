name = input("Enter student name: ")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("{name}\nTotal: {total}/300\nPercentage: {percentage}%\nGrade: {grade}")