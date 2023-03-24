def is_pangram(s):
    s = s.lower()
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in l:
        if i not in s:
            return False
    return True

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))