from tkinter import*
import math,random
from tkinter import ttk,messagebox
class Billing_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        bg_colour="#074463"
        
        title=Label(self.root,text="Billing Software",font=("times new roman",30,"bold"),pady=2,bd=12,relief=GROOVE,bg=bg_colour,fg="White").pack(fill=X) 
        
        
        
        """All Variables"""
        """Cosmetics"""
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        
        """Grocery"""
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        
        """Cold Drinks"""
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        
        """Total Product Price & Tax Variables"""
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        
        """Coustomer"""
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.search_bill=StringVar()
        
        
        
        """Coustomer Detail (Frame 1)"""
        F1 = LabelFrame(self.root,text="Customer Detaiils",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour,bd=10,relief=GROOVE)
        F1.place(x=0,y=70,relwidth=1)
        
        """Labels"""
        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_colour,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cphn_lbl=Label(F1,text="Phone No.",font=("times new roman",18,"bold"),bg=bg_colour,fg="white").grid(row=0,column=2,padx=20,pady=5)   
        c_bill_lbl=Label(F1,text="Bill Number",font=("times new roman",18,"bold"),bg=bg_colour,fg="white").grid(row=0,column=4,padx=20,pady=5)
        
        """Entry Feilds"""
        cname_txt=Entry(F1,width=15,font=("arial",15),bd=7,relief=SUNKEN,textvariable=self.c_name).grid(row=0,column=1,pady=5,padx=10)
        cphn_txt=Entry(F1,width=15,font=("arial",15),bd=7,relief=SUNKEN,textvariable=self.c_phon).grid(row=0,column=3,pady=5,padx=10)
        c_bill_txt=Entry(F1,width=15,font=("arial",15),bd=7,relief=SUNKEN,textvariable=self.search_bill).grid(row=0,column=5,pady=5,padx=10)
        
        """Button"""
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
        bath_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.soap).grid(row=0,column=1,pady=10,padx=10)
        face_cream_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.face_cream).grid(row=1,column=1,pady=10,padx=10)
        f_w_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.face_wash).grid(row=2,column=1,pady=10,padx=10)
        hair_s_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.spray).grid(row=3,column=1,pady=10,padx=10)
        hair_g_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.gell).grid(row=4,column=1,pady=10,padx=10)
        body_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.loshan).grid(row=5,column=1,pady=10,padx=10)
        


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
        g1_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.rice).grid(row=0,column=1,pady=10,padx=10)
        g2_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.food_oil).grid(row=1,column=1,pady=10,padx=10)
        g3_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.daal).grid(row=2,column=1,pady=10,padx=10)
        g4_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.wheat).grid(row=3,column=1,pady=10,padx=10)
        g5_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.sugar).grid(row=4,column=1,pady=10,padx=10)
        g6_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.tea).grid(row=5,column=1,pady=10,padx=10)
        
        
        
        """Cold Drinks(Frame 4)"""
        F4 = LabelFrame(self.root,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_colour,bd=10,relief=GROOVE)
        F4.place(x=657,y=169,width=325,height=380)
        
        """Labels"""
        c1_lbl=Label(F4,text="Maza:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=0,column=0,pady=10,padx=10,sticky="w")
        c2_lbl=Label(F4,text="Cock:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=1,column=0,pady=10,padx=10,sticky="w")
        c3_lbl=Label(F4,text="Frooti:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=2,column=0,pady=10,padx=10,sticky="w")
        c4_lbl=Label(F4,text="Thumbs Up:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=3,column=0,pady=10,padx=10,sticky="w")
        c5_lbl=Label(F4,text="Limca:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=4,column=0,pady=10,padx=10,sticky="w")
        c6_lbl=Label(F4,text="Sprite:",font=("times new roman",16,"bold"),bg=bg_colour,fg="lightgreen").grid(row=5,column=0,pady=10,padx=10,sticky="w")
        
        """Entry Feilds"""
        c1_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.maza).grid(row=0,column=1,pady=10,padx=10)
        c2_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.cock).grid(row=1,column=1,pady=10,padx=10)
        c3_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.frooti).grid(row=2,column=1,pady=10,padx=10)
        c4_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.thumbsup).grid(row=3,column=1,pady=10,padx=10)
        c5_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.limca).grid(row=4,column=1,pady=10,padx=10)
        c6_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,textvariable=self.sprite).grid(row=5,column=1,pady=10,padx=10)
        
        
        
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
        m1_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN,textvariable=self.cosmetic_price).grid(row=0,column=1,pady=1,padx=10)
        m2_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN,textvariable=self.grocery_price).grid(row=1,column=1,pady=1,padx=10)
        m3_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN,textvariable=self.cold_drink_price).grid(row=2,column=1,pady=1,padx=10)
        
        """Prices"""
        """Labels"""
        t1_lbl=Label(F6,text="Cosmetics Tax:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=0,column=2,pady=1,padx=20,sticky="w")
        t2_lbl=Label(F6,text="Grocery Tax:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=1,column=2,pady=1,padx=20,sticky="w")
        t3_lbl=Label(F6,text="Cold Drink Tax:",font=("times new roman",14,"bold"),bg=bg_colour,fg="white").grid(row=2,column=2,pady=1,padx=20,sticky="w")
        
        """Entry Fields"""
        t1_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN,textvariable=self.cosmetic_tax).grid(row=0,column=3,pady=1,padx=10)
        t2_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN,textvariable=self.grocery_tax).grid(row=1,column=3,pady=1,padx=10)
        t3_txt=Entry(F6,width=18,font=("arial",10,"bold"),bd=5,relief=SUNKEN,textvariable=self.cold_drink_tax).grid(row=2,column=3,pady=1,padx=10)
        
        
        
        """Buttons (Frame 7)"""
        btn_f = Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)
        
        total_btn=Button(btn_f,text="Total",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5,command=self.total).grid(row=0,column=0,pady=5,padx=5)
        GBill_btn=Button(btn_f,text="Generate Bill",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5,command=self.bill_area).grid(row=0,column=1,pady=5,padx=5)
        Clear_btn=Button(btn_f,text="Clear",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5).grid(row=0,column=2,pady=5,padx=5)
        Exit_btn=Button(btn_f,text="Exit",bg="cadetblue",fg="white",pady=15,width=11,font=("arial",13,"bold"),bd=5).grid(row=0,column=3,pady=5,padx=5)
        self.welcome_bill()
        
    
        
    def total(self):
        self.c_s_p=(self.soap.get()*40)
        self.c_fc_p=(self.face_cream.get()*120)
        self.c_fw_p=(self.face_wash.get()*60)
        self.c_hs_p=(self.spray.get()*180)
        self.c_hg_p=(self.gell.get()*140)
        self.c_bl_p=(self.loshan.get()*180)
        
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+    
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p
                                    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        
        self.g_r_p=(self.rice.get()*80)
        self.g_fo_p=(self.food_oil.get()*180)
        self.g_d_p=(self.daal.get()*60)
        self.g_w_p=(self.wheat.get()*240)
        self.g_s_p=(self.sugar.get()*45)
        self.g_t_p=(self.tea.get()*150)
        
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+    
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        
        self.cd_m_p=(self.maza.get()*60)
        self.cd_c_p=(self.cock.get()*60)
        self.cd_f_p=(self.frooti.get()*50)
        self.cd_t_p=(self.thumbsup.get()*45)
        self.cd_l_p=(self.limca.get()*40)
        self.cd_s_p=(self.sprite.get()*60)
        
        self.total_cold_drink_price=float(
                                        self.cd_m_p+
                                        self.cd_c_p+    
                                        self.cd_f_p+
                                        self.cd_t_p+
                                        self.cd_l_p+
                                        self.cd_s_p
                                        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
        
        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.cd_tax
                                )
    
        
        
        
                               
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome WebCoding Retial")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n=========================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n=========================================")
        
        
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Please Fill Up The Customer Details")
        
        elif self.cosmetic_price.get()=="Rs. 0.0" or self.grocery_price.get()=="Rs. 0.0" or self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("No Item","No Item Has Been Choosen.Please Select Atlest One Item.")
            
        else:
            self.welcome_bill()
            
            """Cosmetics"""
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")
                
            """Grocery"""
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
    
            """Cold Drink"""
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.cd_m_p}")
            
            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.cd_c_p}")
            
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.cd_f_p}")
            
            if self.thumbsup.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.cd_t_p}")
            
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}")
            
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.cd_s_p}")
    
            self.txtarea.insert(END,"\n ----------------------------------------")
            
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetics Tax\t\t\t{self.cosmetic_tax.get()}")
                
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
               
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")    
            
            self.txtarea.insert(END,"\n ----------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill\t\t\tRs. {self.Total_bill}")   
            self.txtarea.insert(END,"\n ----------------------------------------")
        



root = Tk()
obj=Billing_App(root)
root.mainloop()    