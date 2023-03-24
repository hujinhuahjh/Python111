def get_sum(a,b):
    sums = 0
    if a > b:
        t = a
        a = b
        b = t
    for x in range(a, b+1):
        sums+=x
    return sums

print(get_sum(2, 2))