from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg='white',bd=3,relief=GROOVE)
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)
        #=====Title======
        title=Label(self.root,text="Manage Product Category Details",font=("goudy old style",30,),bg="#184a54",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
        #=====Variables=====
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #=====Label And Entry Field=====
        title=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        title=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)
        #=====Button=====
        btn_add=Button(self.root,text="Add",font=('goudy old style',18),bg="#4caf50",fg="white",cursor="hand2",command=self.add).place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",font=('goudy old style',18),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=520,y=170,width=150,height=30)
        #=====TreeView Configrations
        #=====Content=====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=700,y=100,width=380,height=100)
        #=====Scroll Bar=====
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        #=====TreeView=====
        self.CategoryTable=ttk.Treeview(self.C_Frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        #=====Scroll Bar=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        #=====TreeView Configrations=====
        self.CategoryTable.heading("cid",text="Category ID")
        self.CategoryTable.heading("name",text="Name")

        self.CategoryTable['show']='headings'

        self.CategoryTable.column("cid",width=0)
        self.CategoryTable.column("name",width=100)
        
        self.CategoryTable.pack(fill=BOTH,expand=1)
        #=====Images=====
        self.image_1=Image.open("images/cat.jpg")
        self.image_1=self.image_1.resize((500,250),Image.ANTIALIAS)
        self.image_1=ImageTk.PhotoImage(self.image_1)

        self.lbl_image_1=Label(self.root,image=self.image_1,bd=2,relief=RAISED)
        self.lbl_image_1.place(x=50,y=220)

        self.image_2=Image.open("images/category.jpg")
        self.image_2=self.image_2.resize((500,250),Image.ANTIALIAS)
        self.image_2=ImageTk.PhotoImage(self.image_2)

        self.lbl_image_2=Label(self.root,image=self.image_2,bd=2,relief=RAISED)
        self.lbl_image_2.place(x=580,y=220)
        #=====Binds=====
        self.CategoryTable.bind('<ButtonRelease-1>',self.get_data)
        #=====Function Calls=====
        self.show()
#=================================================================================================
    def add(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name Is Required",parent=self.root)
            
            else:
                cur.execute("select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Category Is Already Present",parent=self.root)
                else:
                    cur.execute("insert into category (name) values (?)",(
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"The Category Added Successfully...The Name Of Category Is {str(self.var_name.get())}",parent=self.root)
                    self.show()
                    print(str(self.var_cat_id.get()))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def show(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from category ")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def get_data(self,ev):
        r=self.CategoryTable.focus()
        content=self.CategoryTable.item(r)
        row=content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
#=================================================================================================
    def delete(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Category Name Is Required",parent=self.root)
            
            else:
                cur.execute("select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select The Category From The List",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm",f"Are You Sure You Wnat To Delete {str(self.var_name.get())} Category...")
                    if op == True:
                        cur.execute('delete from category where cid=?',(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted",f"{str(self.var_name.get())} Category has been deleted...",parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def clear (self):
        self.show()
        self.var_cat_id.set("")
        self.var_name.set("")
#=================================================================================================


        


if __name__ == "__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()