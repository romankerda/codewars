def queue_time(customers, n):
    tills = [0]*n
    for c in customers:
        tills[tills.index(min(tills))] += c
    return max(tills)
    
    


print(queue_time([10, 2, 3], 2))