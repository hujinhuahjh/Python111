def find_outlier(integers):
    j,o = 0,0
    for i in integers:
        if i % 2 == 0:
            o+=1
        else:
            j+=1
        if o == 2:
            for ii in integers:
                if ii % 2 != 0:
                    return ii
        if j == 2:
            for ii in integers:
                if ii % 2 == 0:
                    return ii
    return None

print(find_outlier([2, 4, 6, 8, 10, 3]))