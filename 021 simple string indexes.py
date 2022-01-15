def solve(st, idx):
    short = st[idx:]
    count = 0
    for i in range(len(short)):
        if short[i] == '(': 
            count += 1
        if (short[i] == ')' and count > 0):
            count -= 1
        if count == 0:
            if i == 0:
                return -1
            return i + idx
    return -1
        



print((solve("(())23(45))(aB)",2)))
