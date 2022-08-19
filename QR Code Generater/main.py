from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class QR_Code_Generator:
    def __init__(self,root):
        self.root=root
        self.root.title("QR Code Generator")
        self.root.geometry("900x500+200+50")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="   QR Code Generator",font=("times new roman",40),bg="#053246",fg="white",anchor='w').place(x=0,y=0,relwidth=1)
        """Variables"""
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()

        """Employee Detail Window"""
        emp_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_frame.place(x=50,y=100,width=500,height=380)
        emp_title=Label(emp_frame,text="Employee Detials",font=("goudy old style",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)
        
        """Labels"""
        lbl_emp_code=Label(emp_frame,text="Employee ID:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=60)
        lbl_name=Label(emp_frame,text="Name:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=100)
        lbl_department=Label(emp_frame,text="Department:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=140)
        lbl_designation=Label(emp_frame,text="Designation:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=180)
        
        """Entry Fields"""
        txt_emp_code=Entry(emp_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_emp_code).place(x=200,y=60)
        txt_name=Entry(emp_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_name).place(x=200,y=100)
        txt_department=Entry(emp_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_department).place(x=200,y=140)
        txt_designation=Entry(emp_frame,font=("times new roman",15),bg="lightyellow",textvariable=self.var_designation).place(x=200,y=180)
        
        """Buttons"""
        btn_generater=Button(emp_frame,text="Generate QR",font=("times new roman",18,"bold"),bg="#2196f3",fg="white",command=self.generate).place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_frame,text="Clear",font=("times new roman",18,"bold"),bg="#607d8b",fg="white",command=self.clear).place(x=282,y=250,width=120,height=30)
    
        """Messages"""
        self.msg=('Welcome To QR Code Generater')
        self.lbl_msg=Label(emp_frame,text=(self.msg),font=("times new roman",20),bg="white",fg="blue")
        self.lbl_msg.place(x=0,y=310,relwidth=1)
        
        """Employee QR Code Window"""
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_frame.place(x=600,y=100,width=250,height=380)
        qr_title=Label(qr_frame,text="Employee QR Code",font=("goudy old style",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)
        
        """QR Code Image"""
        self.qr_code=Label(qr_frame,text="No QR \nAvailable",font=("times new roman",15),bg="#3f51b5",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
        
    def generate(self):
        if self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_designation.get()=='':
            self.msg=('All Fields Are Required!!!')
            self.lbl_msg.config(text=(self.msg),fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nDesignation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            # print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_QR/"+str(self.var_emp_code.get())+".png")
            """QR Code Image Update"""
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            
            """Updating Notification"""
            self.msg=('QR Generated Sucessfully!!!')
            self.lbl_msg.config(text=(self.msg),fg='green')
    
    def clear (self):
        self.var_emp_code.set(" ")
        self.var_name.set(" ")
        self.var_department.set(" ")
        self.var_designation.set(" ")
        self.msg=('Welcome To QR Code Generater')
        self.lbl_msg.config(text=(self.msg),fg="blue")
        self.qr_code.config(image="")
        
root=Tk()
obj=QR_Code_Generator(root)
root.mainloop()
        
    