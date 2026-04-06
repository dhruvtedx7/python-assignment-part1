raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"}
]

for student in raw_students:

    name = student["name"].strip()
    name = name.title()

    roll = int(student["roll"])

    marks_list = student["marks_str"].split(", ")
    marks = []

    for m in marks_list:
        marks.append(int(m))

    # validation INSIDE loop
    words = name.split()
    is_valid = True

    for w in words:
        if not w.isalpha():
            is_valid = False

    if is_valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")

    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

    if roll == 103:
        print(name.upper())
        print(name.lower())

# =========================
# Task 2: Marks Analysis

print("\n--- Task 2 Output ---\n")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# loop + grade together
for i in range(len(subjects)):

    subject = subjects[i]
    mark = marks[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subject, ":", mark, "-", grade)

# total + average
total = sum(marks)
average = total / len(marks)

print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))

# highest + lowest
highest = marks[0]
lowest = marks[0]

high_subject = subjects[0]
low_subject = subjects[0]

for i in range(len(marks)):

    if marks[i] > highest:
        highest = marks[i]
        high_subject = subjects[i]

    if marks[i] < lowest:
        lowest = marks[i]
        low_subject = subjects[i]

print("Highest:", high_subject, highest)
print("Lowest:", low_subject, lowest)

# simple addition (no input confusion)
subjects.append("Biology")
marks.append(85)

subjects.append("History")
marks.append(90)

print("\nNew subjects added: 2")

new_total = sum(marks)
new_avg = new_total / len(marks)

print("Updated Average:", round(new_avg, 2))

# Task 3: Class PErformance
print("\n--- Task 3 Output ---\n")

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85])
]

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0

total_avg = 0

for student in class_data:

    name = student[0]
    marks = student[1]

    avg = sum(marks) / len(marks)
    total_avg += avg

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    print(name, "|", round(avg, 2), "|", status)

print("\nPass:", pass_count)
print("Fail:", fail_count)

print("Topper:", topper_name, "-", round(topper_avg, 2))

class_avg = total_avg / len(class_data)
print("Class Average:", round(class_avg, 2))
