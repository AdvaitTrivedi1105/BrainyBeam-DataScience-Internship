def student():
    s = int(input("How many students:"))
    student_name(s)

def student_name(s):
    for i in range(s):
        name = input("Enter name:")
        names.append(name)
        subjects()

def subjects():
    s = int(input("How many subjects:"))
    get_marks(s)

def get_marks(s):
    t = 0
    for i in range(s):
        mark = int(input("Enter marks:"))
        t+=mark
    marks.append(t)
    print(f"Total: {t}")

names = []
marks = []
student()
print(names)
print(marks)