def 练习1_2_5():
    print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

def 练习1_2_6():
    famous_person = 'Albert Einstein'
    print(f"{famous_person} once said, “A person who never made a mistake never tried anything new.”")

def 练习1_2_7():
    famous_person = 'Albert Einstein'
    print(f" {''.join(famous_person.split())}  once\n\t said, “A person who never made a mistake never tried anything new.”")

def 练习1_3_4(): 
    l = ['aa', 'bb', 'cc']
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
     
def 练习1_3_5():
    l = ['aa', 'bb', 'cc']
    for p in l:
        print(f"{p},I want to invite you eat dinner together.\n")
    print(f"I'm sorry that {l.pop(1)} can't to eat dinner.")
    l.insert(1, 'dd')
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")

def 练习1_3_6():
    l = ['aa', 'bb', 'cc']
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print(f"I'm sorry that {l.pop(1)} can't to eat dinner.")
    l.insert(1, 'dd')
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print("\nI'll invite more people because I replace a bigger table.")
    l.insert(0, 'ee')
    a = int(len(l) / 2)
    l.insert(a, 'ff')
    l.append('gg')
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    
def 练习1_3_7():
    l = ['aa', 'bb', 'cc']
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print(f"I'm sorry that {l.pop(1)} can't to eat dinner.")
    l.insert(1, 'dd')
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print("\nI'll invite more people because I replace a bigger table.")
    l.insert(0, 'ee')
    a = int(len(l) / 2)
    l.insert(a, 'ff')
    l.append('gg')
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print("\nI'm sorry that I can only invite two people because the table.")
    while len(l) > 2:
        print(f"{l.pop()},I'm sorry that you can't eat.")
    while l:
        print(f"{l[0]},you still can eat.")
        del l[0]   
    print(l)
  
def 练习1_3_8():   
    p = ['aaa', 'eee', 'ddd', 'ccc', 'bbb']
    print(p)
    print(sorted(p))
    print(p)
    print(sorted(p, reverse=True))
    print(p)
    p.reverse()
    print(p)
    p.reverse()
    print(p)
    p.sort()
    print(p)
    p.sort(reverse=True)
    print(p)
    
def 练习1_3_9():
    # 练习1_3_6()
    l = ['aa', 'bb', 'cc']
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print(f"I'm sorry that {l.pop(1)} can't to eat dinner.")
    l.insert(1, 'dd')
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print("\nI'll invite more people because I replace a bigger table.")
    l.insert(0, 'ee')
    a = int(len(l) / 2)
    l.insert(a, 'ff')
    l.append('gg')
    for p in l:
        print(f"{p},I want to invite you eat dinner together.")
    print(f"I invite {len(l)} people.")
    
练习1_3_9()