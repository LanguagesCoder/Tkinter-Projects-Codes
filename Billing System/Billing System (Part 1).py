from tkinter import*
class Billing_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        bg_colour="#074463"
        
        title=Label(self.root,text="Billing Software",font=("times new roman",30,"bold"),pady=2,bd=12,relief=GROOVE,bg=bg_colour,fg="White").pack(fill=X) 
        
        
        
        """Coustomer Detail (Frame 1)"""
        F1 = LabelFrame(self.root,text="Customer Detaiils",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour,bd=10,relief=GROOVE)
        F1.place(x=0,y=70,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_colour,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font=("arial",15),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",font=("times new roman",18,"bold"),bg=bg_colour,fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,font=("arial",15),bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl=Label(F1,text="Bill Number",font=("times new roman",18,"bold"),bg=bg_colour,fg="white").grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,font=("arial",15),bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn = Button(F1,text="Search",width=10,bd=7,font=("arial",12,"bold")).grid(row=0,column=6,padx=10,pady=10)
        
      
        
        """Cosmetics(Frame 2)"""
        F2 = LabelFrame(self.root,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour,bd=10,relief=GROOVE)
        F2.place(x=0,y=169,width=325,height=380)
        
        """Labels"""
        bath_lbl=Label(F2,text="Bath Soap:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        face_cream_lbl=Label(F2,text="Face Cream:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        face_w_lbl=Label(F2,text="Face Wash:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        hair_s_lbl=Label(F2,text="Hair Spray:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        hair_g_lbl=Label(F2,text="Hair Gell:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        body_lbl=Label(F2,text="Body Loshan:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        
        """Entry Feilds"""
        bath_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        face_cream_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        f_w_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        hair_s_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        hair_g_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        body_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        


        """Grocery(Frame 3)"""
        F3 = LabelFrame(self.root,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour,bd=10,relief=GROOVE)
        F3.place(x=328,y=169,width=325,height=380)
        
        """Labels"""
        g1_lbl=Label(F3,text="Rice:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        g2_lbl=Label(F3,text="Food Oil:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        g3_lbl=Label(F3,text="Daal:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        g4_lbl=Label(F3,text="Wheat:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        g5_lbl=Label(F3,text="Sugar:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        g6_lbl=Label(F3,text="Tea:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        
        """Entry Feilds"""
        g1_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        g2_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        g3_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        g4_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        g5_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        g6_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        
        
        """Cold Drinks(Frame 4)"""
        F4 = LabelFrame(self.root,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour,bd=10,relief=GROOVE)
        F4.place(x=657,y=169,width=325,height=380)
        
        """Labels"""
        c1_lbl=Label(F4,text="Maza:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        c2_lbl=Label(F4,text="Cock:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        c3_lbl=Label(F4,text="Frooti:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        c4_lbl=Label(F4,text="Thums Up:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        c5_lbl=Label(F4,text="Limca:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        c6_lbl=Label(F4,text="Sprite:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        
        """Entry Feilds"""
        c1_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        c2_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        c3_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        c4_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        c5_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        c6_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        
        
        """Bill Area (Frame 5)"""
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=987,y=169,width=370,height=380)
        bill_title=Label(F5,text="Bill Area",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        """Button (Frame 6)"""
        F6 = LabelFrame(self.root,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour,bd=10,relief=GROOVE)
        F6.place(x=0,y=550,relwidth=1,height=150)
        
        """Taxexs"""
        """Labels"""
        m1_lbl=Label(F6,text="Total Cosmetics Price:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=0,column=0,pady=1,padx=20,sticky="w")
        m2_lbl=Label(F6,text="Total Grocery Price:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=1,column=0,pady=1,padx=20,sticky="w")
        m3_lbl=Label(F6,text="Total Cold Drink Price:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=2,column=0,pady=1,padx=20,sticky="w")
        
        """Entry Fields"""
        m1_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)
        m2_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=1,padx=10)
        m3_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=1,padx=10)
        
        """Prices"""
        """Labels"""
        t1_lbl=Label(F6,text="Cosmetics Tax:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=0,column=2,pady=1,padx=20,sticky="w")
        t2_lbl=Label(F6,text="Grocery Tax:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=1,column=2,pady=1,padx=20,sticky="w")
        t3_lbl=Label(F6,text="Cold Drink Tax:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=2,column=2,pady=1,padx=20,sticky="w")
        
        """Entry Fields"""
        t1_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,pady=1,padx=10)
        t2_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,pady=1,padx=10)
        t3_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,pady=1,padx=10)
        
        
        
        """Buttons (Frame 7)"""
        btn_f = Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)
        
        total_btn=Button(btn_f,text="Total",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5).grid(row=0,column=0,pady=5,padx=5)
        GBill_btn=Button(btn_f,text="Generate Bill",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5).grid(row=0,column=1,pady=5,padx=5)
        Clear_btn=Button(btn_f,text="Clear",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5).grid(row=0,column=2,pady=5,padx=5)
        Exit_btn=Button(btn_f,text="Exit",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5).grid(row=0,column=3,pady=5,padx=5)
        
        
        
        

root = Tk()
obj=Billing_App(root)
root.mainloop()    