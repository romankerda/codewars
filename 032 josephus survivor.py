def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1


print((josephus_survivor(7,3)))


# a = [i for i in range(50)]
# for num in a[5::5]:
#     a.remove(num)
# print(a)
