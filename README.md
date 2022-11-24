from tkinter import *
from PIL import ImageTk,Image
from attendance import *
from studentDetails import *
from admin import *
import datetime
import mysql.connector as cn
def main():
db=cn.connect(host="localhost",user="root",passwd="hardik123",database="attendance") ##
Connecting to MySQL
 cr=db.cursor()
 try:
 date=str(datetime.date.today())
 date=date.split("-")
 date=date[::-1]
 mystr=""
 for i in date:
 mystr=mystr+i+"_"
 mystr=mystr[:-1]
 command='alter table SEPM add column "%s" char(20);'%mystr
 command=command.replace('"','')
 print(command)
 cr.execute(command)
 db.commit()
 except:
 pass
 def toAttendance():
 attend()
 def toDetails():
 details()
 def toadmin():
 admindetail()
 n=1.0
 root=Tk()
 root.resizable(0,0)
 background_image =Image.open("template.png")
 [imageSizeWidth, imageSizeHeight] = root.winfo_screenwidth(), root.winfo_screenheight()
 newImageSizeWidth = int(imageSizeWidth*n)
26
 newImageSizeHeight = int(imageSizeHeight*n)
 background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LA
NCZOS)
 img = ImageTk.PhotoImage(background_image)
 f_lbl= Label(root,image=img)
 f_lbl.place(x=0,y=0,relheight=1.0,relwidth=1.0)
 headingLabel = Label(root, text="SMART ATTENDANCE", fg='black',bg='white',
font=('Rockwell',36,'bold'))
 headingLabel.place(relx=0.4,rely=0.015)
 data =Image.open("data.png")
 data = data.resize((100,100),Image.Resampling.LANCZOS)
 img1 = ImageTk.PhotoImage(data)
# First Button
 headingFrame1 = Frame(root,bg="yellow",bd=5)
 headingFrame1.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.2)
 btn1 = Button(headingFrame1,bg='white',border="5", image=img1,command= toDetails)
btn1.place(relx=0, rely=0, relwidth=1,relheight=0.8)
 w1 = Button(headingFrame1,text="Student Details",bg='black', fg='white',font="Arial 12
bold")
 w1.place(relx=0,rely=0.84,relwidth=1,relheight=0.15)
# Second Button
 headingFrame2 = Frame(root,bg="yellow",bd=5)
 headingFrame2.place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.2)
 btn2 = Button(headingFrame2,bg='white',image=img1,command= toAttendance)
 btn2.place(relx=0,rely=0, relwidth=1,relheight=0.8)
 w2 = Label(headingFrame2,text="Attendance",bg='black', fg='white',font="Arial 12 bold")
 w2.place(relx=0,rely=0.84,relwidth=1)
# Third Button
 headingFrame3 = Frame(root,bg="yellow",bd=5)
 headingFrame3.place(relx=0.7,rely=0.4,relwidth=0.2,relheight=0.2)
 btn3 = Button(headingFrame3,bg='white',image=img1,command= toadmin)
 btn3.place(relx=0,rely=0, relwidth=1,relheight=0.8)
 w3 = Label(headingFrame3,text="Admin Dashboard",bg='black', fg='white',font="Arial 12
bold")
 w3.place(relx=0,rely=0.84,relwidth=1)
# Fourth Button
 b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 def on_enter(e):
27
 global img4
 b4 =Image.open("b.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command= root.destroy)
 def on_leave(e):
 global img4
 b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command= root.destroy)
 btn4 = Button(root,image=img4,borderwidth=0,command= root.destroy)
 btn4.place(relx=0.425,rely=0.8, relwidth=0.117,relheight=0.08)
 btn4.bind('<Enter>', on_enter)
 btn4.bind('<Leave>', on_leave)
 root.attributes('-fullscreen', True)
 root.wm_attributes('-transparentcolor','green')
 root.mainloop()
main() 
