# Q-5  Student report card that takes subject, marks as input & return marks of student using functions

def get_students():
    n = int(input("Enter how many students: "))
    return n

def get_name():
    name = input("Enter name: ")
    return name

def get_subjects():
    n = int(input("How many subjects: "))
    return n

def get_marks(n):
    total = 0
    for i in range(n):
        marks = int(input(f"Enter marks for subject {i+1}: "))
        total += marks
    return total


# Main - Driver Code
report_card = {}
num_of_students = get_students()

for i in range(num_of_students):
    name = get_name()
    num_of_subjects = get_subjects()
    marks = get_marks(num_of_subjects)
    report_card[name] = marks

for i,j in report_card.items():
    print(f"\n{i} : {j}")