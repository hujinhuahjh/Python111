def friend(x):
    new = []
    for y in x:
        if len(y) == 4:
            new.append(y)
    return new

print(friend(["Ryan", "Kieran", "Mark",]))