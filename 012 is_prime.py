def is_prime(num):
    if num < 2:  
        return False
    if num == 2: 
        return True
    else:
        for i in range(3, num, 2):
            if num % i == 0:
                return False
        return True



print(is_prime(10))