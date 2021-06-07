#起始：随机数0-50，有200金币，每猜错一次，减去20金币，一直扣完为止。连续10次没猜中，系统锁定。猜中加30。
import random
num=random.randint(0,50)
i=1
x=500
while i <=10 and x>=20:
    number=input("请输入您要猜的数：")
    number = int(number)
    if number > num:
        print("您输入的数值偏大！")
        x=x-20
        i=i+1
    elif number < num:
        print("您输入的数值偏小！")
        x=x-20
        i=i+1
    else:
        print("恭喜猜中！本次数字为：",num)
        x=x+30
        break
if i>10:
    print("本次次数用完，系统已锁定")
if x<20:
    print("金币不足")
