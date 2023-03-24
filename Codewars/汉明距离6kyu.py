def hamming(a,b):
  # Implement me! 
  x,y,z = 0,0,0
  for index1,a_1 in enumerate(a):
    for index2,b_1 in enumerate(b):
        if(index1 == index2 and a_1 != b_1):
            z+=1
  return z

# def hamming(a,b):
#     z=0
#     i=0
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             z+=1
#     return z
  
print(hamming("111","121"))