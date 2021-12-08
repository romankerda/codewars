#002 chr(), ord()
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


#003 map(fun, data)
data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]

def itemgetter(item):
    return item['name']
    
def get_names(data):
    return list(map(itemgetter, data))

#004 set1.intersection(set2), set.add()
def are_coprime(n,m):
    set1, set2 = set(), set()
    for i in range(1, n+1):
        if (n % i == 0):
            set1.add(i)
    print(set1)
    for i in range(1, m+1):
        if (m % i == 0):
            set2.add(i)
    print(set2)
    return set1.intersection(set2) == {1}

#005 bin()
def single_digit(n):
    num = sum(list(map(int, list(bin(n)[2:]))))
    print(num)
    return num if num < 10 else single_digit(num)

#007 list.index()
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def direction(facing, turn):
    return directions[(directions.index(facing) + turn // 45) % 8]

#008 return ... for .. in ..
def solution(s):
    return [(s+'_')[i:i+2] for i in range(0, len(s), 2)]

#009 join(), isalpha()
def alphabet_position(text):
    output = ''
    for ch in text.lower():
        if ch.isalpha():
            output += str(ord(ch.lower())-96) + ' '
    return output[:len(output)-1]

def alphabet_position2(text):
    return ' '.join(str(ord(ch) - 96) for ch in text.lower() if ch.isalpha())

#010 []*n, list.index(), min(list)
def queue_time(customers, n):
    tills = [0]*n
    for c in customers:
        tills[tills.index(min(tills))] += c
    return max(tills)

#011 return [.. for .. in .. if .. not in ..]
def array_diff(a, b):
    return [n for n in a if n not in b]

def array_diff(a, b):
    output = []
    for i in a:
        if i not in b:
            output.append(i)
    return output

#013 return True / False directly
def is_valid_walk(walk):
    w = {'n': 0, 's': 0, 'w': 0, 'e': 0}
    for dir in walk:
        w[dir] += 1
    if sum(w.values()) == 10 and w['n'] - w['s'] == 0 and w['e'] - w['w'] == 0:
        return True
    return False    

def is_valid_walk_better(walk):
    return (len(walk) == 10 and walk.count('s') == walk.count('n') and walk.count('e') == walk.count('w'))

#017 split(), capitalize()
def generate_hashtag2(s):
    output = '#'
    for word in s.split():
        output += word.capitalize()
    if len(output) > 140 or len(s) == 0:
        return False
    return str(output)



