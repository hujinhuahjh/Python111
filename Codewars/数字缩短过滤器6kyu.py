def shorten_number(suffixes, base):
    def shorten(suffix):
        if not isinstance(suffix, str) or not suffix.isdigit():
            return str(suffix)
        l = len(suffixes)
        x = int(suffix)
        for i in range(l, 0, -1):
            y = (base ** (i-1))
            if x >= y:
                z = int(x / y)
                return f"{z}{suffixes[i-1]}"
        return str(suffix)
    return shorten
    
# def shorten_number(suffixes, base):
#     def filter(shuru):
#         if isinstance(shuru,list):
#             return f"{shuru}"
#         elif shuru.isdigit():
#             pd=base
#             if int(shuru)<base:
#                 return f"{shuru}{suffixes[0]}"
#             else:
#                 pd=0
#                 lunhui=1
#                 huituiquyu=0
#                 jilu=0
#                 x=int(shuru)
#                 for i in range(1,100):
#                     pd=base**i
#                     huituiquyu=int(x/(base**(i-1)))
#                     lunhui=int(x/pd)
#                     if i==len(suffixes) or lunhui==0:
#                         jilu=i
#                         break
#                 c=jilu-1
#                 return f"{huituiquyu}{suffixes[c]}"
#         else:
#             return shuru
#     return filter

filter1 = shorten_number(['','k','m'],1000)
filter2 = shorten_number(['','KB','MB','GB'],1024)
print((filter1('98234324')))
print(filter2('1073741823'))