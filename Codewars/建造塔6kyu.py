def tower_builder(n_floors):
    l = []
    s = '*'
    for i in range(n_floors):
        while i > 0:
            s+='**'
            i-=1
        l.append(s.center(n_floors * 2 - 1))
        s = '*'
    return l

print(tower_builder(3))