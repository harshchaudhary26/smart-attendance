from pprint import pprint
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import Style, Treeview
from PIL import Image, ImageTk
import mysql.connector as cn
from math import *
import smtplib
db=cn.connect(host="localhost",user="root",passwd="hardik123",database="attendance") ##
Connecting to MySQL
cr=db.cursor()
def admindetail():
 n=1.0
 root3=Toplevel()
 root3.resizable(0,0)
 background_image =Image.open("template.png") ## Opened the image
 [imageSizeWidth, imageSizeHeight] = root3.winfo_screenwidth(),
root3.winfo_screenheight() ## Putting width and length from original image
 newImageSizeWidth = int(imageSizeWidth*n) ## multipy width by 0.9
 newImageSizeHeight = int(imageSizeHeight*n) ## multiply height by 0.9
 background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
 imgbg = ImageTk.PhotoImage(background_image)
 f_lbl= Label(root3,image=imgbg)
 f_lbl.place(x=0,y=0,relheight=1.0,relwidth=1.0)
 def eml():
 server= smtplib.SMTP('smtp.gmail.com',587)
 server.ehlo()
 server.starttls()
 server.login('sepmattendance@gmail.com','frwqstgvuanpgkui')
 server.sendmail('sepmattendance@gmail.com','st1367@srmist.edu.in','Please attend your
SEPM classes as it is lower than 75%')
 server.close()
 b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.ANTIALIAS)
 img4 = ImageTk.PhotoImage(b4)
 def on_enter(e):
 global img4
 b4 =Image.open("b.jpg")
 b4 = b4.resize((180,69),Image.ANTIALIAS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command= root3.destroy)
 def on_leave(e):
 global img4
 b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.ANTIALIAS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command= root3.destroy)
 s=Style()
 s.theme_use('default')
 s.configure('my.Treeview.Heading', background='light gray', font=('Arial Bold', 14))
 s.configure('my.Treeview.Heading')
 tree=Treeview(root3,columns=(1,2,3,4,5,6,7),show="headings",style='my.Treeview')
 tree.place(relx=0.1,rely=0.25, relwidth=0.8,relheight=0.5)
 tree.heading(1,text="Name",anchor=CENTER)
 tree.heading(2,text="Registration Number",anchor=CENTER)
 tree.heading(3,text="Email",anchor=CENTER)
 tree.heading(4,text="Classes Attended",anchor=CENTER)
 tree.heading(5,text="Total Classes",anchor=CENTER)
 tree.heading(6,text="Attendance Percentage",anchor=CENTER)
 tree.heading(7,text="Late Count",anchor=CENTER)
 tree.column("# 1",width=120,anchor=CENTER)
 tree.column("# 2",width=150,anchor=CENTER)
 tree.column("# 3",width=110,anchor=CENTER)
 tree.column("# 4",width=130,anchor=CENTER)
 tree.column("# 5",width=100,anchor=CENTER)
 tree.column("# 6",width=190,anchor=CENTER)
 tree.column("# 7",width=90,anchor=CENTER)
 mystr="select * from SEPM;"
 cr.execute(mystr)

for i in cr:
 att=0
 reg=i[0]
 name=i[1]
 mob=i[2]
 email=i[3]
 attend=i[4:]
 tot=len(attend)
 for j in (attend):
 if(j=="P"):
 att=att+1
 percent=str(ceil((att/tot)*100))
 tree.insert("",index=0,values=(name,reg,email,str(att),str(tot),str(percent)+"%","2"),tags =
['t1'])
 tree.tag_configure('t1',font="Arial 11")
 btn4 = Button(root3,image=img4,borderwidth=0,command= root3.destroy)
 btn4.place(relx=0.625,rely=0.8, relwidth=0.117,relheight=0.08)
 btn4.bind('<Enter>', on_enter)
 btn4.bind('<Leave>', on_leave)
 b5 =Image.open("email.png")
 b5 = b5.resize((180,69),Image.ANTIALIAS)
 img5 = ImageTk.PhotoImage(b5)
 btn5 = Button(root3,image=img5,borderwidth=0,command= eml)
 btn5.place(relx=0.225,rely=0.8, relwidth=0.117,relheight=0.08)
 root3.attributes('-fullscreen', True)
 root3.mainloop()
admindetail() 

