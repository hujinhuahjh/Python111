import itertools

def next_smaller(n):
    # l = [int(x) for x in str(n)]
    # ls = sorted(l)
    # if l == ls: 
    #     return -1
    # all_l = list(itertools.permutations(ls))
    # j = all_l.index(tuple(l))
    # if all_l[j - 1][0] == 0:
    #     return -1 
    # return int(''.join(str(x) for x in all_l[j - 1]))
        
    digits = list(str(n))

    i = len(digits) - 2
    while i >= 0 and digits[i] <= digits[i+1]:
        i -= 1

    if i < 0:
        return -1

    j = i + 1
    while j < len(digits) and digits[j] < digits[i]:
        j += 1
    j -= 1
    
    print(digits)
    digits[i], digits[j] = digits[j], digits[i]
    digits[i+1:] = reversed(digits[i+1:])
    result = int(''.join(digits))

    if len(str(result)) != len(str(n)):
        return -1
    return result

    
print(next_smaller(17128))
    
    