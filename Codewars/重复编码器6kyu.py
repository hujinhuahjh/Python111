def duplicate_encode(word):
    word = word.lower()
    words = ''
    for i in word:
        if word.count(i) > 1:
            words+=')'
        else:
            words+='('
    return words

print(duplicate_encode('Wt@e@KrxnQ!VqbCX!Xb C))AoBkIDZ@IBYy(s@'))