def disemvowel(string_):
    for l in string_:
        if l in 'aeiouAEIOU':
            string_ = string_.replace(l, '')
    return string_

print(disemvowel("This website is for losers LOL!"))