print("一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。")
dec=0     #每天爬1米
i=0       #爬的天数
while dec<20:
    dec=dec+3
    i=i+1
    if dec<20:
        dec=dec-2
    else:
        print(i)
