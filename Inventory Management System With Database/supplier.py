from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg='white',bd=3,relief=GROOVE)
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)
        #=====Title======
        title=Label(self.root,text="Manage Supplier Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1070,height=35)

        #=====Variables=====
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()

        self.var_search=StringVar()
        #=====Widgets=====
        #=====Labels=====
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)

        lbl_name=Label(self.root,text="Supplier Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)

        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        #=====Entry Fields=====
        self.txt_supplier_invoice=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_sup_invoice)
        self.txt_supplier_invoice.place(x=150,y=60,width=200)

        txt_name=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_name).place(x=150,y=100,width=200)

        txt_contact=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_contact).place(x=150,y=140,width=200)

        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=470,height=180)

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
        lbl_search_supplierName=Label(self.root,text="Search By | Supplier Name : ",font=("goudy old style",15,"bold"),bg="white").place(x=650,y=60)

        self.txt_search_supplierName=Entry(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",textvariable=self.var_search)
        self.txt_search_supplierName.place(x=900,y=60,width=180)

        self.txt_search_supplierName.bind("<Key>",self.search)
        #=====Content=====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=650,y=100,width=430,height=340)
        
        #=====Scroll Bar=====
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        #=====TreeView=====
        self.SupplierTable=ttk.Treeview(self.C_Frame,columns=("sid","sup_invoice","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        #=====Scroll Bar=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        #=====TreeView Configrations=====
        self.SupplierTable.heading("sid",text="Supplier ID")
        self.SupplierTable.heading("sup_invoice",text="Invoice No.")
        self.SupplierTable.heading("name",text="Supplier Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("description",text="Description")

        self.SupplierTable['show']='headings'

        self.SupplierTable.column("sid",width=100)
        self.SupplierTable.column("sup_invoice",width=100)
        self.SupplierTable.column("name",width=120)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("description",width=150)        

        self.SupplierTable.pack(fill=BOTH,expand=1)

        #=====Binds=====
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        #=====Calls=====
        self.show()
#=================================================================================================
    def add(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice No Is Required",parent=self.root)
            
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier Invoice No Is Already Present",parent=self.root)
                else:
                    cur.execute("insert into supplier (invoice,name,contact,description) values (?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"The Supplier Added Successfully...The Name Of Supplier Is {str(self.var_name.get())}",parent=self.root)
                    self.show()
                    print(str(self.var_sup_invoice.get()))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def show(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier ")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def get_data(self,ev):
        self.txt_supplier_invoice.config(state='readonly')

        r=self.SupplierTable.focus()
        content=self.SupplierTable.item(r)
        row=content['values']
        
        self.var_sup_invoice.set(row[1])
        self.var_name.set(row[2])
        self.var_contact.set(row[3])

        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])
#=================================================================================================
    def update(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice ID Is Required",parent=self.root)
            
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select The Supplier From The List",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,description=? where invoice=?",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get('1.0',END),
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success",f"The Supplier Updated Successfully...The Name Of Supplier Invoice ID Is {str(self.var_sup_invoice.get())}",parent=self.root)
                    self.show()
                    print(str(self.var_sup_invoice.get()))
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def clear (self):
        self.show()
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_supplier_invoice.config(state=NORMAL)
#=================================================================================================
    def delete(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice ID Is Required",parent=self.root)
            
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select The Supplier From The List",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm",f"Are You Sure You Wnat To Delete {str(self.var_sup_invoice.get())} Supplier...")
                    if op == True:
                        cur.execute('delete from supplier where invoice=?',(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted",f"{str(self.var_sup_invoice.get())} has been deleted...",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}",parent=self.root)
#=================================================================================================
    def search(self,ev):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM supplier where name LIKE '%"+self.var_search.get()+"%'")
            row=cur.fetchall()
            if len(row)>0:
                self.SupplierTable.delete(*self.SupplierTable.get_children())
                for i in row:
                    self.SupplierTable.insert('',END,values=i)
            else:
                self.SupplierTable.delete(*self.SupplierTable.get_children())
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root) 
#=================================================================================================

if __name__ == "__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()
