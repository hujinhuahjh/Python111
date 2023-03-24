def create_dict(keys, values):
    d = {}
    if not values:
        for x in keys:
            d[x] = None
    for i,x in enumerate(keys):
        for j,y in enumerate(values):
            if (i == j):
                d[x] = y
                continue
            elif (i > j):
                d[x] = None
                continue
            else:
                break
    return d
    
print(create_dict(['a', 'b', 'c', 'd'], [1, 2, 3]))