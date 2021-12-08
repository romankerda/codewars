def single_digit(n):
    num = sum(list(map(int, list(bin(n)[2:]))))
    print(num)
    return num if num < 10 else single_digit(num)


    
    
        
print(single_digit(524287))