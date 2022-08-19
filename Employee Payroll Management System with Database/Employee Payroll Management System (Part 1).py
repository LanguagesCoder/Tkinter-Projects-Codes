from tkinter import*
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Manangement System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Manangement System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        #=============Frame 1
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        
        title2=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        """Row 0"""
        """Labels"""
        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        txt_code=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=220,y=74,width=200)
        btn_search=Button(Frame1,text="Search",font=("times new roman",20),bg="gray",fg="black").place(x=440,y=72,height=30)
        
        """Row 1"""
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black").place(x=10,y=120)
        txt_designation=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=125,width=200)
        
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black").place(x=390,y=120)
        txt_dob=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=125,width=200)
        
        """Row 2"""
        lbl_name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black").place(x=10,y=170)
        txt_name=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=175,width=200)
        
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black").place(x=390,y=170)
        txt_doj=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=175,width=200)
        
        """Row 3"""
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=225,width=200)
        
        lbl_experince=Label(Frame1,text="Experience",font=("times new roman",20),bg="white",fg="black").place(x=390,y=220)
        txt_experince=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=225,width=200)
        
        """Row 4"""
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=275,width=200)
        
        lbl_proof=Label(Frame1,text="Proof ID",font=("times new roman",20),bg="white",fg="black").place(x=390,y=270)
        txt_proof=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=275,width=200)
        
        """Row 5"""
        lbl_email=Label(Frame1,text="Email ID",font=("times new roman",20),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=325,width=200)
        
        lbl_contact=Label(Frame1,text="Contact",font=("times new roman",20),bg="white",fg="black").place(x=390,y=320)
        txt_contact=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=325,width=200)
        
        """Row 6"""
        lbl_hired=Label(Frame1,text="Hired Location",font=("times new roman",18),bg="white",fg="black").place(x=10,y=372)
        txt_hired=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=375,width=200)
        
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black").place(x=390,y=370)
        txt_status=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=375,width=200)
        
        """Row 7"""
        lbl_address=Label(Frame1,text="Address",font=("times new roman",18),bg="white",fg="black").place(x=10,y=422)
        txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        txt_address.place(x=170,y=425,width=550,height=150)
        
        
        #=============Frame 2
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)
        
        #=============Frame 3
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)
        

root=Tk()
obj=EmployeeSystem(root)
root.mainloop()       