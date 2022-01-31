
data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]

def itemgetter(item):
    return item['name']
    
def get_names(data):
    return list(map(itemgetter, data))



print(get_names(data))
