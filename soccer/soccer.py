import random
list = []
dict = {}
avg = []
resulit = ['胜','平','负']
win = ['1:0','2:0','2:1','3:0','3:1','3:2','4:0',
      '4:1','4:2','5:0','5:1','5:2','胜其他']
draw = ['0:0','1:1','2:2','3:3','平其他']
lose = ['0:1','0:2','1:2','0:3','1:3','2:3','0:4',
       '1:4','2:4','0:5','1:5','2:5','负其他']
#随机选择
def test(x):
    for i in range(x):
        ret = random.choice(resulit)
        t = rice(int(change))
        print(t + ":" + ret,end = '\t')
        list.append(ret)
        avg.append(t)
    print()
#比赛结果
def test1(list,avg):
    for j,i in enumerate(list):
        dict[i] = test3(i)
        print(avg[j]+" "+dict.get(i),end = '\t')
def rice(change):
    t = random.randint(1,change+1)
    return str(t)
#比分
def test3(i):
    if i == '胜':
        return random.choice(win)
    elif i == '平':
        return random.choice(draw)
    else:
        return random.choice(lose)
if __name__ == "__main__":
    change = input("请输入总场数:")
    num=input("请输入预测场数:")
    test(int(num))
    ret = input(r"是否预测比分:(Y\N):")
    if ret == 'y' or ret == 'Y':
        test1(list,avg)
    elif ret == 'n' or ret == 'N':
        pass
    else:
        print("终止程序")



