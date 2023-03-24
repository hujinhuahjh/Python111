from math import sqrt

def nearest_sq(n):
    # i = int(sqrt(n))
    # x = i*i
    # y = (i+1) ** 2
    # if abs(x - n) > abs(y - n):
    #     return y
    # else:
    #     return x
    
    return round(n ** 0.5) ** 2
print(nearest_sq(111))