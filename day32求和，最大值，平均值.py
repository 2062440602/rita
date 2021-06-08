print("从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。")
i=1
sum=0
num = input("请输入数字：")
while i<11:
    sum = sum + int(num)
    i=i+1
    num = int(num)+1
max=num-1
ave=sum/10
print("和：",sum)
print("最大的数：",max)
print("平均数：",ave)