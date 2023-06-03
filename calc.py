import math
from tkinter import *
from customtkinter import *
from ctypes import windll, byref, sizeof, c_int

win=CTk(fg_color='#0b0b0b')
win.resizable(False,False)
win.title('Calculator',)
HWND=windll.user32.GetParent(win.winfo_id())
tbc=0x000b0b0b
windll.dwmapi.DwmSetWindowAttribute(HWND,35,byref(c_int(tbc)),sizeof(c_int))
win.update()
global f1
f1=CTkFrame(win,fg_color='#1b1b1b',height=64,corner_radius=20)
f1.pack(fill='x',padx=5,pady=3,side='top')
CTkLabel(f1,text='',font=('product sans',30)).pack(side='left',pady=13,padx=5)
f2=CTkFrame(win,fg_color='transparent')
f2.pack(expand=True,fill='both',padx=1,pady=1,side='bottom')
Grid.rowconfigure(f2,0,weight=1)
Grid.rowconfigure(f2,1,weight=1)
Grid.rowconfigure(f2,2,weight=1)
Grid.rowconfigure(f2,3,weight=1)
Grid.rowconfigure(f2,4,weight=1)
Grid.rowconfigure(f2,5,weight=1)
Grid.columnconfigure(f2,0,weight=1)
Grid.columnconfigure(f2,1,weight=1)
Grid.columnconfigure(f2,2,weight=1)
Grid.columnconfigure(f2,3,weight=1)

global string 
string=[]

