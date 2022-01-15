def matrix():
    matrix = []
    rows, cols = 2, 5
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(i)
        matrix.append(col)
    return matrix

print(matrix())
    
        
    