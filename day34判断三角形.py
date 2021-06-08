print("从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）")
a=input("请输入第一条边的边长：")
a=int(a)
b=input("请输入第二条边的边长：")
b=int(b)
c=input("请输入第三条边的边长：")
c=int(c)
a>0
b>0
c>0
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("该三边可组成等边三角形")
    elif a==b or a==c or b==c:
        print("该三边可组成等腰三角形")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("该三边可组成直角三角形")
    else:
        print("该三边仅可组成普通三角形")
else:
    print("该三边不能组成三角形")



