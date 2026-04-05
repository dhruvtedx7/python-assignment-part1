# Task 1: Cleaning student data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
for student in raw_students:
    print(student)

for student in raw_students:
    
    # Step 1: clean name
    name = student["name"].strip()
    name = name.title()
    
    # Step 2: convert roll number
    roll = int(student["roll"])
    
    # Step 3: convert marks string to list
    marks_str = student["marks_str"]
    marks_list = marks_str.split(", ")
    
    marks = []
    for m in marks_list:
        marks.append(int(m))
    
    print("Cleaned Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)

# Step 4: validate name
words = name.split()

is_valid = True

for w in words:
    if not w.isalpha():
        is_valid = False
        
# Step 5: formatted output
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

if roll == 103:
    print(name.upper())
    print(name.lower())
