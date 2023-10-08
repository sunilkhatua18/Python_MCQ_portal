from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
#print(dir(tkinter))

win=Tk()
img=ImageTk.PhotoImage(Image.open("C:\\Users\\sunil\\Desktop\BCAPROJECT\\login.jpg"))
label=Label(image=img)
label.pack()

def Login():
	username=uid.get()
	Password=pwd.get()
	print(username,"",Password)
	conobj=pymysql.connect(host='localhost',user='root',password='',port=3306)
	curobj=conobj.cursor()
	curobj.execute('use BCA2021AB;')
	#curobj.execute('alter table INFO add (mark int, per_mark varchar(7));')
	test= f'Select * from INFO where userid="{username}" and password="{Password}";'
	curobj.execute(test)
	record=curobj.fetchall()
	if len(record):
		messagebox.showinfo("logininfo","welcome to home page")
		win.destroy()
		from mcq import myQuiz
		quiz=myQuiz()
	else:
		messagebox.showinfo("logininfo","Sorry!!! try again....Try Next Time")
	
def Reset():
	uid.delete(0,END)
	pwd.delete(0,END)
def newUser():
	
	win.destroy()
	win1=Tk()
	img=ImageTk.PhotoImage(Image.open("C:\\Users\\sunil\\Desktop\\BCAPROJECT\\pin.jpg"))
	label=Label(image=img)
	label.pack()

	def Submit():
			a=nuid.get()
			b=nphno.get()
			c=menu.get()
			d=var1.get()
			e=npwd.get()
			#print(a,"",b,"",c,"",d,"",e)
			conobj=pymysql.connect(host="localhost",user="root",password="",port=3306)
			curobj=conobj.cursor()
			#curobj.execute('create database BCA2021AB;')
			curobj.execute('use BCA2021AB;')
			#curobj.execute('create table INFO (userid varchar(20),phno bigint(10),dept varchar(20),gender varchar(6),password varchar(10));')
			r='insert into INFO(userid,phno,dept,gender,password) values("{userid}","{phno}","{dept}","{gender}","{password}");'
			r1=r.format(userid=a,phno=b,dept=c,gender=d,password=e)
			#print(r1)
			curobj.execute(r1)
			conobj.commit()
			curobj.close()
			conobj.close()
			win1.destroy()
	def Reset():
		nuid.delete(0,END)
		nphno.delete(0,END)
		menu.set(None)
		#var1.delete(0,END)
		var1.set(None)
		npwd.delete(0,END)

	win1.title("signup page")
	win1.maxsize(700,700)
	win1.minsize(700,700)
	Label(win1,text="Please signup Here",font=('Bernard MT',20),fg="white",bg="blue",relief=RAISED,width=30).place(x=110,y=50)

	Label(win1,text="Set User ID",font=('Bernard MT',15,),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=150)
	nuid=Entry(win1,font=('Bernard MT',15),fg="white",bg="blue")
	nuid.place(x=350,y=150)
	
	
	Label(win1,text="Enter Phone Number",font=('Bernard MT',15),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=250)
	nphno=Entry(win1,font=('Bernard MT',15),fg="white",bg="blue")
	nphno.place(x=350,y=250)

	
	Label(win1,text="Select Dept name",font=('Bernard MT',15),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=350)
	menu=StringVar()
	drop=OptionMenu(win1,menu,"BCA","BSc.ITM","BSc.CS")
	drop.place(x=450,y=350)

	
	Label(win1,text="Select Gender",font=('Bernard MT',15),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=450)
	var1=StringVar(win1,None)
	Radiobutton(win1,text="Male",variable=var1,value="M",font=('Bernard MT',15)).place(x=350,y=450)
	Radiobutton(win1,text="FeMale",variable=var1,value="F",font=('Bernard MT',15)).place(x=450,y=450)

	
	Label(win1,text="Enter New Password",font=('Bernard MT',15),fg="black",bg="white",relief=RAISED,width=20).place(x=120,y=550)
	npwd=Entry(win1,font=('Bernard MT',15),fg="white",bg="blue",show="*")
	npwd.place(x=350,y=550)

	Button(win1,text="Submit",font=('Bernard MT',15),bg="green",fg="red",command=Submit).place(x=200,y=600)
	Button(win1,text="Reset",font=('Bernard MT',15),bg="red",fg="blue",command=Reset).place(x=500,y=600)
	win1.mainloop()

def Exit():
	win.destroy( )			


win.title("Home Page")
win.maxsize(700,700)
win.minsize(700,700)

Label(win,text="Please Login Here",font=('Bernard MT',20),fg="white",bg="blue",relief=RAISED,width=20,height=1).place(x=120,y=50)

Label(win,text="Enter User ID",font=('Bernard MT',15),fg="black",bg="white",relief=RAISED,width=20).place(x=110,y=150)
uid=Entry(win,font=('Bernard MT',15),fg="white",bg="blue")
uid.place(x=350,y=150)


Label(win,text="Enter Password",font=('Bernard MT',15),fg="black",bg="white",relief=RAISED,width=20).place(x=110,y=250)
pwd=Entry(win,font=('Bernard MT',15),fg="white",bg="blue",show="*")
pwd.place(x=350,y=250)

Button(win,text="Login",font=('Bernard MT',15),bg="brown",fg="white",command=Login,activebackground="#c0c0c0",relief=GROOVE).place(x=200,y=400)
Button(win,text="Reset",font=('Bernard MT',15),bg="brown",fg="white",command=Reset).place(x=400,y=400)
Button(win,text="SignUp",font=('Bernard MT',15),bg="brown",fg="white",command=newUser).place(x=200,y=500)
Button(win,text="Exit",font=('Bernard MT',15),bg="brown",fg="white",command=Exit).place(x=400,y=500)


win.mainloop()