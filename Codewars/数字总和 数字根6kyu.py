def digital_root(n):
    # n = str(n)
    # while len(n) > 1:
    #     sums = 0
    #     for i in range(len(n)):
    #         sums += int(n[i])
    #     n = str(sums)
    # return int(n)
    if n > 9:
        return n % 9
    else:
        return n

print(digital_root(493193))