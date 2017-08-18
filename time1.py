def ftime():
    import time 
    z = time.localtime(time.time())
    z = time.strftime("%H:%M %S", z)
    return z

