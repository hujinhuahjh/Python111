def alphabet_position(text):
    l = list(text.lower())
    new = []
    for x in l:
        if x.isalpha():
#         if ord(x) >= 97 and ord(x) <= 122:
            new.append(str(ord(x) - 96))
    return ' '.join(y for y in new)

print(alphabet_position("The sunset sets at twelve o' clock."))