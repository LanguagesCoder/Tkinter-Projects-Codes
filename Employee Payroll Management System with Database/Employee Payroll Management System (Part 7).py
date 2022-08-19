from tkinter import*
from tkinter import messagebox
import pymysql

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Manangement System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Manangement System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #=============Variables
        self.var_emp_code=StringVar()   
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_experience=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar() #Adhaar Card
        self.var_contact=StringVar()
        self.var_status=StringVar()
        
        #=============Frame 1
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        
        title2=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        """Row 1"""
        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        txt_code=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_emp_code).place(x=220,y=74,width=200)
        btn_search=Button(Frame1,text="Search",font=("times new roman",20),bg="gray",fg="black").place(x=440,y=72,height=30)
        
        """Row 2"""
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black").place(x=10,y=120)
        txt_designation=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_designation).place(x=170,y=125,width=200)
        
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black").place(x=390,y=120)
        txt_dob=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_dob).place(x=520,y=125,width=200)
        
        """Row 3"""
        lbl_name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black").place(x=10,y=170)
        txt_name=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_name).place(x=170,y=175,width=200)
        
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black").place(x=390,y=170)
        txt_doj=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_doj).place(x=520,y=175,width=200)
        
        """Row 4"""
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_age).place(x=170,y=225,width=200)
        
        lbl_experince=Label(Frame1,text="Experience",font=("times new roman",20),bg="white",fg="black").place(x=390,y=220)
        txt_experince=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_experience).place(x=520,y=225,width=200)
        
        """Row 5"""
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_gender).place(x=170,y=275,width=200)
        
        lbl_proof=Label(Frame1,text="Proof ID",font=("times new roman",20),bg="white",fg="black").place(x=390,y=270)
        txt_proof=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_proof_id).place(x=520,y=275,width=200)
        
        """Row 6"""
        lbl_email=Label(Frame1,text="Email ID",font=("times new roman",20),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_email).place(x=170,y=325,width=200)
        
        lbl_contact=Label(Frame1,text="Contact",font=("times new roman",20),bg="white",fg="black").place(x=390,y=320)
        txt_contact=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_contact).place(x=520,y=325,width=200)
        
        """Row 7"""
        lbl_hired=Label(Frame1,text="Hired Location",font=("times new roman",18),bg="white",fg="black").place(x=10,y=372)
        txt_hired=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_hr_location).place(x=170,y=375,width=200)
        
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black").place(x=390,y=370)
        txt_status=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_status).place(x=520,y=375,width=200)
        
        """Row 8"""
        lbl_address=Label(Frame1,text="Address",font=("times new roman",18),bg="white",fg="black").place(x=10,y=422)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=170,y=425,width=550,height=150)

        #=============Variables
        self.var_month=StringVar()   
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()        
        
        #=============Frame 2
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)
        
        title3=Label(Frame2,text="Employee Salary Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        """Row 1"""
        lbl_month=Label(Frame2,text="Month",font=("times new roman",18),bg="white",fg="black").place(x=10,y=60)
        txt_month=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_month).place(x=90,y=62,width=100)
        
        lbl_year=Label(Frame2,text="Year",font=("times new roman",18),bg="white",fg="black").place(x=210,y=60)
        txt_year=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_year).place(x=270,y=62,width=100)
        
        lbl_salary=Label(Frame2,text="Salary",font=("times new roman",18),bg="white",fg="black").place(x=380,y=60)
        txt_salary=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_salary).place(x=460,y=62,width=100)
        

        """Row 2"""
        lbl_days=Label(Frame2,text="Total Days",font=("times new roman",18),bg="white",fg="black").place(x=10,y=120)
        txt_days=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_t_days).place(x=170,y=125,width=100)
        
        lbl_absent=Label(Frame2,text="Absents",font=("times new roman",18),bg="white",fg="black").place(x=300,y=120)
        txt_absent=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_absent).place(x=420,y=125,width=120)
        
        """Row 3"""
        lbl_medical=Label(Frame2,text="Medical",font=("times new roman",18),bg="white",fg="black").place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_medical).place(x=170,y=155,width=100)
        
        lbl_pf=Label(Frame2,text="P.F.",font=("times new roman",18),bg="white",fg="black").place(x=300,y=150)
        txt_pf=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_pf).place(x=420,y=155,width=120)
        
        """Row 4"""
        lbl_convence=Label(Frame2,text="Convence",font=("times new roman",18),bg="white",fg="black").place(x=10,y=180)
        txt_convence=Entry(Frame2,font=("times new roman",15),bg="lightyellow",fg="black",textvariable=self.var_convence).place(x=170,y=185,width=100)
        
        lbl_netsalary=Label(Frame2,text="Net Salary",font=("times new roman",18),bg="white",fg="black").place(x=300,y=180)
        txt_netsalary=Entry(Frame2,font=("times new roman",15),bg="lightyellow",state=DISABLED,fg="black",textvariable=self.var_net_salary).place(x=420,y=185,width=120)
        
        """Buttons (Row 5)"""
        btn_calculate=Button(Frame2,text="Calculate",font=("times new roman",20),bg="orange",fg="black",command=self.calculate).place(x=150,y=240,height=30,width=120)        
        btn_save=Button(Frame2,text="Save",font=("times new roman",20),bg="green",fg="white",command=self.add).place(x=285,y=240,height=30,width=120)        
        btn_clear=Button(Frame2,text="Clear",font=("times new roman",20),bg="gray",fg="black").place(x=420,y=240,height=30,width=120)        
                
        
        
        #=============Frame 3
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click (num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
        
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
           
        def cal_clear():
            self.var_txt.set('')
            self.var_operator=''
        
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)
        
        """Calculator Frame"""
        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=247,height=300)
        
        txt_result=Entry(Cal_Frame,bg="lightgray",state=DISABLED,font=("times new roman",25,"bold"),justify=RIGHT,textvariable=self.var_txt,fg="black").place(x=0,y=0,relwidth=1,height=50)
        
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
    
        
    
        """Salary Frame"""
        sal_Frame=Frame(Frame3,bg='white',bd=2,relief=RIDGE)
        sal_Frame.place(x=251,y=2,width=320,height=300)
        
        title_sal=Label(sal_Frame,text="Salary Reciept",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        sal_Frame2=Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)
        
        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        self.txt_salary_recipt=Text(sal_Frame2,font=("times new roman",15),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        
        btn_print=Button(sal_Frame,text="Print",font=("times new roman",20),bg="lightblue",fg="black").place(x=180,y=262,height=30,width=120)
    
        self.check_connection()
    
    
    
    
    
    
#==============All Funstions Start Here=============        
    def add(self):
        if self.var_emp_code == "" or self.var_net_salary.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Please Calculate The Net Salary And \nFill Up The Employee Code And Your Name")
            
        else:    
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="ems")
                cur=con.cursor()
                cur.execute("SELECT * FROM emp_salary WHERE e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror("Error","This employee ID has already available in our record,\ntry again with another ID",parent=self.root)
                else:
                    cur.execute("INSERT INTO emp_salary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.var_emp_code.get(),   
                                    self.var_designation.get(),
                                    self.var_name.get(),
                                    self.var_age.get(),  
                                    self.var_gender.get(),
                                    self.var_email.get(),
                                    self.var_hr_location.get(),
                                    self.var_doj.get(),
                                    self.var_dob.get(),
                                    self.var_experience.get(),
                                    self.var_proof_id.get(),
                                    self.var_contact.get(),
                                    self.var_status.get(),
                                    self.txt_address.get('1.0',END),
                                    self.var_month.get(),   
                                    self.var_year.get(),
                                    self.var_salary.get(),
                                    self.var_t_days.get(),
                                    self.var_absent.get(),
                                    self.var_medical.get(),
                                    self.var_pf.get(),
                                    self.var_convence.get(),
                                    self.var_net_salary.get(),
                                    self.txt_salary_recipt.get('1.0',END)
                                )
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Record Has Been Added Sucessfully")
                    
                
            except Exception as ex:
                messagebox.showerror("Error",f"Error Due To :{ex}")         
        
        
        
    def calculate(self):
         if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_t_days.get()=='' or self.var_absent.get()=='' or self.var_medical.get()=='' or self.var_pf.get()=='' or self.var_convence.get()=='':
             messagebox.showerror("Error","All Fields In Employee Salary Details Are Required")
             
         else:
             #self.var_net_salary.set('RESULT')
             #35000/31==1752
             #31-10=21*1752
             per_day=int(self.var_salary.get())/int(self.var_t_days.get())
             work_day=int(self.var_t_days.get())-int(self.var_absent.get())
             sal_=per_day*work_day
             deduct=int(self.var_medical.get())+int(self.var_pf.get())
             addition=int(self.var_convence.get())
             net_sal=sal_-deduct+addition
             self.var_net_salary.set(str(round(net_sal,2)))
        
        
    def check_connection(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",db="ems")
            cur=con.cursor()
            cur.execute("SELECT * FROM emp_salary")
            rows=cur.fetchall()
            print(rows)
            
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To :{ex}")            
        
        
        

root=Tk()
obj=EmployeeSystem(root)
root.mainloop()       