def is_triangular(t):
    for i in range (1, t//2 + 2):
        if (i*i + i == t*2):
            return True
    return False
        
    




print(is_triangular(100000000000))
