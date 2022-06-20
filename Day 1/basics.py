# LISTS
a = ['hello','how','are','you']
print(a[:-3:-1])
# ['you','are']      -> [start:stop:jump]
print(a[-2:-4:-1])
# ['are','how']

# SETS
a = {1,2,3,4,5,5,4}
b = {4,5,6,7,8}
print(a&b)     #intersection
# {4, 5}
print(a|b)     #union
# {1, 2, 3, 4, 5, 6, 7, 8}

# DICTIONARY
a = {'x':45, 'sem':{'A':30,'B':40},'z':['a','b']}
a['h'] = 1   # 'h':1 will be added to dict
