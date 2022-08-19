from tkinter import *
from tkinter import messagebox
import wikipedia

class SearchApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Search App | Developed By Durgesh")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#262626")
        
        self.var_search=StringVar()
        
        title=Label(self.root,text="Search Application",font=("times new roman",40,"bold"),bg="white",fg="#262626",bd=4,relief=RIDGE)
        title.place(x=0,y=0,relwidth=1)
        
        lbl_word=Label(self.root,text="Search Word:",font=("times new roman",30,"bold"),bg="#262626",fg="white")
        lbl_word.place(x=10,y=100)
        
        txt_word=Entry(self.root,font=("times new roman",20),textvariable=self.var_search)
        txt_word.place(x=300,y=110,width=300)
    
        """BUTTONS"""
        search_btn=Button(self.root,text="Search",font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626",command=self.searchword)
        search_btn.place(x=620,y=108,height=40,width=150)
        
        search_btn=Button(self.root,text="Clear",font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626",command=self.clear)
        search_btn.place(x=790,y=108,height=40,width=150)
        
        search_btn=Button(self.root,text="Enable",font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626",command=self.enable)
        search_btn.place(x=950,y=108,height=40,width=200)
        
        search_btn=Button(self.root,text="Disable",font=("times new roman",20,"bold"),bg="lightyellow",fg="#262626",command=self.disable)
        search_btn.place(x=1170,y=108,height=40,width=180)
        
        
        self.lbl_mode=Label(self.root,text="MODE:TEXT ENABLED                                MAKE SURE THAT THE TEXT MODE IS ENABLED BEFORE CLICKING ON SEARCH BUTTON",font=("times new roman",15),bg="#262626",fg="yellow")
        self.lbl_mode.place(x=20,y=160)
        
        frame1=Frame(self.root,bd=2,relief=RIDGE)
        frame1.place(x=10,y=195,width=1330,height=500)
        
        scrolly=Scrollbar(frame1,orient=VERTICAL)
        scrolly.pack(fill=Y,side=RIGHT)
        
        self.txt_area=Text(frame1,font=("times new roman",15),yscrollcommand=scrolly.set,state=NORMAL)
        self.txt_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_area.yview)
        
    def enable (self):
        self.txt_area.config(state=NORMAL)
        self.lbl_mode.config(text="MODE:TEXT ENABLED                                MAKE SURE THAT THE TEXT MODE IS ENABLED BEFORE CLICKING ON SEARCH BUTTON")
        
    def disable (self):
        self.txt_area.config(state=DISABLED) 
        self.lbl_mode.config(text="MODE:TEXT DISABLED                                MAKE SURE THAT THE TEXT MODE IS ENABLED BEFORE CLICKING ON SEARCH BUTTON")
        
    def searchword (self):
        if self.var_search.get()=="":
            messagebox.showerror("Error","Please Fill Up The Entry Field")
        else:
            fetch_data=wikipedia.summary(self.var_search.get())
            self.txt_area.insert('1.0',fetch_data)
            self.lbl_mode.config(text="MODE:TEXT ENABLED                               MAKE SURE THAT THE TEXT MODE IS ENABLED BEFORE CLICKING ON SEARCH BUTTON")
    
    def clear (self):
        clear=messagebox.askyesno("Clear","After Clearing The Area The Text area would \nbe in DISABLED MODE If You are searching a word again\nfirst please click on the enable button.")
        if clear>0:
            self.var_search.set("")
            self.txt_area.delete('1.0',END)        
            self.lbl_mode.config(text="                                             MAKE SURE THAT THE TEXT MODE IS ENABLED BEFORE CLICKING ON SEARCH BUTTON")       
            self.txt_area.config(state=DISABLED)
        
            
        
root=Tk()
obj=SearchApp(root)
root.mainloop()        
        