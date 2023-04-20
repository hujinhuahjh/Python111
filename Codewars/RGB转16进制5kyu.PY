def rgb(r, g, b):
    dic = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 
           10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    l = []
    for i in (r, g, b):
        if i < 0:
            i = 0
        if i > 255:
            i = 255
        l.append(dic[int(i / 16)])
        i = i % 16
        l.append(dic[i])
    return ''.join(l)
    
print(rgb(234,255,0))