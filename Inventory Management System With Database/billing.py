""""•"""
#=====Library Imports=====
import os
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import tempfile
class billClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg='white',bd=3,relief=GROOVE)
        #=====Variables=====        
        self.var_search=StringVar()
        
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        self.cart_list=[]

        self.chk_print=0
        #=====Calculator Frame
        self.var_cal_input=StringVar()
        #=====Images=====
        self.icon_title=PhotoImage(file='images/logo1.png')

        self.MenuLogo=Image.open('images/menu_im.png')
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        self.icon_side=PhotoImage(file='images/side.png')
        #=====Title=====
        title=Label(self.root,text="Inventory Management System",font=('times new roman',40,'bold'),bg='#010c48',fg='white',anchor='w',padx=20,image=self.icon_title,compound=LEFT).place(x=0,y=0,relwidth=1,height=70)
        #=====Button Logout=====
        btn_logout=Button(self.root,text="Logout",font=('times new roman',15,'bold'),bg='yellow',cursor='hand2',command=self.logout).place(x=1150,y=10,height=50,width=150)
        #=====Time And Date Bar=====
        self.lbl_clock=Label(self.root,text="Welcome To Inventory Management System\t\tDate:DD/MM/YYYY\t\tTime:HH-MM-SS",font=('times new roman',15),bg='#4d636d',fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #=====Product Frame 1=====
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=('goudy old style',20,'bold'),bg='#262626',fg='white').pack(side=TOP,fill=X)
        #=====Product Frame 2=====
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg='white')
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=('times new roman',15,'bold'),bg='white',fg='green').place(x=2,y=5)
        btn_show_all=Button(ProductFrame2,text="Show All",font=('goudy old style',15),bg='#083531',fg='white',cursor='hand2',command=self.show).place(x=285,y=10,width=100,height=25)

        lbl_search=Label(ProductFrame2,text="Product Name",font=('times new roman',15,'bold'),bg='white').place(x=5,y=45)
        self.txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=('times new roman',15),bg='lightyellow')
        self.txt_search.place(x=135,y=48,width=250,height=22)
        
        self.txt_search.bind("<Key>",self.search)
        #=====Product Frame 3=====
        ProductFrame3=Frame(ProductFrame1,bd=2,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)
        
        #=====Scroll Bar=====
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        #=====TreeView=====
        self.ProductTable=ttk.Treeview(ProductFrame3,columns=("pid","name","qty","price","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        #=====Scroll Bar=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        #=====TreeView Configrations=====
        self.ProductTable.heading("pid",text="P ID")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("status",text="Status")

        self.ProductTable['show']='headings'

        self.ProductTable.column("pid",width=50)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("qty",width=60)
        self.ProductTable.column("price",width=70)
        self.ProductTable.column("status",width=100)        
        self.ProductTable.pack(fill=BOTH,expand=1)
        #=====Note=====
        lbl_note=Label(ProductFrame1,text="Note : 'Enter 0 Quantity To Remove Product From The Cart'",font=('goudy old style',12),bg='white',fg='red',anchor='w').pack(side=BOTTOM,fill=X)
        #=====Customer Frame=====
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=('goudy old style',15),bg='lightgray').pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame,text="Name",font=('times new roman',15),bg='white').place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=('times new roman',13),bg='lightyellow').place(x=80,y=35,width=180)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=('times new roman',15),bg='white').place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=('times new roman',13),bg='lightyellow').place(x=380,y=35,width=140)
        
        #=====Calculator And Cart Frame=====
        Cal_Cart_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=320)
        #=====Calculator Frame=====
        Cal_Frame=Frame(Cal_Cart_Frame,bd=4,relief=RIDGE,bg='white')
        Cal_Frame.place(x=5,y=10,width=252,height=300)

        self.var_operator=''
        def btn_click (num):
            self.var_operator=self.var_operator+str(num)
            self.var_cal_input.set(self.var_operator)
        
        def result():
            res=str(eval(self.var_operator))
            self.var_cal_input.set(res)
            self.var_operator=''
           
        def cal_clear():
            self.var_cal_input.set('')
            self.var_operator=''
        
        self.txt_cal_input=Entry(Cal_Frame,bg="lightgray",state=DISABLED,font=("times new roman",25,"bold"),justify=RIGHT,textvariable=self.var_cal_input,fg="black")
        self.txt_cal_input.place(x=0,y=0,relwidth=1,height=50)

        """Row 1"""
        btn_7=Button(Cal_Frame,text="7",font=("times new roman",15,"bold"),command=lambda:btn_click(7)).place(x=0,y=52,widt=60,height=60)
        btn_8=Button(Cal_Frame,text="8",font=("times new roman",15,"bold"),command=lambda:btn_click(8)).place(x=61,y=52,widt=60,height=60)
        btn_9=Button(Cal_Frame,text="9",font=("times new roman",15,"bold"),command=lambda:btn_click(9)).place(x=122,y=52,widt=60,height=60)
        btn_div=Button(Cal_Frame,text="/",font=("times new roman",15,"bold"),command=lambda:btn_click('/')).place(x=183,y=52,widt=60,height=60)
        
        """Row 2"""
        btn_4=Button(Cal_Frame,text="4",font=("times new roman",15,"bold"),command=lambda:btn_click(4)).place(x=0,y=112,widt=60,height=60)
        btn_5=Button(Cal_Frame,text="5",font=("times new roman",15,"bold"),command=lambda:btn_click(5)).place(x=61,y=112,widt=60,height=60)
        btn_6=Button(Cal_Frame,text="6",font=("times new roman",15,"bold"),command=lambda:btn_click(6)).place(x=122,y=112,widt=60,height=60)
        btn_mul=Button(Cal_Frame,text="*",font=("times new roman",15,"bold"),command=lambda:btn_click('*')).place(x=183,y=112,widt=60,height=60)
        
        """Row 3"""
        btn_1=Button(Cal_Frame,text="1",font=("times new roman",15,"bold"),command=lambda:btn_click(1)).place(x=0,y=172,widt=60,height=60)
        btn_2=Button(Cal_Frame,text="2",font=("times new roman",15,"bold"),command=lambda:btn_click(2)).place(x=61,y=172,widt=60,height=60)
        btn_3=Button(Cal_Frame,text="3",font=("times new roman",15,"bold"),command=lambda:btn_click(3)).place(x=122,y=172,widt=60,height=60)
        btn_min=Button(Cal_Frame,text="-",font=("times new roman",15,"bold"),command=lambda:btn_click('-')).place(x=183,y=172,widt=60,height=60)
        
        """Row 4"""
        btn_0=Button(Cal_Frame,text="0",font=("times new roman",15,"bold"),command=lambda:btn_click(0)).place(x=0,y=233,widt=60,height=60)
        btn_dot=Button(Cal_Frame,text="C",font=("times new roman",15,"bold"),command=cal_clear).place(x=61,y=233,widt=60,height=60)
        btn_add=Button(Cal_Frame,text="+",font=("times new roman",15,"bold"),command=lambda:btn_click('+')).place(x=122,y=233,widt=60,height=60)
        btn_equal=Button(Cal_Frame,text="=",font=("times new roman",15,"bold"),command=result).place(x=183,y=233,widt=60,height=60)
        #=====Cart Frame=====
        CartFrame=Frame(Cal_Cart_Frame,bd=2,relief=RIDGE)
        CartFrame.place(x=260,y=8,width=250,height=300)
        
        self.cartTitle=Label(CartFrame,text="Cart \t Total Product : [ 0 ]",font=('goudy old style',15),bg='lightgray')
        self.cartTitle.pack(side=TOP,fill=X)
        #=====Scroll Bar=====
        scrolly=Scrollbar(CartFrame,orient=VERTICAL)
        scrollx=Scrollbar(CartFrame,orient=HORIZONTAL)

        #=====TreeView=====
        self.CartTable=ttk.Treeview(CartFrame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        #=====Scroll Bar=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        #=====TreeView Configrations=====
        self.CartTable.heading("pid",text="P ID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="Quantity")

        self.CartTable['show']='headings'

        self.CartTable.column("pid",width=50)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=60)
        self.CartTable.column("qty",width=60)
        self.CartTable.pack(fill=BOTH,expand=1)

        #=====Add Cart Widgets Frame=====
        Add_CartWidgetsFrame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Add_CartWidgetsFrame.place(x=420,y=515,width=530,height=145)

        #=====Labels And Entry Fields=====
        lbl_p_name=Label(Add_CartWidgetsFrame,text='Product Name',font=('times new roman',15),bg='white').place(x=5,y=5)       
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=('times new roman',15),bg='lightyellow',state='readonly').place(x=5,y=35,width=225,height=22)
        
        lbl_p_price=Label(Add_CartWidgetsFrame,text='Price Per Qty',font=('times new roman',15),bg='white').place(x=5,y=70)       
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=('times new roman',15),bg='lightyellow',state='readonly').place(x=5,y=100,width=150,height=22)
        
        lbl_p_qty=Label(Add_CartWidgetsFrame,text='Quantity',font=('times new roman',15),bg='white').place(x=275,y=5)       
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=('times new roman',15),bg='lightyellow',state=NORMAL).place(x=275,y=35,width=225,height=22)
        
        self.lbl_instock=Label(Add_CartWidgetsFrame,text='In Stock : [ 0 ]',font=('times new roman',15),bg='white')
        self.lbl_instock.place(x=170,y=80)       
        #=====Buttons
        btn_clear_cart=Button(Add_CartWidgetsFrame,text='Clear',font=('times new roman',15,'bold'),bg='lightgray',cursor='hand2',command=self.clear_cart).place(x=370,y=105,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text='Add | Update',font=('times new roman',15,'bold'),bg='orange',cursor='hand2',command=self.add_update_cart).place(x=370,y=70,width=150,height=30)

        #=====Billing Frame=====
        BillingFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        BillingFrame.place(x=953,y=110,width=400,height=410)

        bTitle=Label(BillingFrame,text="Customer Billing Area",font=('goudy old style',20,'bold'),bg='#f44336',fg='white').pack(side=TOP,fill=X)

        scrolly=Scrollbar(BillingFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(BillingFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)

        scrolly.config(command=self.txt_bill_area.yview)

        #=====Billing Menu Frame=====
        BillingMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        BillingMenuFrame.place(x=953,y=520,width=400,height=140)
        #=====Labels=====
        self.lbl_amnt=Label(BillingMenuFrame,text="Bill Amount\nRs.0",font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white')
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(BillingMenuFrame,text="Discount\n5%",font=('goudy old style',15,'bold'),bg='#8bc34a',fg='white')
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(BillingMenuFrame,text="Net Pay\nRs.0",font=('goudy old style',15,'bold'),bg='#607d8b',fg='white')
        self.lbl_net_pay.place(x=246,y=5,width=148,height=70)
        #=====Buttons
        btn_print=Button(BillingMenuFrame,text="Print",font=('goudy old style',15,'bold'),bg='lightgreen',fg='white',cursor='hand2',command=self.print_bill).place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(BillingMenuFrame,text="Clear",font=('goudy old style',15,'bold'),bg='gray',fg='white',cursor='hand2',command=self.clear_all).place(x=124,y=80,width=120,height=50)

        btn_generate=Button(BillingMenuFrame,text="Generate\nSave Bill",font=('goudy old style',15,'bold'),bg='#009688',fg='white',cursor='hand2',command=self.generate_bill).place(x=246,y=80,width=148,height=50)
        #=====Footer=====
        lbl_fottor=Label(self.root,text="IMS-Inventory Management System...For Any Technical Issues Call-987xxxx321",font=('times new roman',15),bg='#4d636d',fg='white').pack(side=BOTTOM,fill=X)
        #=====Binds=====
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.CartTable.bind('<ButtonRelease-1>',self.get_data_cart)
        #=====Calls=====
        self.show()
        self.update_date_time()
        #=====Defining Variables=====
        self.var_cname.set('Durgesh Kavate')
        self.var_contact.set('+91 9307739060')
#=================================================================================================
    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select pid,name,qty,price,status from product where status='Active'")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To : {str(ex)}...",parent=self.root)
#=================================================================================================
    def search(self,ev):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT pid,name,qty,price,status FROM product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
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
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.lbl_instock.config(text=f'In Stock : [ {str(row[2])} ]')
        self.var_price.set(row[3])
        self.var_stock.set(row[2])
        self.var_qty.set('1')
#=================================================================================================
    def add_update_cart(self):
        if self.var_qty.get()=='':
            messagebox.showerror('Error','Please Enter The Quantity Of The Product You Want...',parent=self.root)
        elif self.var_pid.get()=='':
            messagebox.showerror('Error','Please Select The Product...',parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error','Please Select The Valid Quantity Of The Product...',parent=self.root)
        else:
            #price_cal=int(self.var_qty.get())*float(self.var_price.get())
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            #=====Update Cart=====
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present == 'yes':
                op=messagebox.askyesno('Same Product','Product Is Already Present In The Cart\nYou Want To Delete It Or You HAve To Update It...',parent=self.root)
                if op ==True:
                    if self.var_qty.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()
#=================================================================================================
    def show_cart (self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f'Error Due To : {str(ex)}',parent=self.root)
#=================================================================================================
    def bill_updates(self):
        self.bill_amnt=0
        self.netpay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+float(row[2])*int(row[3])
        self.discount=(self.bill_amnt*5)/100

        self.netpay=self.bill_amnt-self.discount

        self.lbl_amnt.config(text=f'Bill Amount\nRs.{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\nRs.{str(self.netpay)}')
        self.cartTitle.config(text=f'Cart \t Total Product : [ {str(len(self.cart_list))} ]')
#=================================================================================================
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f'In Stock : [ {str(row[4])} ]')
        self.var_stock.set(row[4])
        self.var_qty.set('1')

#=================================================================================================
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror('Error','Please Enter You Name And Contact No...',parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror('Error','Please Select The Product...',parent=self.root)
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()

            messagebox.showinfo('Saved',f'The Bill Is Saved In Backend...\nInvoice No : {self.invoice}\nFile Name : {self.invoice}.txt')
            self.chk_print=1
#=================================================================================================
    def bill_top(self):
        self.invoice=int(time.strftime('%H%M%S'))+int(time.strftime('%d%m%Y'))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No.98725*****, Delhi-125001
{str('='*46)}
 Customer Name : {self.var_cname.get()}
 Phone No : {self.var_contact.get()}
 Bill No : {str(self.invoice)}\t\t\tDate : {str(time.strftime('%d/%m/%Y'))}
{str('='*46)}
 Product Name\t\t\tQTY\tPrice
{str('='*46)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
#=================================================================================================
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str('='*46)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.netpay}
{str('='*46)}
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
#=================================================================================================
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                name=row[1]
                qty=int(row[4])-int(row[3])
                pid=row[0]

                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'

                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                cur.execute('Update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid,
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To:{str(ex)}",parent=self.root)
#=================================================================================================
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f'In Stock : [ 0 ]')
        self.var_stock.set('')
#=================================================================================================
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.var_search.set('')

        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text='Cart \t Total Product : [ 0 ]')

        self.clear_cart()
        self.show()
        self.show_cart()

        self.chk_print=0
#=================================================================================================
    def update_date_time(self):
        time_= time.strftime('%I:%M:%S')
        date_= time.strftime('%d-%m-%Y')
        self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\tDate:{str(date_)}\t\tTime:{str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
#=================================================================================================
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Printing','Please Wait While Printing The Bill',parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Printing Error','Please Generte The Bill...To Print The Bill',parent=self.root)
#=================================================================================================
    def logout(self):
        self.root.destroy()
        os.system('python login.py')
#=================================================================================================

if __name__ == "__main__":
    root=Tk()
    obj=billClass(root)
    root.mainloop()