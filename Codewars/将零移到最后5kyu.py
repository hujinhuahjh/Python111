def move_zeros(lst):
    l = len(lst)
    i,j = 0,0
    while i < l:
        if lst[i] == 0:
            lst.pop(i)
            lst.append(0)
            i -= 1
        j += 1
        if j == l:
            break
        i += 1
    return lst


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))