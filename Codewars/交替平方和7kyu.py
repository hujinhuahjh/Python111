# def alternate_sq_sum(arr):
#     sums = 0
#     for index,x in enumerate(arr):
#         if(index % 2 != 0):
#             sums += x ** 2
#         else:
#             sums += x
#     return 

# def alternate_sq_sum(arr):
#     sums = 0
#     index = 0
#     for index in range(len(arr)):
#         if(index % 2 != 0):
#             sums += arr[index] ** 2
#         else:
#             sums += arr[index]
#         index+=1
#     return sums

def alternate_sq_sum(arr):
    return sum([x ** 2 if index % 2 != 0 else x for index,x in enumerate(arr)])

print(alternate_sq_sum([11, 12, 13, 14, 15]))