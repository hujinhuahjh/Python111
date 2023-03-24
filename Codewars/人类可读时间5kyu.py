def make_readable(seconds):
    # l = []
    # if seconds < 3600:
    #     l.append('00:')
    # if seconds < 60:
    #     l.append('00:')
    # if seconds == 0:
    #     l.append('00')
    # while seconds != 0:
    #     if seconds >= 3600:
    #         i = int(seconds / 3600)
    #         if i > 9:
    #             l.append(str(i))
    #         else:
    #             l.append('0')
    #             l.append(str(i))
    #         seconds = seconds % 3600
    #         if seconds < 3600:
    #             l.append(':')
    #         if seconds == 0:
    #             l.append('00:')
    #     if seconds >= 60:
    #         j = int(seconds / 60)
    #         if j > 9:
    #             l.append(str(j))
    #         else:
    #             l.append('0')
    #             l.append(str(j))
    #         seconds = seconds % 60
    #         if seconds < 60:
    #             l.append(':')
    #     if seconds < 60 and seconds >= 0:
    #         k = int(seconds)
    #         if k > 9:
    #             l.append(str(k))
    #         else:
    #             l.append('0')
    #             l.append(str(k))
    #         seconds = 0
    # return "".join(x for x in l)
    return f'{seconds//3600:02d}:{seconds%3600//60:02d}:{seconds%3600%60:02d}'
print(make_readable(234530))
            