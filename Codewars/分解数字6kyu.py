def decompose(num):
    num1 = num
    x = 1
    z = 0
    result = []
    while(num1 > x+1):
        x += 1
        z = 0
        num = num1
        while num > 1:
            num = int(num / x)
            if num >= 1:
                z += 1
        if z > 1:
            result.append(z)
        else:
            break
        num1 = num1 - x ** z
    return [result, num1]
    
print(decompose(25))