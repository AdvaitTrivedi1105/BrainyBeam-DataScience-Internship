a=['y','y','y','y','n','y','n']
total = 0
for i in range(len(a)):
    if a[i]=='y':
        total+=1
        print('Index:',i+1)
print(f"Total: {total}")