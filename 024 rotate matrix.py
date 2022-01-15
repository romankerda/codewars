def rotate(matrix): 
    rows, cols = len(matrix[0]), len(matrix)
    rot_matrix = []
    for i in range(rows):
        col = []
        for j in range(cols):
            if False: #direction == 'clockwise':
                col.append(matrix[cols-1-j][i])
            else:
                col.append(matrix[j][rows-1-i])
        rot_matrix.append(col)
    return rot_matrix

matrix = [[1, 2],
          [4, 5],
          [7, 8]]

print(rotate(matrix))
    
            
            
    


rotate([[1,2,3],[4,5,6],[7,8,9]])