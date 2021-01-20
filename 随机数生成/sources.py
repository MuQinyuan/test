import sys
import time
import random
#生成前区号码
List_RED = []
for i in range(0,35):
    List_RED.append(i+1)
#生成后区号码
List_BLUE = []
for i in range(0,12):
    List_BLUE.append(i+1)
#计算金额
def Calculate_money(a,b):
	a = chengjie(a)/(chengjie(a-5)*chengjie(5))
	b = chengjie(b)/(chengjie(b-2)*chengjie(2))
	return '''预计金额为:{}'''.format(a*b*2)
#乘阶算法	
def chengjie(c):
	if c<=1:
		return 1
	else:
		return c*chengjie(c-1)
#复式
def Random_gen(a,b):
# 抽取前区5个号码
    num_R = random.sample(List_RED,a)
    key1='+'.join(str(i)for i in num_R)
#抽取后区2个号码
    num_B = random.sample(List_BLUE,b)
    key2='+'.join(str(i)for i in num_B)
#格式化输出
    return '''前区号码为：{}    后区号码为：{}'''.format(key1,key2)
#单式
class Random_gen1:
# 抽取前区5个号码
    def __init__(self):
        self.num_R = random.sample(List_RED,5)
        self.key1='+'.join(str(i)for i in self.num_R)
#抽取后区2个号码
     
        self.num_B = random.sample(List_BLUE,2)
        self.key2='+'.join(str(i)for i in self.num_B)
    def output(self):
#格式化输出
        return '''前区号码为：{}    后区号码为：{}'''.format(key1,key2)
#输入文本
#with open('base.txt','w',encoding='utf-8')as f:
       # f.write(Random_gen())
#main()
