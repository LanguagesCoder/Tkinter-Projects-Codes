from tkinter import*
from tkinter import ttk,messagebox
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
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        
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
        
        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.email_var)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        """Gender"""
        lbl_email=Label(Manage_Frame,text="Gender",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_email.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        self.gender=ttk.Combobox(Manage_Frame,font=("times new roman",14,"bold"),state='readonly',justify=CENTER,textvariable=self.gender_var)
        self.gender['values']=("Select","Male/Men","Female","Other")
        self.gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        self.gender.current(0)
        
        """Contact"""
        lbl_email=Label(Manage_Frame,text="Contact",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_email.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.contact_var)
        txt_email.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        """Date Of Birth"""
        lbl_dob=Label(Manage_Frame,text="D.O.B",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_dob=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.dob_var)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        """Address"""
        lbl_address=Label(Manage_Frame,text="Address",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        """Buttons"""
        #Button Frame
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=520,width=410)
        
        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        
        
        
        #Detail Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=590)
        
        """Search"""
        lbl_search=Label(Detail_Frame,text="Search By",fg="white",font=("times new roman",20,"bold"),bg="crimson")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        self.search=ttk.Combobox(Detail_Frame,font=("times new roman",14,"bold"),state='readonly',justify=CENTER,width=10,textvariable=self.search_by)
        self.search['values']=("Select","roll_no","name","contact","gender")
        self.search.grid(row=0,column=1,pady=10,padx=20,sticky="w")
        self.search.current(0)
    
        txt_Search=Entry(Detail_Frame,font=("times new roman",14,"bold"),bd=5,relief=GROOVE,width=15,textvariable=self.search_txt)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        
        #Table Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)
        
        """ScrollBars"""
        scrolly=Scrollbar(Table_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Table_Frame,orient=HORIZONTAL)
        
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        
        
        
        """Student Table"""
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        """Headings"""
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        
        """Columns"""
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=200)
        self.Student_table.column("email",width=250)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=300)
        
        scrolly.config(command=self.Student_table.yview)
        scrollx.config(command=self.Student_table.xview)
        
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
    
        self.fetch_data()
    
    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s)",(
                                                                         self.Roll_no_var.get(),
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_address.get('1.0',END)
                                                                         ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
     
        
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("SELECT * FROM students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
        
        
    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("Select")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0',END)
        self.search_by.set("Select")
        self.search_txt.set("")
            
        
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])
        
        
    def update_data(self):
        if self.Roll_no_var.get()=='':
            messagebox.showerror("Error","Please Enter The Roll No Or Select The Data From the Right Side Table")
        
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("UPDATE students SET name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s WHERE roll_no=%s",(
                                                                                                                         self.name_var.get(),
                                                                                                                         self.email_var.get(),
                                                                                                                         self.gender_var.get(),
                                                                                                                         self.contact_var.get(),
                                                                                                                         self.dob_var.get(),
                                                                                                                         self.txt_address.get('1.0',END),
                                                                                                                         self.Roll_no_var.get()
                                                                                                                         ))
            con.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Updated","The Record Har Been Updated")
            con.close()
            
        
    def delete_data(self):
        if self.Roll_no_var.get()=='':
            messagebox.showerror("Error","Please Enter The Roll No Or Select The Data From the Right Side Table")
            
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("DELETE FROM students WHERE roll_no=%s",(self.Roll_no_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Deleted","The Record Har Been Deleted")
            con.close()
     
    
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("SELECT * FROM students WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
            self.clear()
        con.close()
        
        
        
        
        
    
root=Tk()
obj=Student_Management_System(root)
root.mainloop()    