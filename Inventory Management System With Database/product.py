from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg='white',bd=3,relief=GROOVE)
        self.root.focus_force()
        self.root.resizable(False,False)
        #=====Variables=====
        self.var_pid=StringVar()

        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        #=====Product Frame=====
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        product_Frame.place(x=10,y=10,width=450,height=480)
        #=====Title=====
        title=Label(product_Frame,text="Manange Product Details",font=('goudy old style',18),bg='#0f4d7d',fg='white').pack(side=TOP,fill=X)
        #=====Labels=====
        lbl_category=Label(product_Frame,text="Category",font=('goudy old style',18),bg='white').place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=('goudy old style',18),bg='white').place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=('goudy old style',18),bg='white').place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=('goudy old style',18),bg='white').place(x=30,y=210)
        lbl_qty=Label(product_Frame,text="Quantity",font=('goudy old style',18),bg='white').place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=('goudy old style',18),bg='white').place(x=30,y=310)
        #=====ComboBox=====
        cmb_cat=ttk.Combobox(product_Frame,values=self.cat_list,justify=CENTER,state='readonly',font=('goudy old style',15),textvariable=self.var_cat)
        cmb_cat.place(x=150,y=60,width=200) 
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,values=self.sup_list,justify=CENTER,state='readonly',font=('goudy old style',15),textvariable=self.var_sup)
        cmb_sup.place(x=150,y=110,width=200) 
        cmb_sup.current(0)

        cmb_status=ttk.Combobox(product_Frame,values=("Select","Active","Inactive"),justify=CENTER,state='readonly',font=('goudy old style',15),textvariable=self.var_status)
        cmb_status.place(x=150,y=310,width=200) 
        cmb_status.current(0)
        #=====Entry Fiels=====
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=('goudy old style',15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=('goudy old style',15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=('goudy old style',15),bg='lightyellow').place(x=150,y=260,width=200)
        #=====Button=====
        btn_add=Button(product_Frame,text="Add",font=('goudy old style',15),bg='#2196f3',fg="white",cursor="hand2",command=self.add).place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",font=('goudy old style',15),bg='#4caf50',fg="white",cursor="hand2",command=self.update).place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",font=('goudy old style',15),bg='#f44336',fg="white",cursor="hand2",command=self.delete).place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",font=('goudy old style',15),bg='#607d8b',fg="white",cursor="hand2",command=self.clear).place(x=340,y=400,width=100,height=40)
        #=====Search Frame=====
        SearchFrame=LabelFrame(self.root,text="Search Product",bg='white',font=('goudy old style',12,'bold'),bd=2,relief=RIDGE)
        SearchFrame.place(x=480,y=10,width=600,height=70)
        #=====Options=====
        lbl_search=Label(SearchFrame,text="Search By",font=('goudy old style',15),bg='white').place(x=10,y=10)

        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Category","Supplier","Name"),justify=CENTER,state='readonly',font=('goudy old style',15),textvariable=self.var_searchby)
        cmb_search.place(x=110,y=10,width=210) 
        cmb_search.current(0)

        self.txt_search=Entry(SearchFrame,font=('goudy old style',15),bg='lightyellow',bd=2,textvariable=self.var_searchtxt)
        self.txt_search.place(x=330,y=10,width=250)

        self.txt_search.bind("<Key>",self.search)
        #=====Product TreeView=====
        p_farme=Frame(self.root,bd=3,relief=RIDGE)
        p_farme.place(x=480,y=100,width=600,height=390)

        scrollx=Scrollbar(p_farme,orient=HORIZONTAL)
        scrolly=Scrollbar(p_farme,orient=VERTICAL)

        self.ProductTable=ttk.Treeview(p_farme,columns=("pid","Category","Supplier","name","price","qty","status"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading('pid',text="Pro ID")
        self.ProductTable.heading('Category',text="Category")
        self.ProductTable.heading('Supplier',text="Supplier")
        self.ProductTable.heading('name',text="Name")
        self.ProductTable.heading('price',text="Price")
        self.ProductTable.heading('qty',text="Quantity")
        self.ProductTable.heading('status',text="Status")

        self.ProductTable['show']='headings'

        self.ProductTable.column('pid',width=90)
        self.ProductTable.column('Category',width=100)
        self.ProductTable.column('Supplier',width=100)
        self.ProductTable.column('name',width=250)
        self.ProductTable.column('price',width=100)
        self.ProductTable.column('qty',width=100)
        self.ProductTable.column('status',width=100)
        
        self.ProductTable.pack(fill=BOTH,expand=1)
        #=====Binds=====
        self.ProductTable.bind('<ButtonRelease-1>',self.get_data)
        #=====Calls=====
        self.show()
        self.fetch_cat_sup()
#=================================================================================================
    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Empty":
                messagebox.showerror("Error",f"Please Select And Enter The Category, Supplier And Name Of The Product...Which Is Currently...\nCategory : {self.var_cat.get()}\nSupplier : {self.var_sup.get()}\nName : {self.var_name.get()}",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","The Product You Are Adding Is Already Present In The Database...}",parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values (?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Added",f"The Product Added Successfully...\nName : {str(self.var_name.get())}",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)
#=================================================================================================
    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)
#=================================================================================================
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
#=================================================================================================
    def update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select The Product To Update...",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",f"{self.var_pid.get()} Is Invalid product ID...Please Enter The Correct product ID...",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Added",f"product ID : {self.var_pid.get()}'s Data...\nIs Updated Successfully...")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)
#=================================================================================================
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Insert The product ID...",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",f"{self.var_pid.get()} Is Invalid product ID...Please Enter The Correct product ID...",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirmation",f"Are You Sure You Want To Delete The product...\nproduct ID : {self.var_pid.get()}\nName : {self.var_name.get()}")
                    if op == True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted",f"The Product ID {self.var_pid.get()} Deleted Successfully...")
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)        
#=================================================================================================
    def clear(self):
        self.var_pid.set("")
        self.var_name.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_price.set("")
        self.var_status.set("Select")
        self.var_qty.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
#=================================================================================================
    def search(self,ev):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            row=cur.fetchall()
            if len(row)>0:
                self.ProductTable.delete(*self.ProductTable.get_children())
                for i in row:
                    self.ProductTable.insert('',END,values=i)
            else:
                self.ProductTable.delete(*self.ProductTable.get_children())
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root)
#=================================================================================================
    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            #=====Category=====
            cur.execute("select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            self.sup_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            #=====Supplier=====
            cur.execute("select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root)
#=================================================================================================


if __name__ == "__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()