def unique_in_order(sequence):
    length = len(sequence)
    index = 2
    while(length-1>0):
        if sequence[index-2] == sequence[index-1]: 
            sequence = sequence[:index-1] + sequence[index:]
        else:
            index+=1
        length-=1
    return list(sequence)

print(unique_in_order(()))