a = ['hello','','how','are','you',None]
for i in a:
    if(type(i)!=str or len(i)<2):
        continue
    else:
        print(i[1])