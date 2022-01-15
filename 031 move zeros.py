def move_zeros(array):
    result, idx = [], 0
    for num in array:
        if num == 0:
            result.append(num)
        else: 
            result.insert(idx, num)
            idx += 1
    return result





print(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))