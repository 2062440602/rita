#给商城添加以下功能：
#1.进入商城时候，随机抽奖某个商品的优惠券。
#优惠券如下：
		#10张辣条优惠券：满600减300
		#20张Lenovo电脑优惠券：半折甩卖
#2.结算时，添加购物积分功能
#10元1个积分。

print("------------欢迎光临Rita商超！--------------")
print("\t编号\t\t\t\t名称\t\t\t价格/件\t\t\t")
names = (["联想电脑","华为手机","苹果手机","智能音箱","洗碗机器","卫龙辣条","华为手表","新式空调"])
price = ([6000,15000,8000,500,3000,10,1200,8500])
id=0
while id<8:
    print("\t",id,"\t\t\t",names[id],"\t\t",price[id],"\t\t\t")
    id=id+1
print("------------------------------------------")
shop=[
    ["联想电脑",6000],
    ["华为手机",15000],
    ["苹果手机",8000],
    ["智能音箱",500],
    ["洗碗机器",3000],
    ["卫龙辣条",100],
    ["华为手表",1200],
    ["新式空调",8500]
]
mycart = []

while True:
    salary =  input("请输入您的余额:")
    if salary.isdigit():
        salary = int(salary)
        if salary<=0:
            print("对不起，您的输入无效，请重新输入！")
        else:
            break
    else:
        print("对不起，您的输入无效，请重新输入！")

money=salary

while True:
    name = input("请输入您要的商品编号：")
    if name.isdigit():
        name = int(name)
        if name < len(shop):
            if salary >= shop[name][1]:
                mycart.append(shop[name])
                salary = salary - shop[name][1]
                print("恭喜，添加成功！您的余额还剩：￥",salary)
            else:
                print("穷鬼，钱不够，请选择其他商品！")
        elif name >=len(shop):
            print("您输入的商品编码不存在，请重新输入")
    elif name == 'q' or name == 'Q':
        print("欢迎下次光临，再见！")
        break
    else:
        print("对不起，您的输入有误，请重新输入！")


print("-------------------------------------------")
print("您的购物清单如下：")
for index,value in mycart:
    print(index,value)
aa=mycart.count(["联想电脑",6000])
bb=mycart.count(["卫龙辣条",100])
if aa>=1 and bb<6:
    print("其中您有联想电脑",aa,"台，","享受厂家单件五折优惠")
    salary=salary+3000*aa
    print("您的账户余额为：￥",salary)
if bb>=6 and aa<1:
    print("其中您有辣条",bb,"包，","享受厂家满",600,"减",300)
    salary=salary+300
    print("您的账户余额为：￥",salary)
if bb>=6 and aa>=1:
    salary=salary+300+3000*aa
    print("其中您有联想电脑", aa, "台，", "享受厂家单件五折优惠")
    print("您有辣条",bb,"包，","享受厂家满",600,"减",300)
    print("您的账户余额为：￥", salary)
J=(money-salary)/10
J=int(J)
print("您可获得积分",J,"分")



