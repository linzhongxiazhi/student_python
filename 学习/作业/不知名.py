print('***************************')
print('''欢迎光临小象奶茶馆！
您已进入小象奶茶自助点餐系统！
小象奶茶馆售卖宇宙无敌奶茶！
奶茶虽好，可不要贪杯哦！
1号. 原味冰奶茶 3元 
2号. 香蕉冰奶茶 5元 
3号. 草莓冰奶茶 5元  
4号. 蒟蒻冰奶茶 7元  
5号. 珍珠冰奶茶 7元 ''')
print('***************************')
milktea_name=int(input('请输入奶茶号：'))
print('***************************')
milktea_number=int(input('请输入要购买奶茶数量：'))
print('***************************')
Vip=input('请确认是否为会员（会员输入y，非会员输入n）')
print('***************************')
print('您选择的是{}号奶茶，数量为{}杯'.format(milktea_name,milktea_number))
print('***************************')
if milktea_name==1:
    toltal=3*milktea_number
elif milktea_name==2:
    toltal=5*milktea_number
elif milktea_name==3:
    toltal=5*milktea_number
elif milktea_name==4:
    toltal=7*milktea_number
elif milktea_name==5:
    toltal=7*milktea_number
if Vip=='y':
    print('您是本店会员，可以享受会员价')
    a = 0.9* toltal
    print('请您支付{}元'.format(a))
elif Vip=='n':
    print('不好意思哦，您目前还不是我们的会员，\n本次无法享受会员价喽，永远爱你么么哒！')
    print('请您支付{}元'.format(toltal))
else:
    print('我还是个小宝宝，您的输入我看不懂，您拿着小票问问小象君吧！')



print('****************************************')
print('做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！\n\t\t诚挚欢迎您再次光临！')
print('****************************************')