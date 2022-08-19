from tkinter import*
from tkinter import ttk
import time
import os

class GUI_SOFTWARE:
    def __init__(self):
        """SETTING WINDOW"""
        self.root=Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")
        
        """TITLE OF THE WINDOW"""
        title = Label(self.root,text="File Based Record System",font=("times new roman",35,"bold"),bd=10,relief=GROOVE,pady=10).pack(fill=X)
        """ALL VARIABLES"""
        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()
    
        """STUDENT FRAME"""
        F1=Frame(self.root,bd=10,relief=GROOVE)
        F1.place(x=0,y=100,height=420)
        stitle = Label(F1,text="Student Details",font=("times new roman",30,"bold")).grid(row=0,columnspan=4)
        
        """STUDENT ID AND CONTACT NUMBER"""
        stud_id=Label(F1,text="Student Id :",font=("arial",15,"bold")).grid(row=1,column=0,padx=20,pady=20)   
        txt_stud_id=Entry(F1,bd=7,relief=GROOVE,width=22,font=("arial",15,"bold"),textvariable=self.s_id).grid(row=1,column=1,pady=10,padx=10)
        
        stud_contact=Label(F1,text="Contact :",font=("arial",15,"bold")).grid(row=1,column=2,padx=20,pady=20)   
        txt_stud_contact=Entry(F1,bd=7,relief=GROOVE,width=22,font=("arial",15,"bold"),textvariable=self.contact).grid(row=1,column=3,pady=10,padx=10)
        
        
        """STUDENT NAME AND DATE OF BIRTH"""
        stud_name=Label(F1,text="Name :",font=("arial",15,"bold")).grid(row=2,column=0,padx=20,pady=20)   
        txt_stud_name=Entry(F1,bd=7,relief=GROOVE,width=22,font=("arial",15,"bold"),textvariable=self.name).grid(row=2,column=1,pady=10,padx=10)
        
        stud_dob=Label(F1,text="D.O.B :",font=("arial",15,"bold")).grid(row=2,column=2,padx=20,pady=20)   
        txt_stud_dob=Entry(F1,bd=7,relief=GROOVE,width=22,font=("arial",15,"bold"),textvariable=self.date).grid(row=2,column=3,pady=10,padx=10)
        
        
        """COURSE AND DEGREE"""
        stud_course=Label(F1,text="Course :",font=("arial",15,"bold")).grid(row=3,column=0,padx=20,pady=20)   
        txt_stud_course=Entry(F1,bd=7,relief=GROOVE,width=22,font=("arial",15,"bold"),textvariable=self.course).grid(row=3,column=1,pady=10,padx=10)
        
        stud_degree=Label(F1,text="Degree :",font=("arial",15,"bold")).grid(row=3,column=2,padx=20,pady=20)   
        combo_degree=ttk.Combobox(F1,width=20,state="readonly",font=("arial",15,"bold"),justify=CENTER,textvariable=self.degree)
        combo_degree['values']=("Select","BCA","MAC","Btech","MBA","Mtech")
        combo_degree.grid(row=3,column=3,pady=10,padx=10)
        combo_degree.current(0)
        
        """ADDRESS AND ID PROOF"""
        stud_address=Label(F1,text="Address :",font=("arial",15,"bold")).grid(row=4,column=0,padx=20,pady=20)   
        txt_stud_address=Entry(F1,bd=7,relief=GROOVE,width=22,font=("arial",15,"bold"),textvariable=self.address).grid(row=4,column=1,pady=10,padx=10)
        
        stud_proof=Label(F1,text="ID Proof :",font=("arial",15,"bold")).grid(row=4,column=2,padx=20,pady=20)   
        combo_proof=ttk.Combobox(F1,width=20,state="readonly",font=("arial",15,"bold"),justify=CENTER,textvariable=self.proof)
        combo_proof['values']=("Select","Pass Port","Pan Card","Driving License")
        combo_proof.grid(row=4,column=3,pady=10,padx=10)
        combo_proof.current(0)
        
        """CITY AND PAYMENT MODE"""
        stud_city=Label(F1,text="City :",font=("arial",15,"bold")).grid(row=5,column=0,padx=20,pady=20)   
        txt_stud_city=Entry(F1,bd=7,relief=GROOVE,width=22,font=("arial",15,"bold"),textvariable=self.city).grid(row=5,column=1,pady=10,padx=10)
        
        stud_payment=Label(F1,text="Payment Mode :",font=("arial",15,"bold")).grid(row=5,column=2,padx=20,pady=20)   
        combo_payment=ttk.Combobox(F1,width=20,state="readonly",font=("arial",15,"bold"),justify=CENTER,textvariable=self.payment)
        combo_payment['values']=("Select","Cash","Chaque","NEFT","Net Banking")
        combo_payment.grid(row=5,column=3,pady=10,padx=10)
        combo_payment.current(0)
        
        """BUTTON FRAME"""
        F2=Frame(self.root,bd=10,relief=GROOVE)
        F2.place(x=0,y=520)
        
        btnsave=Button(F2,text="Save",font=("arial",15,"bold"),bd=7,width=18,command=self.save_data).grid(row=0,column=0,padx=12,pady=10)
        btndelete=Button(F2,text="Delete",font=("arial",15,"bold"),bd=7,width=18,command=self.delete).grid(row=0,column=1,padx=12,pady=10)
        btnclear=Button(F2,text="Clear",font=("arial",15,"bold"),bd=7,width=18,command=self.clear).grid(row=0,column=2,padx=12,pady=10)
        btnlog=Button(F2,text="Logout",font=("arial",15,"bold"),bd=7,width=18,command=self.logout).grid(row=0,column=3,padx=12,pady=10)
        btnexit=Button(F2,text="Exit",font=("arial",15,"bold"),bd=7,width=18,command=self.exit_fun).grid(row=0,column=4,padx=12,pady=10)
        
        """FILE FRAME"""
        F3=Frame(self.root,bd=10,relief=GROOVE)
        F3.place(x=930,y=100,width=400,height=420)
        f3title=Label(F3,text="All Files",font=("times new roman",20,"bold"),bd=5,relief=GROOVE).pack(side=TOP,fill=X)
        
        scroll_y = Scrollbar(F3,orient=VERTICAL)
        self.file_list=Listbox(F3,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        root.mainloop()
    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student Id Is requires")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present = "yes"
                if present == "yes":
                    ask=messagebox.askyesno("Update","File Alredy Exist\nDo You Want To Update This File")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record Has Been Updated Sucessfully")
                        self.show_files()
                        self.clear()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved","Record Has Been Saved Sucessfully")
                    self.show_files()
            else:
                self.save_file()
                messagebox.showinfo("Saved","Record Has Been Saved Sucessfully")
                self.show_files()
            
    def save_file(self):
        f=open("files/"+str(self.s_id.get())+".txt","w")
        f.write(
            str(self.s_id.get())+","+
            str(self.name.get())+","+
            str(self.course.get())+","+
            str(self.address.get())+","+
            str(self.city.get())+","+
            str(self.contact.get())+","+
            str(self.date.get())+","+
            str(self.degree.get())+","+
            str(self.proof.get())+","+
            str(self.payment.get())
               )
       
        f.close()
    
    def show_files(self):
        files=os.listdir("files/")       
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)
        
    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        #print(self.file_list.get(get_cursor))        
        f1=open("files/"+self.file_list.get(get_cursor))
        for f in f1:
            value=f.split(",")
        
            
        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])

    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")                

    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student Id Is requires")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present = "yes"
                if present == "yes":
                    ask=messagebox.askyesno("Delete","Are You Sure To Delete Your\nselected File")
                    if ask>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Sucess","File Deleted Sucessfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error","File Not Found")
                        
    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Are You Sure To Exit ")
        if ask>0:
            self.root.destroy()                
    
    def logout(self):
        self.root.destroy()
        import login_page                
                    
                    
                    
                        

               