from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
from math import* 
import time
import sqlite3
from tkinter import ttk,messagebox
import os

class Login_Window:
    def __init__ (self,root):
        self.root=root
        """ For Setting Up The Window """
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        #BackGround Colours
        lbl_left=Label(self.root,bg="#08A3D2",bd=0)
        lbl_left.place(x=0,y=0,width=600,relheight=1)
        
        lbl_right=Label(self.root,bg="#031F3C",bd=0)
        lbl_right.place(x=600,y=0,relwidth=1,relheight=1)
        
        #=========Frames===============
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)
        
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        email=Label(login_frame,text="EMAIL/USERNAME",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",18),bg="lightgray",fg="black")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",18),bg="lightgray",fg="black")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#b00857",cursor="hand2",activebackground="white",activeforeground="#b00857",command=self.register_window).place(x=250,y=320)
        btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red",cursor="hand2",activebackground="white",activeforeground="red",command=self.forget_password_window).place(x=450,y=320)
        btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),bg="#b00857",fg="white",cursor="hand2",command=self.login).place(x=250,y=360,width=180,height=40)
        
        
        
        
        # CLock
        self.lbl=Label(self.root,text="Coding Clock",bg="#081923",bd=0,fg="white",compound=BOTTOM,font=("Book Antiqua",25,"bold"))
        self.lbl.place(x=90,y=120,width=350,height=450)
        self.working()
        # self.clock_image()
    
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)
    
    
    
    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All Fields Re Requried For Changing The Password")
            
        else:
            try:
                con=con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Choose Correct Sequrity Question / Enter Correct Answer",parent=self.root2)
                else:
                    cur.execute(" UPDATE employee SET password=? WHERE email=?",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Updated","Your password Has Been Updated",parent=self.root2)     
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To : {str(es)}",parent=self.root2)
                    
    
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Fill Up The Email For Changing The Password",parent=self.root)
       
        else:
            try:
                con=con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",f"Plese Enter The Valid Email Address",parent=self.root2)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+500+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.resizable(False,False)
                    self.root2.config(bg="white")
                    
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    
                    #------------------------Forget Password
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","You Pet Name","Your Birth Place","Your Best Friend")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
                    
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15,"bold"),bg="light gray",fg="black")
                    self.txt_answer.place(x=50,y=210,width=250)
                    
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15,"bold"),bg="light gray",fg="black")
                    self.txt_new_pass.place(x=50,y=290,width=250)
                    
                    btn_change_password=Button(self.root2,text="Change Password",bg="green",fg="white",font=("times new roman",15,"bold"),command=self.forget_password).place(x=100,y=340)
                    
                    self.root2.mainloop()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To : {str(es)}",parent=self.root2)
   
    def register_window(self):
        self.root.destroy()
        import register
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Blank","Fill Up The Entry Fields")
        
        try:
            con=con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            cur.execute("SELECT * FROM employee WHERE email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
            row=cur.fetchone()
            if row == None:
                messagebox.showerror("Error",f"Invalid Username Or Password")
            else:
                messagebox.showinfo("Logined",f"Welcome : {str(self.txt_email.get())}")
                self.root.destroy()
                os.system("python dashboard.py")
            con.close()
                
                
        except Exception as es:
            messagebox.showerror("Error",f"Error Due To : {str(es)}")
    
    
    
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        
        """For Clock Image """
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        """ Formula TO Rotate The Clock"""
        #angle_in_radian = angle_in_degrees * math.pi/180
        #line_lenght = 100
        #center_x = 250
        #center_y = 250
        #end_x = center_x + line_lenght * math.cos(angle in radians)
        #end_y = center_y + line_lenght * math.sin(angle in radians)
        
        origin = 200,200
        """ For Hour Line Image """    
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        """ For Minute Line Image """    
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        """ For Second Line Image """    
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        """For Circle Image"""
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        """ For Saving The Image """
        clock.save("images/clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(hr,min_,sec_)
        self.clock_image(hr, min_, sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
obj=Login_Window(root)
root.mainloop()      
