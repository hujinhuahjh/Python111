# def square_sum(numbers):
#     sums = 0
#     for number in numbers: 
#         sums += number*number
#     return sums

def square_sum(numbers):
    return sum([x ** 2 for x in numbers])

print(square_sum([0, 3, 4, 5]))