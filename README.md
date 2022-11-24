from tkinter import *
from PIL import Image, ImageTk
import cv2
from face_recognition import face_encodings , face_locations,compare_faces
import pyttsx3
import mysql.connector as cn
import datetime
a=0
30
reg=""
mystr="C:/Users/hardi/Desktop/Hardik/Semester 4/Project
Management/project/students/box.png"
data =Image.open(mystr)
data = data.resize((100,120),Image.Resampling.LANCZOS)
img1 =""
def attend():
 engine = pyttsx3.init('sapi5')
 voices=engine.getProperty('voices')
 global val,c
 val=3
 engine.setProperty('voice',voices[val].id)
 # print(voices)
 engine. setProperty("rate", 150)
 c=0

 n=1.0
 root1=Toplevel()
 root1.resizable(0,0)
 background_image =Image.open("template.png") ## Opened the image
 [imageSizeWidth, imageSizeHeight] = root1.winfo_screenwidth(),
root1.winfo_screenheight() ## Putting width and length from original image
 newImageSizeWidth = int(imageSizeWidth*n) ## multipy width by 0.9
 newImageSizeHeight = int(imageSizeHeight*n) ## multiply height by 0.9
 background_image =
background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LA
NCZOS)
 imgbg = ImageTk.PhotoImage(background_image)
 f_lbl= Label(root1,image=imgbg)
 f_lbl.place(x=0,y=0,relheight=1.0,relwidth=1.0)
 # Create a Label to capture the Video frames
 label =Label(root1,bg="deep sky blue",relief="solid")
 label.place(relx=0.1,rely=0.25,relwidth=0.4,relheight=0.5)
 cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
 # data =Image.open("C:/Users/hardi/Desktop/Hardik/Semester 4/Project
Management/project/students/box.png")
31
 # data = data.resize((100,120),Image.Resampling.LANCZOS)
 # img1 = ImageTk.PhotoImage(data)

 def speak(audio):
 engine.say(audio)
 engine.runAndWait()

 def finish():
 print("This is working")
 cap.release()
 root1.destroy()
 # Define function to show frame
 def show_frames():
 global a,name,ww3,ww4,ww5,ww6,ww7,ww8,reg,img1
 # Get the latest frame and convert into Image
 cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
 cv2image = cv2.flip(cv2image,1)
 imgGray = cv2.cvtColor(cv2image,cv2.COLOR_BGR2GRAY)
 try:
 loc= face_locations(imgGray)[0]
 cv2.rectangle(cv2image,(loc[3],loc[0]),(loc[1],loc[2]),(0,255,0),2)
 except Exception as e:
 cv2image=cv2image
 img = Image.fromarray(cv2image)
 # Convert image to PhotoImage
 imgtk = ImageTk.PhotoImage(image = img)
 label.imgtk = imgtk
 label.configure(image=imgtk)
 # Repeat after an interval to capture continiously
 a=a+1
 if(a>25):
 encode1=0
 while(type(encode1)==int):
 try:
 encode1 = face_encodings(cv2image)[0]
 if type(encode1)!=int:
 break
 except Exception as e:
 break
 try:
 l=[]
 fl = open("data.txt","r")
