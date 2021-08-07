#体育竞技分析
from random import *
def printintro():
    print("这个程序模拟a和b两个选手的某种竞技比赛")
    print("程序运行需要a和b两个选手的能力值(以0到1之间的小数表示)")
def getinputs():
    a = eval (input ("请输入选手a的能力值(0-1):"))
    b = eval (input ("请输入选手b的能力值(0-1):"))
    n = eval (input("模拟比赛的场次:"))
    return a,b,n
def simngames(n,proba,probb):
    winsa,winsb=0,0
    for i in range(n):
        scorea,scoreb=simOneGame(proba,probb)
        if scorea>scoreb:
            winsa +=1
        else:
            winsb +=1
    return winsa ,winsb
def gameover(a,b):
    return a==15 or b==15
def simOneGame(proba,probb):
    scorea,scoreb=0,0
    serving ="a"
    while not gameover(scorea,scoreb):
        if serving =="a":
            if random()< proba:
                scorea += 1
            else:
                serving="b"
        else:
            if random()<probb:
                scoreb +=1
            else:
                serving="a"
    return scorea,scoreb
def printsummary(winsa,winsb):
    n=winsa+winsb
    print("竞技分析开始,共模拟{}场比赛".format(n))
    print("选手a获胜{}场比赛,占比{:0.1%}".format(winsa,winsa/n))
    print("选手b获胜{}场比赛,占比{:0.1%}".format(winsb,winsb/n))
def main():
    printintro()
    proba,probb,n=getinputs()
    winsa,winsb =simngames(n,proba,probb)
    printsummary(winsa,winsb)
main()



