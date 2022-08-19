from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg='white',bd=3,relief=GROOVE)
        self.root.focus_force()
        self.root.resizable(False,False)
        #=====Variables=====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()

        self.var_salary=StringVar()
        #=====Search Frame=====
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg='white',font=('goudy old style',12,'bold'),bd=2,relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        #=====Options=====
        lbl_search=Label(SearchFrame,text="Search By",font=('goudy old style',15),bg='white').place(x=10,y=10)

        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"),justify=CENTER,state='readonly',font=('goudy old style',15),textvariable=self.var_searchby)
        cmb_search.place(x=120,y=10,width=200) 
        cmb_search.current(0)

        self.txt_search=Entry(SearchFrame,font=('goudy old style',15),bg='lightyellow',bd=2,textvariable=self.var_searchtxt)
        self.txt_search.place(x=370,y=10,width=200)

        self.txt_search.bind("<Key>",self.search)
        #=====Title=====
        title=Label(self.root,text="Employee Details",font=('goudy old style',15),bg='#0f4d7d',fg="white").place(x=50,y=100,width=1000)
        #=====Content=====
        #===Row 1===
        lbl_empid=Label(self.root,text="Emp ID",font=('goudy old style',15),bg='white').place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=('goudy old style',15),bg='white').place(x=350,y=150)
        lbl_contact=Label(self.root,text="Conatact",font=('goudy old style',15),bg='white').place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=('goudy old style',15),bg='lightyellow').place(x=150,y=150,width=180)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,font=('goudy old style',15),bg='lightyellow').place(x=500,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15),bg='lightyellow').place(x=850,y=150,width=180)

        cmb_gender=ttk.Combobox(self.root,values=("Select","Male","Female","Other"),justify=CENTER,state='readonly',font=('goudy old style',15),textvariable=self.var_gender)
        cmb_gender.place(x=500,y=150,width=180) 
        cmb_gender.current(0)
        #===Row 2===
        lbl_name=Label(self.root,text="Name",font=('goudy old style',15),bg='white').place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=('goudy old style',15),bg='white').place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=('goudy old style',15),bg='white').place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15),bg='lightyellow').place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=('goudy old style',15),bg='lightyellow').place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=('goudy old style',15),bg='lightyellow').place(x=850,y=190,width=180)
        #===Row 3===
        lbl_email=Label(self.root,text="EMail",font=('goudy old style',15),bg='white').place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=('goudy old style',15),bg='white').place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=('goudy old style',15),bg='white').place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=('goudy old style',15),bg='lightyellow').place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=('goudy old style',15),bg='lightyellow').place(x=500,y=230,width=180)
        #txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15),bg='lightyellow').place(x=850,y=230,width=180)

        cmb_utype=ttk.Combobox(self.root,values=("Select","Admin","Employee"),justify=CENTER,state='readonly',font=('goudy old style',15),textvariable=self.var_utype)
        cmb_utype.place(x=850,y=230,width=180) 
        cmb_utype.current(0)
        #===Row 4===
        lbl_address=Label(self.root,text="Address",font=('goudy old style',15),bg='white').place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=('goudy old style',15),bg='white').place(x=500,y=270)
        
        self.txt_address=Text(self.root,font=('goudy old style',15),bg='lightyellow')
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=('goudy old style',15),bg='lightyellow').place(x=600,y=270,width=180)
        #=====Button=====
        btn_add=Button(self.root,text="Add",font=('goudy old style',15),bg='#2196f3',fg="white",cursor="hand2",command=self.add).place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",font=('goudy old style',15),bg='#4caf50',fg="white",cursor="hand2",command=self.update).place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",font=('goudy old style',15),bg='#f44336',fg="white",cursor="hand2",command=self.delete).place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",font=('goudy old style',15),bg='#607d8b',fg="white",cursor="hand2",command=self.clear).place(x=860,y=305,width=110,height=28)
        #=====Employee TreeView=====
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading('eid',text="Emp ID")
        self.EmployeeTable.heading('name',text="Name")
        self.EmployeeTable.heading('email',text="EMail")
        self.EmployeeTable.heading('gender',text="Gender")
        self.EmployeeTable.heading('contact',text="Contact")
        self.EmployeeTable.heading('dob',text="D.O.B")
        self.EmployeeTable.heading('doj',text="D.O.J")
        self.EmployeeTable.heading('pass',text="Password")
        self.EmployeeTable.heading('utype',text="User Type")
        self.EmployeeTable.heading('address',text="Address")
        self.EmployeeTable.heading('salary',text="Salary")

        self.EmployeeTable['show']='headings'

        self.EmployeeTable.column('eid',width=90)
        self.EmployeeTable.column('name',width=100)
        self.EmployeeTable.column('email',width=250)
        self.EmployeeTable.column('gender',width=100)
        self.EmployeeTable.column('contact',width=100)
        self.EmployeeTable.column('dob',width=70)
        self.EmployeeTable.column('doj',width=70)
        self.EmployeeTable.column('pass',width=100)
        self.EmployeeTable.column('utype',width=100)
        self.EmployeeTable.column('address',width=250)
        self.EmployeeTable.column('salary',width=100)
        
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        
        #=====Calls=====
        self.show()
        #=====Bins=====
        self.EmployeeTable.bind('<ButtonRelease-1>',self.get_data)
#=================================================================================================
    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Please Insert The Employee ID...",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","The Employee ID You Are Adding Is Already Present In The Database...}",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values (?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Added",f"The Employee Added Successfully...\nEmployee ID : {str(self.var_emp_id.get())}\nName : {str(self.var_name.get())}\nUser Type : {str(self.var_utype.get())}",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)
#=================================================================================================
    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)
#=================================================================================================
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])
#=================================================================================================
    def update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Please Insert The Employee ID...",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",f"{self.var_emp_id.get()} Is Invalid Employee ID...Please Enter The Correct Employee ID...",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Added",f"Employee ID : {self.var_emp_id.get()}'s Data...\nIs Updated Successfully...")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)
#=================================================================================================
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Please Insert The Employee ID...",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",f"{self.var_emp_id.get()} Is Invalid Employee ID...Please Enter The Correct Employee ID...",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirmation",f"Are You Sure You Want To Delete The Employee...\nEmployee ID : {self.var_emp_id.get()}\nName : {self.var_name.get()}")
                    if op == True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted",f"The Employee ID {self.var_emp_id.get()} Deleted Successfully...")
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)        
#=================================================================================================
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
#=================================================================================================
    def search(self,ev):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            row=cur.fetchall()
            if len(row)>0:
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for i in row:
                    self.EmployeeTable.insert('',END,values=i)
            else:
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root)
#=================================================================================================
        
        

if __name__ == "__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()