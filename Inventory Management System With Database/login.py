#=====Library Imports=====
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os
import smtplib
import time
#=====File Imports=====
import email_pass
class LoginSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Inventory Management System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#fafafa')

        self.otp=''

        self.phone_image=ImageTk.PhotoImage(file='images/phone.png')
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        self.employee_id=StringVar()
        self.password=StringVar()

        login_farme=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        login_farme.place(x=650,y=90,width=350,height=460)

        title=Label(login_farme,text='Login System',font=('Elephant',30,'bold'),bg='white').place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_farme,text='Employee ID',font=('Andalus',15,'bold'),bg='white',fg='#767171').place(x=50,y=100)
        txt_employee_id=Entry(login_farme,font=('times new roman',15),bg='#ECECEC',textvariable=self.employee_id).place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_farme,text='Password',font=('Andalus',15,'bold'),bg='white',fg='#767171').place(x=50,y=200)
        txt_password=Entry(login_farme,font=('times new roman',15),bg='#ECECEC',textvariable=self.password,show='*').place(x=50,y=240,width=250)

        btn_login=Button(login_farme,text='Log In',font=('Arial Rounded MT Bold',15),bg='#00B0F0',cursor='hand2',command=self.login).place(x=50,y=300,width=250,height=35)

        hr=Label(login_farme,bg='lightgray').place(x=50,y=370,width=250,height=2)
        or_=Label(login_farme,fg='lightgray',text='OR',font=('times new roman',15,'bold'),bg='white').place(x=150,y=355)

        btn_forget=Button(login_farme,text='Forget Password',font=('times new roman',15),bg='#FFFFFF',cursor='hand2',fg='#00759E',bd=0,activebackground='white',activeforeground='#00759E',command=self.forget_window).place(x=50,y=390,width=250,height=35)

        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Inventory Managemant System",font=('times new roman',13),bg='white').place(x=0,y=16,relwidth=1)

        self.im1=ImageTk.PhotoImage(file='images/im1.png')
        self.im2=ImageTk.PhotoImage(file='images/im2.png')
        self.im3=ImageTk.PhotoImage(file='images/im3.png')

        self.lbl_change_image=Label(self.root,bg='white')
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()
#=================================================================================================
    def login(self):
        #if self.employee_id.get()=='' or self.password.get()=='':
        #    messagebox.showerror('Error','All Fields Are Required')
        #elif self.employee_id.get()!='Durgesh' or self.password.get()!='*pkies5*':
        #    messagebox.showerror('Error','Invalid employee_id Or Passowrd...\nPlese Try Again...')
        #else:
        #    messagebox.showinfo('Login Successfully',f'Welcome : {self.employee_id.get()}')
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=='' or self.password.get()=='':
                messagebox.showerror('Error','All Fields Are Required',parent=self.root)
            else:
                cur.execute('select utype from employee where eid=? AND pass=?',(
                    self.employee_id.get(),
                    self.password.get(),
                ))
                user=cur.fetchone()

                if user==None:
                    messagebox.showerror('Error','Invalid Employee ID Or Password...',parent=self.root)
                else:
                    if user[0]=='Admin':
                        self.root.destroy()
                        os.system('python dashboard.py')
                    else:
                        self.root.destroy()
                        os.system('python billing.py')

        except Exception as ex:
            messagebox.showerror('Error',f'Error Due To : {str(ex)}',parent=self.root)
#=================================================================================================
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im

        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
#=================================================================================================
    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=='':
                messagebox.showerror('Error','To Change The Password...Please Enter The Employee ID...')
            else:
                cur.execute('select email from employee where eid=?',(self.employee_id.get(),))
                email=cur.fetchone()

                if email==None:
                    messagebox.showerror('Error','Invalid Employee ID...',parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()

                    chk=self.send_email(email[0])

                    if chk!='s':
                        messagebox.showerror('Error','Connection Error...Please Try Again',self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('Forgot / Reset Password')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()
                        self.forget_win.resizable(False,False)

                        title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white').pack(side=TOP,fill=X)

                        lbl_reset=Label(self.forget_win,text='Enter OTP Sent On Registered Email',font=('times new roman',15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=('times new roman',15),bg='lightyellow').place(x=20,y=100,width=250,height=30)

                        self.btn_reset=Button(self.forget_win,text='SUBMIT',font=('times new roman',15),bg='lightblue',command=self.validate_otp)
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        lbl_new_pass=Label(self.forget_win,text='New Password',font=('times new roman',15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=('times new roman',15),bg='lightyellow').place(x=20,y=190,width=250,height=30)

                        lbl_conf_pass=Label(self.forget_win,text='Confirm Password',font=('times new roman',15)).place(x=20,y=225)
                        txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=('times new roman',15),bg='lightyellow').place(x=20,y=255,width=250,height=30)

                        self.btn_update=Button(self.forget_win,text='Update',font=('times new roman',15),bg='lightblue',state=DISABLED,command=self.update_password)
                        self.btn_update.place(x=150,y=300,width=100,height=30)

        except Exception as ex:
            messagebox.showerror('Error',f'Error Due To : {str(ex)}',parent=self.root)
#=================================================================================================
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime('%H%M%S'))+int(time.strftime('%S'))

        subj='Inventory Management System Password Reset OTP For Verification'
        msg=f'Dear Sir/Madam,\n\nEmployee ID : {self.employee_id.get()}\nOTP : {self.otp}\n\nThis Is The OTP For Changing The Password Of The Employee {self.employee_id.get()}...\n\nInventory Management System\nEMail ID : inventorymanagementsystem25r21@gmail.com'
        msg="Subject:{}\n\n{}".format(subj,msg)

        s.sendmail(email_,to_,msg)
        chk=s.ehlo()

        if chk[0]==250:
            return 's'
        else:
            return 'f'
#=================================================================================================
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror('Error','The OTP You Have Entered Is Wrong...Please Enter The Correct OTP',parent=self.forget_win)
#=================================================================================================
    def update_password(self):
        if self.var_new_pass.get()=='' or self.var_conf_pass.get()=='':
            messagebox.showerror('Error','Please Enter Both New Password & Confirm Password...',parent=self.forget_win)
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror('Error','New Password & Confirm Password Should Be Same...',parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute('Update employee SET pass=? where eid=?',(
                    self.var_new_pass.get(),
                    self.employee_id.get(),
                ))
                con.commit()
                messagebox.showinfo('Password Changed',f'The Password Has Been Changed To {self.var_new_pass.get()}',parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror('Error',f'Error Due To : {str(ex)}',parent=self.forget_win)
            
#==================================================================================================
root=Tk()
obj=LoginSystem(root)
root.mainloop()