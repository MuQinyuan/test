from tkinter import *
import tkinter.font as tkFont
from sources import Random_gen1
import time
top = Tk()
top.title("大乐透机选")
helv36 = tkFont.Font(family='Helvetica',size=18,weight= 'bold')
cv = Canvas(top,bg ='white')
cv.bell()
cv.pack()
class cvShow:

	def __init__(self):
		self.x0,self.y0,self.x1,self.y1=12,12,52,52
		self.num = 0
	def start(self):
		if self.x0 != 12 and self.y0 !=12:
			self.x0=12
			self.x1=52
			self.y0 = self.y0+52
			self.y1 = self.y1+52
		self.volue1 = Random_gen1().num_R
		self.volue2 = Random_gen1().num_B
		for i,j in enumerate(self.volue1+self.volue2):
			self.flag = 'red' 
			if i >= 5:
				self.flag = 'blue'
			cv.create_oval(self.x0,self.y0,self.x1,self.y1,width = 0,fill = self.flag,tags = 'a')
			cv.create_text(self.x0+22,self.y1-20,text = j,width = 100,anchor = 'center',font=helv36,tags = 'a')
			self.x0=self.x0+52
			self.x1 = self.x1+52
		self.y0 =self.y0+52
		self.x0 = 12
		self.y1 = self.y1+52
		self.x1 = 52
		if self.y1==52*6:
			self.y1=52
			self.y0=12

	def delete(self):
		cv.delete('a')
		self.y1=52
		self.y0=12
		#self.w = Label(cv, text="Hello RUNOOB!").pack()
		self.x0 = 12
		self.x1 = 52
		self.num = 0
	def eventhandler(self,ev = None):
		tEn.focus()
		self.num=self.num+1
		self.flag = 'red'
		if self.num >= 6 and self.num <=7:
			self.flag = 'blue'
		elif self.num >7:
			self.num = 1
			self.y0 = self.y0+52
			self.x0 = 12
			self.y1 = self.y1+52
			self.x1 = 52

		cv.create_oval(self.x0,self.y0,self.x1,self.y1,width = 0,fill = self.flag,tags = 'a')
		cv.create_text(self.x0+22,self.y1-20,text = tEn.get(),width = 100,anchor = 'center',font=helv36,tags = 'a')
		self.x0 = self.x0+52
		self.x1 = self.x1+52

		if self.y1==52*6:
			self.y1=52
			self.y0=12

		tEn.delete(0, END)


show = cvShow()


frame1 = Frame(top)
tEn = Entry(frame1, bd =5,relief=SUNKEN)
tEn.pack(side = 'left',expand ='yes',fill='none',anchor ='w')
tEn.bind('<Return>', show.eventhandler)
dBn = Button(frame1,text = '提交',command = show.eventhandler).pack(side = 'left',expand='yes',fill = 'none')
frame1.pack(padx=1,pady=1,side = 'top',anchor = 'w',fill='x')


sBn = Button(top,text = '开始',command = show.start).pack(side = 'left',expand='yes',fill = 'none')
dBn = Button(top,text = '清除',command = show.delete).pack(side = 'left',expand='yes',fill = 'none')
eBn = Button(top,text = '结束',command = top.destroy).pack(side = 'right',expand='yes',fill = 'none')

top.mainloop()
