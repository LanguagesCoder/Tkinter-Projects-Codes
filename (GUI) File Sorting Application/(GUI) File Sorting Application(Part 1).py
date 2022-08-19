from tkinter import*
from tkinter import ttk

class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("File Sorting Application")
        self.root.geometry("1350x700+0+0")
        
        self.root.config(bg="white")
        
        self.logo_icon=PhotoImage(file="images/folder_image.png")
        title=Label(self.root,text="Files Sorting Appliction",font=("impact",40),bg="#023548",fg="white",anchor="w",image=self.logo_icon,compound=LEFT,padx=10).place(x=0,y=0,relwidth=1)
        
        """Section 1"""
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman",25),bg="white").place(x=50,y=100)
        txt_folder_name=Entry(self.root,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=250,y=100,height=40,width=600)
        btn_browse=Button(self.root,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2").place(x=900,y=100,height=40,width=150)
        hr=Label(self.root,bg="lightgray").place(x=50,y=160,height=2,width=1250)
        

root=Tk()
obj=Sorting_App(root)
root.mainloop()        