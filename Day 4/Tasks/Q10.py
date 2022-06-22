# Q-10  Use of external and inbuilt library

import numpy as np
import random

def get_rows():
    rows = int(input("Enter number of row: "))
    return rows

# Main - Driver code
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(array)
rows = get_rows()
cols = (len(array)+1)//rows
array = array.reshape(rows,cols)
print(array)