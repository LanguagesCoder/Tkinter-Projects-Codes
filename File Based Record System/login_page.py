from tkinter import*
from tkinter import messagebox

class Login:
    def __init__(self,root):
        """SETTING WINDOW"""
        self.root=root
        self.root.title("File Based Record System")
        self.root.geometry("450x300+450+150")
        
        """VARIABLES"""
        self.username=StringVar()
        self.password=StringVar()
        
        
        
        """FRAME """
        F1 = Frame(self.root,bd=10,relief=GROOVE)
        F1.place(x=0,y=0,width=450,height=300)

        title=Label(F1,text="Login System",font=("times new roman",30,"bold"))
        title.grid(row=0,columnspan=2,pady=20)
        
        """USERNAME"""
        lbl_Username=Label(F1,text="Username :",font=("times new roman",20,"bold"))
        lbl_Username.grid(row=1,column=0,pady=10,padx=20)
        
        txtuser=Entry(F1,bd=7,relief=GROOVE,textvariable=self.username,width=25,font=("arial",11,"bold"))
        txtuser.grid(row=1,column=1,pady=10,padx=10)
        
        """PASSWORD"""
        lbl_Password=Label(F1,text="Password :",font=("times new roman",20,"bold"))
        lbl_Password.grid(row=2,column=0,pady=10,padx=20)
        
        txtpass=Entry(F1,bd=7,relief=GROOVE,textvariable=self.password,width=25,font=("arial",11,"bold"),show="*")
        txtpass.grid(row=2,column=1,pady=10,padx=10)
        
        """Buttons"""
        btn_log=Button(F1,text="Login",bd=7,width=10,height=1,font=("arial",11,"bold"),command=self.login).place( x=10,y=225)
        btn_res=Button(F1,text="Reset",bd=7,width=10,height=1,font=("arial",11,"bold"),command=self.reset).place(x=150,y=225)
        btn_exi=Button(F1,text="Exit" ,bd=7,width=10,height=1,font=("arial",11,"bold"),command=self.exitFunction).place(x=290,y=225)
    
    """WORKING OF LOGIN SYSTEM """    
    def login(self):
        if self.username.get()=="" or self.password.get()=="":
             messagebox.showerror("Error","All Fields Are Required")
        else:
            if self.username.get()=="Durgesh" and self.password.get()=="*pkies5*":
                self.root.destroy()
                import software
                software.GUI_SOFTWARE()
            else:
                messagebox.showerror("Error","Invalid Username Or Password")
        
    """WORKING OF RESET BUTTON"""
    def reset(self):
        self.username.set("")
        self.password.set("")
    
    """WORKING OF EXIT BUTTON"""
    def exitFunction(self):
        exitwindow = messagebox.askyesno("Exit","Do you Want To Exit?",parent=self.root)
        if exitwindow >0:
            self.root.destroy()
    
            
    
"""CREATING WINDOW"""
root=Tk()
obj=Login(root)
root.mainloop()        