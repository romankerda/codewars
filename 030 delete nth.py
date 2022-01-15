# def delete_nth(order,max_e):
#     result = []
#     for i in range(len(order)):
#         if order[:i + 1].count(order[i]) <= max_e:
#             result.append(order[i])
#     return result

def delete_nth(order,max_e):
    result = []
    for num in order:
        if result.count(num) < max_e:
            result.append(num)
    return result

  
    

    
print(delete_nth([20,37,20,21], 1))