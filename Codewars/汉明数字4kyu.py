def hamming(n):
    a,b,c = 0,0,0
    r = [1]
    for i in range(1, n):
        x = r[a] * 2
        y = r[b] * 3
        z = r[c] * 5
        m = min(x, y, z)
        r.append(m)
        if m == x:
            a += 1
        if m == y:
            b += 1
        if m == z:
            c += 1
    return r[-1]
    
print(hamming(15))