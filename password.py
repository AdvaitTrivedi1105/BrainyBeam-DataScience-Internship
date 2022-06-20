import random
small = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym = "!@$%^&*()_"
num = "0123456789"
all = small + caps + num + sym
i = int(input("Enter length:"))
if(i<3):
    print("invalid length")
else:
    print("".join(random.sample(all,i)))