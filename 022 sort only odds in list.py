def sort_array(source_array):
    even_nums = []
    for num in source_array:
        if num % 2 == 1:
            even_nums.append(num)
    even_nums.sort()
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = even_nums.pop(0)
    return source_array
            
print(sort_array([5, 3, 2, 8, 1, 4]))