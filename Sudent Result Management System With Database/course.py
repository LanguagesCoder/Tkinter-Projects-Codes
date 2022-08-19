from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Course Details")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====Title======
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        #=====Variables=====
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_search=StringVar()

        #=====Widgets=====
        #=====Labels=====
        lbl_curseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)

        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)

        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)

        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        #=====Entry Fields=====
        self.txt_courseName=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_course)
        self.txt_courseName.place(x=150,y=60,width=200)

        txt_duration=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_duration).place(x=150,y=100,width=200)

        txt_charges=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_charges).place(x=150,y=140,width=200)

        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=500,height=180)

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
        lbl_search_courseName=Label(self.root,text="Search By | Course Name : ",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)

        self.txt_search_courseName=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_search)
        self.txt_search_courseName.place(x=960,y=60,width=180)

        self.txt_search_courseName.bind("<Key>",self.search)
        #=====Content=====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        
        #=====Scroll Bar=====
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        #=====TreeView=====
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        #=====Scroll Bar=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        #=====TreeView Configrations=====
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Course Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")

        self.CourseTable['show']='headings'

        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=120)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)        

        self.CourseTable.pack(fill=BOTH,expand=1)

        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        #=====Calls=====
        self.show()
#=================================================================================================
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name Is Required",parent=self.root)
            
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Course Name Is Already Present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values (?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"The Course Added Successfully...The Name Of Course Is {str(self.var_course.get())}",parent=self.root)
                    self.show()
                    print(str(self.var_course.get()))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')

        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content['values']
        
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])

        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])
#=================================================================================================
    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name Is Required",parent=self.root)
            
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select The Course From The List",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get('1.0',END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"The Course Updated Successfully...The Name Of Course Is {str(self.var_course.get())}",parent=self.root)
                    self.show()
                    print(str(self.var_course.get()))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def clear (self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)
#=================================================================================================
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name Is Required",parent=self.root)
            
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select The Course From The List",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm",f"Are You Sure You Wnat To Delete {str(self.var_course.get())} course...")
                    if op == True:
                        cur.execute('delete from course where name=?',(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted",f"{str(self.var_course.get())} has been deleted...",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def search(self,ev):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM course where name LIKE '%"+self.var_search.get()+"%'")
            row=cur.fetchall()
            if len(row)>0:
                self.CourseTable.delete(*self.CourseTable.get_children())
                for i in row:
                    self.CourseTable.insert('',END,values=i)
            else:
                self.CourseTable.delete(*self.CourseTable.get_children())
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root) 
#=================================================================================================

if __name__ == "__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()
