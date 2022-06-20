student = int(input("Enter how many students:"))
names_list = []
marks_list = []
for i in range(student):
    t=0
    name=input("Enter Name:")
    names_list.append(name)
    sub=int(input("How many subjects:"))
    for j in range(sub):
        marks = int(input("Enter marks:"))
        t = t + marks
    marks_list.append(t)
    print(t)
print(names_list)
print(marks_list)