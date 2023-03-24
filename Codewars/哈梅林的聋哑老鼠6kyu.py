def count_deaf_rats(town):
    s = town.replace(' ', '')
    l = s.index('P')
    i = 0
    sums = 0
    while i < l:
        if s[i:i+2] != '~O':
            sums += 1
        i += 2
    i += 1
    while i > l and i < len(s):
        if s[i:i+2] != 'O~':
            sums += 1
        i += 2
    return sums

print(count_deaf_rats("~O~O~O~O P"))