def descending_order(num):
    # l = list(str(num))
    # l.sort(reverse=True)
    # return int("".join([str(x)for x in l]))
    return int("".join(sorted(str(num), reverse=True)))

print(descending_order(564567))