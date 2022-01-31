def are_coprime(n,m):
    set1, set2 = set(), set()
    for i in range(1, n+1):
        if (n % i == 0):
            set1.add(i)
    print(set1)
    for i in range(1, m+1):
        if (m % i == 0):
            set2.add(i)
    print(set2)
    return set1.intersection(set2) == {1}
        
        
print(are_coprime(34, 17))

help(set)

help>set