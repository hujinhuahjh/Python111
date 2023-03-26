def get_count(sentence):
    i = sentence.count('a')
    j = sentence.count('e')
    k = sentence.count('i')
    l = sentence.count('o')
    m = sentence.count('u')
    return i + j + k + l + m

print(get_count("aeiouasafgvbfdb"))