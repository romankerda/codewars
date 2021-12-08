def array_diff(a, b):
    return [n for n in a if n not in b]

def array_diff(a, b):
    output = []
    for i in a:
        if i not in b:
            output.append(i)
    return output
        






a = [1, 2, 3, 4, 5, 5, 6, 7]
b = [5, 2, 7]
print(array_diff(a, b))