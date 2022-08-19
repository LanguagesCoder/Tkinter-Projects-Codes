from tkinter import*
from tkinter import ttk
import pymysql

class Student_Management_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.focus_force()
        
        title=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #All Variables
        self.Roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        
        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=590)
        
        m_title=Label(Manage_Frame,text="Manage Students",fg="white",font=("times new roman",30,"bold"),bg="crimson")
        m_title.grid(row=0,columnspan=2,pady=20)
        
        
        """Labels And Entry Fields"""
        """Roll No."""
        lbl_roll=Label(Manage_Frame,text="Roll No.",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        
        txt_roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.Roll_no_var)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        """Name"""
        lbl_name=Label(Manage_Frame,text="Name",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.name_var)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        """Email"""
        lbl_email=Label(Manage_Frame,text="Email",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.gmail_var)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        """Gender"""
        lbl_email=Label(Manage_Frame,text="Gender",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_email.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        self.gender=ttk.Combobox(Manage_Frame,font=("times new roman",14,"bold"),state='readonly',justify=CENTER,textvariable=self.gender_var)
        self.gender['values']=("Select","Male","Female","Other")
        self.gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        self.gender.current(0)
        
        """Contact"""
        lbl_email=Label(Manage_Frame,text="Contact",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_email.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.contact_var)
        txt_email.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        """Date Of Birth"""
        lbl_email=Label(Manage_Frame,text="D.O.B",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_email.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.dob_var)
        txt_email.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        """Address"""
        lbl_address=Label(Manage_Frame,text="Address",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        """Buttons"""
        #Button Frame
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=520,width=410)
        
        Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)
        
        
        
        #Detail Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=590)
        
        """Search"""
        lbl_search=Label(Detail_Frame,text="Search By",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        self.search=ttk.Combobox(Detail_Frame,font=("times new roman",14,"bold"),state='readonly',justify=CENTER,width=10)
        self.search['values']=("Select","Roll No.","Name","Contact")
        self.search.grid(row=0,column=1,pady=10,padx=20,sticky="w")
        self.search.current(0)
    
        txt_Search=Entry(Detail_Frame,font=("times new roman",14,"bold"),bd=5,relief=GROOVE,width=15)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)
        
        #Table Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)
        
        """ScrollBars"""
        scrolly=Scrollbar(Table_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Table_Frame,orient=HORIZONTAL)
        
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        
        
        
        """Student Table"""
        Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        """Headings"""
        Student_table.heading("roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="D.O.B")
        Student_table.heading("address",text="Address")
        Student_table['show']='headings'
        
        """Columns"""
        Student_table.column("roll",width=100)
        Student_table.column("name",width=100)
        Student_table.column("email",width=100)
        Student_table.column("gender",width=100)
        Student_table.column("contact",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("address",width=150)
        
        scrolly.config(command=Student_table.yview)
        scrollx.config(command=Student_table.xview)
        
        Student_table.pack(fill=BOTH,expand=1)
        
        
    
root=Tk()
obj=Student_Management_System(root)
root.mainloop()    