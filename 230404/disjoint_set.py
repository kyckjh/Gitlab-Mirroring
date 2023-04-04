def make_set():
    return [x for x in range(11)]
def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])
def union(x, y):
    p[find_set(y)] = find_set(x)

p = make_set()
union()