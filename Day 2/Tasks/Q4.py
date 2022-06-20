# Q-4  5 methods of list, set and dictionary

"""
LIST:-
1) append
2) remove
3) index
4) insert
5) sort

SET:-
1) intersection
2) add
3) union
4) difference
5) remove

Dictionary:-
1) keys
2) get
3) values
4) items
5) clear
"""


# LIST

my_list = [1,2,4,7,6,3,9,5,8]
# [1, 2, 4, 7, 6, 3, 9, 5, 8]
my_list.append(0)
# [1, 2, 4, 7, 6, 3, 9, 5, 8, 0]
my_list.sort()
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.remove(3)
# [0, 1, 2, 4, 5, 6, 7, 8, 9]
my_list.index(4)
# 3
my_list.insert(3,3)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# SET

my_set = {1,2,3,4,3,2,1}
# {1, 2, 3, 4}
my_set2 = {2,7,4,5,4,3}
# {2, 3, 4, 5, 7}
my_set.intersection(my_set2)
# {2, 3, 4}
my_set2.add(1)
# {1, 2, 3, 4, 5, 7}
my_set2.remove(1)
# {2, 3, 4, 5, 7}
my_set.difference(my_set2)
# {1}
my_set.union(my_set2)
# {1, 2, 3, 4, 5, 7}


# DICTIONARY

my_dict = {
    "fruits" : ["apple","mango","banana","grapes"],
    "cars" : ["ferrari","tesla","lamborghini","buggati"],
    0 : [1,2,3,4,5]
}

my_dict.keys()
# dict_keys(['fruits', 'cars', 0])
my_dict.values()
# dict_values([['apple', 'mango', 'banana', 'grapes'], ['ferrari', 'tesla', 'lamborghini', 'buggati'], [1, 2, 3, 4, 5]])
my_dict.items()
# dict_items([('fruits', ['apple', 'mango', 'banana', 'grapes']), ('cars', ['ferrari', 'tesla', 'lamborghini', 'buggati']), (0, [1, 2, 3, 4, 5])])
my_dict.get("cars")
# ['ferrari', 'tesla', 'lamborghini', 'buggati']
my_dict.clear()
# {}