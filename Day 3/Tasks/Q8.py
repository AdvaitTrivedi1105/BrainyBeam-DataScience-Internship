# Q-8  List 5 inbuilt libraries of python with example using 3 methods

"""
OS:-
1) getcwd
2) mkdir
3) rmdir

time:-
1) sleep
2) strftime
3) ctime

random:-
1) random
2) randint
3) shuffle

itertools:-
1) chain
2) product
3) permutations

math:-
1) sqrt
2) pow
3) floor
"""

import os
import time
import random
import itertools
import math

# OS
print(os.getcwd())
os.mkdir("new-folder")
os.rmdir("new-folder")

# time
print(time.ctime())
time.sleep(1)
print(time.strftime("%a, %d %b %Y %H:%M:%S"))

# random
a = [1,2,3,4,5]
print(random.random())
print(random.randint(1,9))
random.shuffle(a)
print(a)

# itertools
b = [1,2]
c = [2,3,4]
chain = itertools.chain(b,c)
for i in chain:
    print(i)
product = itertools.product(b,c)
for i in product:
    print(i)
combinations = itertools.permutations(c,2)
for i,j in combinations:
    print(i,j)

# math:-
print(math.sqrt(81))
print(math.pow(2,3))
print(math.floor(3.7))