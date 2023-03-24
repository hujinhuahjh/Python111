def zero(f = None): 
    if f:
        return f(0)
    else:
        return 0

def one(f = None):  
    if f:
        return f(1)
    else:
        return 1

def two(f = None):  
    if f:
        return f(2)
    else:
        return 2

def three(f = None):  
    if f:
        return f(3)
    else:
        return 3

def four(f = None):  
    if f:
        return f(4)
    else:
        return 4

def five(f = None):  
    if f:
        return f(5)
    else:
        return 5

def six(f = None):  
    if f:
        return f(6)
    else:
        return 6

def seven(f = None):  
    if f:
        return f(7)
    else:
        return 7

def eight(f = None):  
    if f:
        return f(8)
    else:
        return 8

def nine(f = None):  
    if f:
        return f(9)
    else:
        return 9


def plus(y): 
    return lambda x: x+y

def minus(y): 
    return lambda x: x-y

def times(y): 
    return lambda x: x*y

def divided_by(y): 
    return lambda x: int(x/y)

print(seven(times(five())))