def bf():
	string.append(str(math.pi))
	l0=CTkLabel(f1,text='π',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
b=CTkButton(f2,text='π', text_color='#bbbbbb',font=('product sans',20),command=bf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def cf():
	l0=CTkLabel(f1,text='^',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('**') 
c=CTkButton(f2,text='^', text_color='#bbbbbb',font=('product sans',20),command=cf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def ef():
	global f1
	f1.destroy()
	f1=CTkFrame(win,fg_color='#1b1b1b',height=64,corner_radius=20)
	f1.pack(fill='x',padx=5,pady=3,side='top')
	CTkLabel(f1,text='',font=('product sans',30)).pack(side='left',pady=13,padx=5)
	string.clear()
e=CTkButton(f2,text='AC',text_color='#bbbbbb',font=('product sans',10),command=ef,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def ff():
	l0=CTkLabel(f1,text='(',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('(')
f=CTkButton(f2,text='(', text_color='#bbbbbb',font=('product sans',20),command=ff,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def gf():
	l0=CTkLabel(f1,text=')',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append(')')
g=CTkButton(f2,text=')', text_color='#bbbbbb',font=('product sans',20),command=gf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def hf():
	l0=CTkLabel(f1,text='÷',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('/')
h=CTkButton(f2,text='÷', text_color='#bbbbbb',font=('product sans',25),command=hf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def jf():
	l0=CTkLabel(f1,text='7',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('7')
j=CTkButton(f2,text='7', text_color='#bbbbbb',font=('product sans',20),command=jf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def kf():
	l0=CTkLabel(f1,text='8',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('8')
k=CTkButton(f2,text='8', text_color='#bbbbbb',font=('product sans',20),command=kf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def lf():
	l0=CTkLabel(f1,text='9',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('9')
l=CTkButton(f2,text='9', text_color='#bbbbbb',font=('product sans',20),command=lf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def mf():
	l0=CTkLabel(f1,text='×',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('*')
m=CTkButton(f2,text='×', text_color='#bbbbbb',font=('product sans',25),command=mf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def nf():
	l0=CTkLabel(f1,text='4',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('4')
n=CTkButton(f2,text='4', text_color='#bbbbbb',font=('product sans',20),command=nf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def of():
	l0=CTkLabel(f1,text='5',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('5')
o=CTkButton(f2,text='5', text_color='#bbbbbb',font=('product sans',20),command=of,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def pf():
	l0=CTkLabel(f1,text='6',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('6')
p=CTkButton(f2,text='6', text_color='#bbbbbb',font=('product sans',20),command=pf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def qf():
	l0=CTkLabel(f1,text='-',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('-')
q=CTkButton(f2,text='-', text_color='#bbbbbb',font=('product sans',25),command=qf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def rf():
	l0=CTkLabel(f1,text='1',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('1')
r=CTkButton(f2,text='1', text_color='#bbbbbb',font=('product sans',20),command=rf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def sf():
	l0=CTkLabel(f1,text='2',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('2')
s=CTkButton(f2,text='2', text_color='#bbbbbb',font=('product sans',20),command=sf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def tf():
	l0=CTkLabel(f1,text='3',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('3')
t=CTkButton(f2,text='3', text_color='#bbbbbb',font=('product sans',20),command=tf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def uf():
	l0=CTkLabel(f1,text='+',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('+')
u=CTkButton(f2,text='+', text_color='#bbbbbb',font=('product sans',25),command=uf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def vf():
	l0=CTkLabel(f1,text='0',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('0')
v=CTkButton(f2,text='0', text_color='#bbbbbb',font=('product sans',20),command=vf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def wf():
	l0=CTkLabel(f1,text='.',text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.append('.')
w=CTkButton(f2,text='.', text_color='#bbbbbb',font=('product sans',20),command=wf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=64,corner_radius=20)

def xf():	
	string.pop()
	global f1
	f1.destroy()
	f1=CTkFrame(win,fg_color='#1b1b1b',height=64,corner_radius=20)
	f1.pack(fill='x',padx=5,pady=3,side='top')
	CTkLabel(f1,text='',font=('product sans',30)).pack(side='left',pady=13,padx=5)
	for i in string:
		if i=='**':
			string[string.index(i)]='^'
		if i=='/':
			string[string.index(i)]='÷'
		if i=='*':
			string[string.index(i)]='×'
	z=(''.join(string))
	l0=CTkLabel(f1,text=z,text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)      
x=CTkButton(f2,text='⌫',text_color='#bbbbbb',font=('product sans',10),command=xf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=135,corner_radius=20)

def yf():
	global f1
	f1.destroy()
	f1=CTkFrame(win,fg_color='#1b1b1b',height=64,corner_radius=20)
	f1.pack(fill='x',padx=5,pady=3,side='top')
	CTkLabel(f1,text='',font=('product sans',30)).pack(side='left',pady=13,padx=5)
	z=str(eval(''.join(string)))
	l0=CTkLabel(f1,text=z,text_color='#bbbbbb',font=('product sans',30))
	l0.pack(side='left',pady=13)
	string.clear()
	string.append(z)
y=CTkButton(f2,text='=', text_color='#bbbbbb',font=('product sans',25),command=yf,
fg_color='#1b1b1b',hover_color='#101010',height=64,width=135,corner_radius=20)


b.grid(column=0,row=0,padx=3,pady=3)
c.grid(column=0,row=1,padx=3,pady=3)
e.grid(column=1,row=0,padx=3,pady=3)
f.grid(column=1,row=1,padx=3,pady=3)
g.grid(column=2,row=1,padx=3,pady=3)
h.grid(column=3,row=1,padx=3,pady=3)
j.grid(column=0,row=2,padx=3,pady=3)
k.grid(column=1,row=2,padx=3,pady=3)
l.grid(column=2,row=2,padx=3,pady=3)
m.grid(column=3,row=2,padx=3,pady=3)
n.grid(column=0,row=3,padx=3,pady=3)
o.grid(column=1,row=3,padx=3,pady=3)
p.grid(column=2,row=3,padx=3,pady=3)
q.grid(column=3,row=3,padx=3,pady=3)
r.grid(column=0,row=4,padx=3,pady=3)
s.grid(column=1,row=4,padx=3,pady=3)
t.grid(column=2,row=4,padx=3,pady=3)
u.grid(column=3,row=4,padx=3,pady=3)
v.grid(column=0,row=5,padx=3,pady=3)
w.grid(column=1,row=5,padx=3,pady=3)
x.grid(column=2,row=0,padx=3,pady=3,columnspan=2)
y.grid(column=2,row=5,padx=3,pady=3,columnspan=2)
win.mainloop()

