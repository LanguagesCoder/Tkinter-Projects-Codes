from tkinter import*
import time
import datetime
import calendar
root = Tk()

root.title("Digital Clock")
root.geometry("1350x700+0+0")
root.config(bg="#081923")

"""WORKING OF A CLOCK"""
def clock():
   """TIME"""
   h = str(time.strftime("%H")) 
   m = str(time.strftime("%M"))
   s = str(time.strftime("%S"))
   # print(h,m,s)
   
   """DATE"""
   dd = str(time.strftime("%d")) 
   mm = int(time.strftime("%m"))
   mm=calendar.month_name[mm]
   yy = datetime.datetime.now()
   # print(dd,mm,yy)

   if int(h)>12 and int(m)>0:
       lbl_noon.config(text="PM")
   
   if int(h)>12:
       h=str((int(h)-12))
       
   lbl_hr.config(text=h)
   lbl_min.config(text=m)
   lbl_sec.config(text=s)
   
   lbl_month.config(text=dd)
   lbl_year.config(text=str(mm))
   lbl_c_date.config(text=str(yy.year))
   
   lbl_hr.after(200,clock)




"""HOUR"""
lbl_hr = Label(root,text="12",font=("times new roman",50,"bold"),bg="#0875B7",fg="white" )
lbl_hr.place(x=350,y=200,width=150,height=150)

lbl_hr2 = Label(root,text="HOUR",font=("times new roman",20,"bold"),bg="#0875B7",fg="white" )
lbl_hr2.place(x=350,y=360,width=150,height=50)

"""MINUTES"""
lbl_min = Label(root,text="12",font=("times new roman",50,"bold"),bg="#0875B7",fg="white" )
lbl_min.place(x=520,y=200,width=150,height=150)

lbl_min2 = Label(root,text="MINUTES",font=("times new roman",20,"bold"),bg="#0875B7",fg="white" )
lbl_min2.place(x=520,y=360,width=150,height=50)

"""SECONDS"""
lbl_sec = Label(root,text="12",font=("times new roman",50,"bold"),bg="#DF002A",fg="white" )
lbl_sec.place(x=690,y=200,width=150,height=150)

lbl_sec2 = Label(root,text="SECONDS",font=("times new roman",20,"bold"),bg="#DF002A",fg="white" )
lbl_sec2.place(x=690,y=360,width=150,height=50)

"""NOON"""
lbl_noon = Label(root,text="AM",font=("times new roman",50,"bold"),bg="#DF002A",fg="white" )
lbl_noon.place(x=860,y=200,width=150,height=150)

lbl_noon2 = Label(root,text="NOON",font=("times new roman",20,"bold"),bg="#DF002A",fg="white" )
lbl_noon2.place(x=860,y=360,width=150,height=50)

"""DATE"""
lbl_date = Label(root,text="Date",font=("times new roman",20,"bold"),bg="#0875B7",fg="white" )
lbl_date.place(x=350,y=420,width=150,height=50)

"""Month"""
lbl_month = Label(root,text="Month",font=("times new roman",20,"bold"),bg="#0875B7",fg="white" )
lbl_month.place(x=520,y=420,width=150,height=50)

"""Year"""
lbl_year = Label(root,text="Year",font=("times new roman",20,"bold"),bg="#DF002A",fg="white" )
lbl_year.place(x=690,y=420,width=150,height=50)

"""C_date"""
lbl_c_date = Label(root,text="Date",font=("times new roman",20,"bold"),bg="#DF002A",fg="white" )
lbl_c_date.place(x=860,y=420,width=150,height=50)



clock()
root.mainloop()