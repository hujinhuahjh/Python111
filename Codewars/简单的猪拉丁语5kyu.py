# def pig_it(text):
#     words = text.split()
#     l = []
#     for i,word in enumerate(words):
#         for index in range(2, len(word)+1):
#             l.append(word[index - 1])
#         l.append(word[0])
#         if i != len(words) - 1 and word.isalpha():
#             l.append('ay ')
#     str = l[-1]
#     if str[0].isalpha():
#          l.append('ay')
#     return "".join(x for x in l)

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

print(pig_it('Pig , latin is cool'))