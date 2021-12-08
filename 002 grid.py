def grid(N):
    if N < 0:
        return None
    j,k = 0,0
    output = ''
    while k < N:
        i = k
        for i in range(i, N + i):
            j = i
            if i >= 26:
                j =  j - 26 * (i // 26)
            output += (chr(j+97)+ ' ')
        output = output[:len(output)-1]
        output += '\n'
        k += 1
    return output[:len(output)-1]
        
        
N = 0
print(grid(N))

