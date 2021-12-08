def is_valid_walk(walk):
    w = {'n': 0, 's': 0, 'w': 0, 'e': 0}
    for dir in walk:
        w[dir] += 1
    if sum(w.values()) == 10 and w['n'] - w['s'] == 0 and w['e'] - w['w'] == 0:
        return True
    return False    

def is_valid_walk_better(walk):
    return (len(walk) == 10 and walk.count('s') == walk.count('n') and walk.count('e') == walk.count('w'))




walk1 = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'e', 's']
walk = ['n','s','n','s','n','s','n','s','n','s']
print(is_valid_walk(walk1))