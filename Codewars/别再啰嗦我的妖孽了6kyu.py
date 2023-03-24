# def spin_words(sentence):
#     l = list(sentence)
#     y = []
#     a = 0
#     if " " in l:
#         for index,x in enumerate(l):
#             if x == ' ':
#                 y.append(int(index + 1))
#         for z in range(len(y)-1):
#             a = y[z+1] - y[z]
#             if a >= 6:
#                 li = l[y[z] : y[z+1]-1]
#                 li.reverse()
#                 l[y[z] : y[z+1]-1] = li
#         if len(l) - y[-1] >= 5:
#             lis = l[y[-1]:]
#             lis.reverse()
#             l[y[-1]:] = lis
#         if y[0] >= 6:
#             liss = l[:y[0]-1]
#             liss.reverse()
#             l[:y[0]-1] = liss
#     else:
#         if len(l) >= 5:
#             l.reverse()
#     return ''.join(b for b in l)
    
def spin_words(sentence): 
    l = sentence.split()
    li = []
    for word in l:
        if len(word) >= 5:
            li.append(word[::-1])
        else:
            li.append(word)
    return ' '.join(x for x in li)
            
print(spin_words("CodeWars"))
print(spin_words("Welcome"))
print(spin_words("function when the more and a the more five letter all words only the in in more string than letters letters"))