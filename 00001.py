# import sys


# for p in sys.path:
#     print(p)

# import random
# import math
# import statistics

# die = [1, 2, 3, 4, 5, 6]
# l = []
# for i in range(50):
#     a = random.choice(die)
#     l.append(a)
# print(sum(l)/50)

# import os
# print(os.getcwd())
# print(os.__file__)
# print(math.__file__)

    
# import secrets
# list = ['ahoj', 'vecere', 'queen']
# print(secrets.choice(list))
 
# num = 10
# print(num)
# print(type(num)) 
# print(dir(num))

# print(help(int.denominator))



# print(dir(int))

# a = 8
# print(a.to_bytes(4, 'little'))

list = [3, 2, 1, 5, 6, 7, 8]
a = list[:3]
a.reverse()
a.extend(list[3:])
print(a)
