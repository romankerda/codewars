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

# list = [3, 2, 1, 5, 6, 7, 8]
# a = list[:3]
# a.reverse()
# a.extend(list[3:])
# print(a)

# list = [True] * 1001
# count = 0
# for i in range (2, 1001):
#     if list[i]:
#         print(i)
#         count += 1
#     for j in range(i*i, 1001, i):
#         list[j] = False
# print(f'count = {count}')


# def function(*args, **kwargs):
#     print(args)
#     print(kwargs)

# function('a', 1, b='b', c=1)

# args = ['a', 'b', 'c']
# kwargs = {'name':'joe', 'age':25}
# function(*args, **kwargs)

# import os
# print(os.getcwd())
# print(help(os))

# import datetime

# a = datetime.datetime.now()
# b = datetime.datetime.today()
# print(a)
# print(b)

# print(datetime.__file__)

# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list3 = range(20)
# print(list(zip(list1, list2, list3)))

# def fib():
#     a,b = 0,1
#     for i in range (0, 10):
#         print(a)
#         a,b = b, a + b

# print(fib())

# my_dict = {'name': 'Roman', 'surname': 'Kerda', 'age': 46}
# for key, value in my_dict.items():
#     print(f'My {key} is {value}.')

# my_set = {1, 2, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9}
# for i in my_set:
#     print(i)
# print(len(my_set))

my_list = [1,2,4]
squares = [i*i for i in my_list]
print(squares)

