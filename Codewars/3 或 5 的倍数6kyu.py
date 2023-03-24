def solution(number):
    if number < 3:
        return 0
    sums = 0
    while number > 2:
        number-=1
        if number % 3 == 0 or number % 5 == 0:
            sums += number
    return sums

print(solution(6))