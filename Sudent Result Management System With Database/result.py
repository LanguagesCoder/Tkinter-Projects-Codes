from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Add Student Result Details")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====Title======
        title=Label(self.root,text="Add Student Result Details",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)
        #=====Variables=====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        #=====Widgets=====
        #=====Labels=====
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)
        #=====ComboBox=====
        self.roll_list=['Select']
        self.fetch_course()

        self.txt_course=ttk.Combobox(self.root,font=("goudy old style",15,"bold"),textvariable=self.var_roll,state='readonly',justify=CENTER,values=self.roll_list)
        self.txt_course.place(x=280,y=100,width=210)
        self.txt_course.current(0)

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg='#03a9f4',fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=100,height=30)
        #=====Entry Fields=====
        txt_name=Entry(self.root,font=("goudy old style",20,"bold"),bg="lightyellow",textvariable=self.var_name,state='readonly').place(x=280,y=160,width=300)
        txt_course=Entry(self.root,font=("goudy old style",20,"bold"),bg="lightyellow",textvariable=self.var_course,state='readonly').place(x=280,y=220,width=300)
        txt_marks_ob=Entry(self.root,font=("goudy old style",20,"bold"),bg="lightyellow",textvariable=self.var_marks).place(x=280,y=280,width=300)
        txt_full_marks=Entry(self.root,font=("goudy old style",20,"bold"),bg="lightyellow",textvariable=self.var_full_marks).place(x=280,y=340,width=300)
        #=====Button=====
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_aclear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
        #=====Side Image=====
        self.bg_img=Image.open("images/result.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)
        #=====Calls=====
#=================================================================================================
    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student ")
            rows=cur.fetchall()
            v=[]
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
            print(v)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT name,course FROM student where roll LIKE '%"+self.var_roll.get()+"%'")
            row=cur.fetchone()
            if len(row)>0:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No Record",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root) 
#=================================================================================================
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please Select The Student",parent=self.root)
            
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Result Is Already Present",parent=self.root)
                else:
                    per=round((int(self.var_marks.get())/int(self.var_full_marks.get()))*100,2)
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values (?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"Result Added Successfully...The Name Of Student Is {str(self.var_name.get())}",parent=self.root)
                    print(str(per))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
#=================================================================================================



if __name__ == "__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()