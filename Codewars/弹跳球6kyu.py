def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        times = 0
        while window < h:
            h = h * bounce
            if window < h:
                times+=2
            else:
                times+=1
                break
        return times
    else:
        return -1
    
print(bouncing_ball(30, 0.75, 1.5))