32
 v=fl.readlines()
 n=len(v)
 x=0
 for i in range(0,n//129):
 for j in range(x,x+128):
 l.append(float(v[j]))
 x=x+129
 results = compare_faces([l],encode1)
 results[0] = str(results[0])
 if(results[0]=="True"):
 print("working")
 id=v[j+1]
 break
 l.clear()
 fl.close()
 a=0
 id=id.replace("\n","")
 mystr='select Reg_No,Name,Mobile,Email from SEPM where Reg_No="%s";'%id
db=cn.connect(host="localhost",user="root",passwd="hardik123",database="attendance") ##
Connecting to MySQL
 cr=db.cursor()
 cr.execute(mystr)
 for i in cr:
 reg=i[0]
 name=i[1]
 mob=i[2]
 email=i[3]
data.resize((100,120),Image.Resampling.LANCZOS)

 try:
 date=str(datetime.date.today())
 date=date.split("-")
 date=date[::-1]
 mystr=""
 for i in date:
 mystr=mystr+i+"_"
 mystr=mystr[:-1]
 command='select '+mystr+' from SEPM where Reg_No = "%s";'%reg
 print(command)
 cr.execute(command)
 for j in cr:
 for i in j:
 if(i!="P"):
 command='update SEPM set '+mystr+'="P" where Reg_No =
"%s";' %reg
 print(command)
33
 cr.execute(command)
 db.commit()
 mystr="C:/Users/hardi/Desktop/Hardik/Semester 4/Project
Management/project/students/"+reg+".png"
 data =Image.open(mystr)
 data = data.resize((100,120),Image.Resampling.LANCZOS)
 img1 = ImageTk.PhotoImage(data)
 print(img1)
 ww2 = Label(frame1,bg="white",relief="solid",image=img1)
 ww2.place(relx=0.06,rely=0.15,relwidth=0.2,relheight=0.29)
 try:
 ww3.destroy()
 ww4.destroy()
 ww5.destroy()
 ww6.destroy()
 ww7.destroy()
 ww8.destroy()
 except:
 pass
 ww3 = Label(frame1,text=name,bg="deep sky blue",
fg='black',font="Arial 14 bold")
 ww3.place(relx=0.45,rely=0.5)
 ww4 = Label(frame1,text=reg,bg="deep sky blue", fg='black',font="Arial
14 bold")
 ww4.place(relx=0.45,rely=0.57)
 ww5 = Label(frame1,text="80%",bg="deep sky blue",
fg='black',font="Arial 14 bold")
 ww5.place(relx=0.45,rely=0.64)
 ww6 = Label(frame1,text="4",bg="deep sky blue", fg='black',font="Arial
14 bold")
 ww6.place(relx=0.45,rely=0.71)
 ww7 = Label(frame1,text="16",bg="deep sky blue", fg='black',font="Arial
14 bold")
 ww7.place(relx=0.45,rely=0.78)
 ww8 = Label(frame1,text="4",bg="deep sky blue", fg='black',font="Arial
14 bold")
 ww8.place(relx=0.45,rely=0.85)

 speak(name+" has been marked present")
 except Exception as e:
 e=e
 except:
 pass
 label.after(20, show_frames)
b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
34
 img4 = ImageTk.PhotoImage(b4)
 def on_enter(e):
 global img4
 b4 =Image.open("b.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command= lambda: finish())
 def on_leave(e):
 global img4
 b4 =Image.open("a.jpg")
 b4 = b4.resize((180,69),Image.Resampling.LANCZOS)
 img4 = ImageTk.PhotoImage(b4)
 btn4.config(image=img4,command= lambda: finish())
 # HEADING
 global w2
 frame1 = Frame(root1,bg="deep sky blue",bd=5)
 frame1.place(relx=0.6,rely=0.25,relwidth=0.35,relheight=0.5)
 w1 = Label(frame1,text="Student Information",bg="deep sky blue", fg='navy',font="Roman
30 bold")
 w1.place(relx=0.0,rely=0.02,relwidth=0.76)
 w2 = Label(frame1,bg="white",relief="solid")
 w2.place(relx=0.06,rely=0.15,relwidth=0.2,relheight=0.29)
 #w2.place_forget()
 w3 = Label(frame1,text="Name: ",bg="deep sky blue", fg='white',font="Arial 14 bold")
 w3.place(relx=0.03,rely=0.5,relwidth=0.2)
 w4 = Label(frame1,text="Registraion Number: ",bg="deep sky blue", fg='white',font="Arial
14 bold")
 w4.place(relx=0.05,rely=0.57,relwidth=0.4)
 w5 = Label(frame1,text="Attendance : ",bg="deep sky blue", fg='white',font="Arial 14
bold")
 w5.place(relx=0.03,rely=0.64,relwidth=0.3)
 w6 = Label(frame1,text="Margin : ",bg="deep sky blue", fg='white',font="Arial 14 bold")
 w6.place(relx=0.03,rely=0.71,relwidth=0.22)
 w7 = Label(frame1,text="Hours Present : ",bg="deep sky blue", fg='white',font="Arial 14
bold")
 w7.place(relx=0.05,rely=0.78,relwidth=0.32)
 w8 = Label(frame1,text="Hours Absent : ",bg="deep sky blue", fg='white',font="Arial 14
bold")
 w8.place(relx=0.05,rely=0.85,relwidth=0.3)
 btn4 = Button(root1,image=img4,borderwidth=0,command= lambda: finish())
 btn4.place(relx=0.425,rely=0.8, relwidth=0.117,relheight=0.08)
 btn4.bind('<Enter>', on_enter)
 btn4.bind('<Leave>', on_leave)
 root1.attributes('-fullscreen', True)
 show_frames()
 root1.mainloop() 
