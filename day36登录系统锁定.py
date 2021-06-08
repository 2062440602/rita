print("实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）")
print("请输入您的用户名：root")
password=input("请输入您的密码：")
i=1
if password==("admin"):
    print("登录成功")
while password!=("admin"):
    if i<3:
        password == input("密码错误，请重新输入：")
        i=i+1
    else:
        print("密码多次输入错误，系统已锁定")
        break

