from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Student Details")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====Title======
        title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        #=====Variables=====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

        self.var_search=StringVar()
        #=====Widgets=====
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #COLUMN 1
        #=====Labels=====
        lbl_roll_no=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)

        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)

        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        #=====Entry Fields=====
        self.txt_roll=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_roll)
        self.txt_roll.place(x=150,y=60,width=200)

        txt_name=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_name).place(x=150,y=100,width=200)

        txt_email=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_email).place(x=150,y=140,width=200)

        self.txt_gender=ttk.Combobox(self.root,font=("goudy old style",15,"bold"),textvariable=self.var_gender,state='readonly',justify=CENTER,values=("Select","Male","Female","Other"))
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)

        txt_state=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_state).place(x=150,y=220,width=150)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #COLUMN 2
        #=====Labels=====
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)

        lbl_addmission=Label(self.root,text="Addmission",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=140)

        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)

        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=220)

        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=220)
        #=====Entry Fields=====
        self.course_list=['Select']
        self.fetch_course()
        
        self.txt_dob=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_dob).place(x=480,y=60,width=200)

        txt_contact=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_contact).place(x=480,y=100,width=200)

        txt_a_date=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_a_date).place(x=480,y=140,width=200)

        self.txt_course=ttk.Combobox(self.root,font=("goudy old style",15,"bold"),textvariable=self.var_course,state='readonly',justify=CENTER,values=self.course_list)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select")

        txt_city=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_city).place(x=380,y=220,width=100)

        txt_pin=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_pin).place(x=560,y=220,width=120)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #=================

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=260)

        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=260,width=500,height=100)

        #=====Buttons=====
        self.btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)

        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #=====Search Panel=====
        lbl_search_txt_roll=Label(self.root,text="Search By | Roll No : ",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)

        self.txt_search_roll=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_search)
        self.txt_search_roll.place(x=960,y=60,width=180)

        self.txt_search_roll.bind("<Key>",self.search)
        #=====Content=====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        
        #=====Scroll Bar=====
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        #=====TreeView=====
        self.StudentTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","addmission","course","state","city","pin","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        #=====Scroll Bar=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        #=====TreeView Configrations=====
        self.StudentTable.heading("roll",text="Roll No.")
        self.StudentTable.heading("name",text="Name")
        self.StudentTable.heading("email",text="EMail")
        self.StudentTable.heading("gender",text="Gender")
        self.StudentTable.heading("dob",text="D.O.B")
        self.StudentTable.heading("contact",text="Contact")
        self.StudentTable.heading("addmission",text="Addmission")
        self.StudentTable.heading("course",text="Course")
        self.StudentTable.heading("state",text="State")
        self.StudentTable.heading("city",text="City")
        self.StudentTable.heading("pin",text="Pin")
        self.StudentTable.heading("address",text="Address")

        self.StudentTable['show']='headings'

        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("email",width=200)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("contact",width=100)
        self.StudentTable.column("addmission",width=100)
        self.StudentTable.column("course",width=100)
        self.StudentTable.column("state",width=100)
        self.StudentTable.column("city",width=100)
        self.StudentTable.column("pin",width=100)
        self.StudentTable.column("address",width=200)       

        self.StudentTable.pack(fill=BOTH,expand=1)

        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)
        #=====Calls=====
        self.show()
#=================================================================================================
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number Is Required",parent=self.root)
            
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Roll Number Is Already Present",parent=self.root)
                else:
                    cur.execute("insert into student (roll,name,email,gender,dob,contact,addmission,course,state,city,pin,address) values (?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"The Student Added Successfully...The Name Of Student Is {str(self.var_name.get())}",parent=self.root)
                    self.show()
                    print(str(self.var_name.get()))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student ")
            rows=cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')

        r=self.StudentTable.focus()
        content=self.StudentTable.item(r)
        row=content['values']
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[11])
        
#=================================================================================================
    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No Is Required",parent=self.root)
            
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select The Student From The List",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,addmission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0',END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"The Student Delatis Updated Successfully...The Name Of Student Is {str(self.var_name.get())}",parent=self.root)
                    self.show()
                    print(str(self.var_roll.get()))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def clear (self):
        self.show()
        self.txt_roll.config(state=NORMAL)
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete('1.0',END)
        self.var_search.set("")
#=================================================================================================
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No Is Required",parent=self.root)
            
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select The Student From The List",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm",f"Are You Sure You Wnat To Delete {str(self.var_roll.get())} Roll No Student...")
                    if op == True:
                        cur.execute('delete from student where roll=?',(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted",f"{str(self.var_roll.get())} has been deleted...",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def search(self,ev):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM student where roll LIKE '%"+self.var_search.get()+"%'")
            row=cur.fetchall()
            if len(row)>0:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for i in row:
                    self.StudentTable.insert('',END,values=i)
            else:
                self.StudentTable.delete(*self.StudentTable.get_children())
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root) 
#=================================================================================================
    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course ")
            rows=cur.fetchall()
            v=[]
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
            print(v)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
if __name__ == "__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()
