from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from face_recognition import face_encodings , face_locations,compare_faces
import os
import mysql.connector as cn
def details():
 n=1.0
 root2=Toplevel()
 root2.resizable(0,0)
 background_image =Image.open("template.png") ## Opened the image
 [imageSizeWidth, imageSizeHeight] = root2.winfo_screenwidth(),
root2.winfo_screenheight() ## Putting width and length from original image
 newImageSizeWidth = int(imageSizeWidth*n) ## multipy width by 0.9
 newImageSizeHeight = int(imageSizeHeight*n) ## multiply height by 0.9
 background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LA
NCZOS)
 imgbg = ImageTk.PhotoImage(background_image)
 f_lbl= Label(root2,image=imgbg)
 f_lbl.place(x=0,y=0,relheight=1.0,relwidth=1.0)

 data =Image.open("C:/Users/hardi/Desktop/Hardik/Semester 4/Project
Management/project/students/box.png")
 data = data.resize((100,120),Image.Resampling.LANCZOS)
 faceimage = ImageTk.PhotoImage(data)

 def finish():
 if(str(studentinfo2.get())==""):
 messagebox.showinfo("Error","Plese Enter your name")
 elif(str(studentinfo3.get())==""):
 messagebox.showinfo("Error","Plese Enter your Reg Num")
 elif(str(studentinfo5.get())==""):
 messagebox.showinfo("Error","Plese Enter your Email")

 elif(str(studentinfo6.get())==""):
 messagebox.showinfo("Error","Plese Enter your Mobile Number")

 elif(not(studentinfo6.get().isnumeric())):
 messagebox.showinfo("Error","Plese Enter your mobile properly")
 else:
 l=[]
 fl = open("data.txt","r")
 v=fl.readlines()
 n=len(v)
 check=0
 a=0
 for i in range(0,n//129):
 for j in range(a,a+128):
 l.append(float(v[j]))
 a=a+129
 results = compare_faces([l],encode1)
 results[0] = str(results[0])
 l.clear()
 fl.close()
 if(check==0):
 fl = open("data.txt","a")
 fl.write("\n")
 for i in encode1:
 fl.write(str(i)+"\n")
 fl.write(reg)
 fl.close()
 root2.destroy()

 def capture():
 global faceimage,encode1,reg,name,mobile,email
 if(str(studentinfo3.get())==""):
 messagebox.showerror("Error","Fill the details first")
 else:
 frameWidth = 640
 frameHeight = 480
 cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
 cap.set(3, frameWidth)
 cap.set(4, frameHeight)
 cap.set(10,150)
 encode1=0
 i=0
 while (i<30):
 success, img1 = cap.read()
 imgGray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
 img1 = cv2.flip(img1,1)
 imgGray = cv2.flip(imgGray,1)
 try:
 loc= face_locations(imgGray)[0]
 cv2.rectangle(imgGray,(loc[3],loc[0]),(loc[1],loc[2]),(0,255,0),2)
 cv2.imshow("Result",img1)
 i=i+1
 except Exception as e:
 cv2.imshow("Result",img1)
 if cv2.waitKey(1) & 0xFF == ord('q'):
 break
 if(i>25):
 encode1=0
 while(type(encode1)==int):
 try:
 encode1 = face_encodings(img1)[0]
 if type(encode1)!=int:
 break
 except Exception as e:
 break
 name=str(studentinfo2.get())
 reg=str(studentinfo3.get())
 email=str(studentinfo5.get())
 mobile=str(studentinfo6.get())
 print(reg)
 cv2.imwrite("C:/Users/hardi/Desktop/Hardik/Semester 4/Project
Management/project/students/"+reg+".png", img1)
 cv2.destroyWindow("Result")
 data =Image.open("C:/Users/hardi/Desktop/Hardik/Semester 4/Project
Management/project/students/"+reg+".png")
 data = data.resize((140,130),Image.Resampling.LANCZOS)
 faceimage = ImageTk.PhotoImage(data)
 w7 = Label(frame1,relief="solid",image=faceimage)
 w7.place(relx=0.72,rely=0.25,relwidth=0.14,relheight=0.29)

db=cn.connect(host="localhost",user="root",passwd="hardik123",database="attendance") ##
Connecting to MySQL
 cr=db.cursor()
 mystr="insert into "+"SEPM"+"(Reg_No,Name,Mobile,Email) values
('"+reg+"','"+name+"','"+mobile+"','"+email+".srmist.edu.in"+"')"
 cr.execute(mystr)
 db.commit()
 return
 return
 b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 def on_enter(e):
 global img4
 b4 =Image.open("b.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command=root2.destroy)
 def on_leave(e):
 global img4
 b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command=root2.destroy)
 def on_enter_sub(e):
 global img5
 b5 =Image.open("2.jpg")
 b5 = b5.resize((180,69),Image.Resampling.LANCZOS)
 img5 = ImageTk.PhotoImage(b5)
 btn5.config(image=img5,command= lambda: finish())
 def on_leave_sub(e):
 global img5
 b5 =Image.open("1.jpg")
 b5 = b5.resize((180,69),Image.Resampling.LANCZOS)
 img5 = ImageTk.PhotoImage(b5)
 btn5.config(image=img5,command= lambda: finish())

 btn4 = Button(root2,image=img4,borderwidth=0,command= lambda: finish())
 btn4.place(relx=0.225,rely=0.8, relwidth=0.117,relheight=0.08)
 btn4.bind('<Enter>', on_enter)
 btn4.bind('<Leave>', on_leave)
 b5 =Image.open("1.jpg")
 b5 = b5.resize((180,69),Image.Resampling.LANCZOS)
 img5 = ImageTk.PhotoImage(b5)
 btn5 = Button(root2,image=img5,borderwidth=0,command=root2.destroy)
 btn5.place(relx=0.625,rely=0.8, relwidth=0.117,relheight=0.08)
 btn5.bind('<Enter>', on_enter_sub)
 btn5.bind('<Leave>', on_leave_sub)
 frame1 = Frame(root2,bg="grey",bd=5)
 frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.55)
 w1 = Label(frame1,text="Student Details",bg="grey", fg='white',font="Rockwell 30 bold")
 w1.place(relx=0.1,rely=0.02,relwidth=0.8)
 w2 = Label(frame1,text="Name: ",bg="grey", fg='yellow',font="Arial 14 bold")
 w2.place(relx=0.06,rely=0.27,relwidth=0.2,relheight=0.05)
 studentinfo2 = Entry(frame1,font='Arial')
 studentinfo2.place(relx=0.2,rely=0.27, relwidth=0.3, relheight=0.05)
 w3 = Label(frame1,text="Reg No : ",bg="grey", fg='yellow',font="Arial 14 bold")
 w3.place(relx=0.045,rely=0.4,relwidth=0.2,relheight=0.05)
 studentinfo3 = Entry(frame1,font='Arial')
 studentinfo3.place(relx=0.2,rely=0.4, relwidth=0.3, relheight=0.05)
 w4 = Label(frame1,text="Email ID : ",bg="grey", fg='yellow',font="Arial 14 bold")
 w4.place(relx=0.045,rely=0.53,relwidth=0.2,relheight=0.05)
 studentinfo4 = Entry(frame1,font='Arial')
 studentinfo4.insert(END,'@srmist.edu.in')
 studentinfo4.config(state=DISABLED,disabledbackground="grey99")
 studentinfo4.place(relx=0.28,rely=0.53, relwidth=0.15, relheight=0.05)
 studentinfo5 = Entry(frame1,font='Arial')
 studentinfo5.place(relx=0.2,rely=0.53, relwidth=0.08, relheight=0.05)
 w5 = Label(frame1,text="Mobile Number : ",bg="grey", fg='yellow',font="Arial 14 bold")
 w5.place(relx=0.01,rely=0.66,relwidth=0.2,relheight=0.05)
 studentinfo6 = Entry(frame1,font='Arial')
 studentinfo6.place(relx=0.2,rely=0.66, relwidth=0.3, relheight=0.05)
 w7 = Label(frame1,bg="white",relief="solid",image=faceimage)
 w7.place(relx=0.72,rely=0.25,relwidth=0.14,relheight=0.29)
 b1 = Button(frame1,text="Open Cam",command=capture)
 b1.place(relx=0.75,rely=0.6)
 root2.attributes('-fullscreen', True)
 root2.mainloop()  
