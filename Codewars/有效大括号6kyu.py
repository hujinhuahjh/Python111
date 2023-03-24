def valid_braces(string):
    x = len(string)
    if x % 2 != 0:
        return False
    l = []
    for j in string:
        if j in ['(', '[', '{']:
            l.append(j)
        else:
            if len(l) != 0:
                if l[-1] == '(' and j == ')':
                    del l[-1]
                elif l[-1] == '[' and j == ']':
                    del l[-1]
                elif l[-1] == '{' and j == '}':
                    del l[-1]
                else:
                    return False
            else:
                return False
    return len(l) == 0

print(valid_braces("(){[]}()"))
