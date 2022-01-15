def digital_root(n):
    digits = []
    exp = len(str(n))
    for i in reversed(range(exp)):
        digits.append(int(n / 10**i))
        n = n % 10**i
    if sum(digits) > 9:
        return digital_root(sum(digits))
    else:
        return sum(digits)
    
def root2(n):
    return n if n < 9 else root2(sum(map(int, str(n))))



print(root2(165))
    

        