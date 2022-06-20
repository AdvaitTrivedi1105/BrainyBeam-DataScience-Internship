a=['a','b','v',3,7,9,0]
s=[]
i=[]
for i in a:
    if type(i) == str:
        s.append(i)
    else:
        i.append(i)
print(a)
print(s)
print(i)