def single_digit(n):
    num = sum(list(map(int, list(bin(n)[2:]))))
    return num if num < 10 else single_digit(num)



      
if __name__ == '__main__':
    assert single_digit(15) == 4, "Should be 4"
    assert single_digit(157) == 5, "Should be 5"