def recoverSecret(triplets):
        l,l1,l2 = [],[],[]
        i = 0
        while triplets:
            i = int(len(l))
            for triplet in triplets:
                l1.append(triplet[0])
                l2.append(triplet[1])
                l2.append(triplet[2])
            for m in l1:
                if m not in l2:
                    l.append(m)
                    break
            l1,l2 = [],[]
            if i == int(len(l)):
                break
            for t in triplets:
                if l[-1] == t[0]:
                    t.pop(0)
                    t.append(0)
        return ''.join(x for x in l)
    
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))