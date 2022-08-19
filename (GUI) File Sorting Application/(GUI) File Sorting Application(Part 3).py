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
        
        """All Extensions"""
        self.image_extensions=["Image Extentions",".jpeg",".jpg",".png"]
        self.audio_extensions=["Audio Extentions",".mp3",".wav",".amr"]
        self.video_extensions=["Video Extentions",".mp4",".mov",".avi",".mkv"]
        self.doc_extensions=["Document Extentions",".doc",".xlsx",".ppt",".pptx",".xls",".pdf",".zip",".rar",".cvs",".docx",".txt"]
        
        """Section 2"""
        lbl_support_ext=Label(self.root,text="Various Supported Extentions",font=("times new roman",25),bg="white").place(x=50,y=170)
        
        """Image Extension Combobox"""
        self.image_box=ttk.Combobox(self.root,font=("times new roman",15),values=self.image_extensions,state='readonly',justify=CENTER)
        self.image_box.place(x=60,y=230,width=270,height=35)
        self.image_box.current(0)
        
        """Video Extension Combobox"""
        self.video_box=ttk.Combobox(self.root,font=("times new roman",15),values=self.video_extensions,state='readonly',justify=CENTER)
        self.video_box.place(x=360,y=230,width=270,height=35)
        self.video_box.current(0)
        
        """Audio Extension Combobox"""
        self.audio_box=ttk.Combobox(self.root,font=("times new roman",15),values=self.audio_extensions,state='readonly',justify=CENTER)
        self.audio_box.place(x=700,y=230,width=270,height=35)
        self.audio_box.current(0)
        
        """Document Extension Combobox"""
        self.doc_box=ttk.Combobox(self.root,font=("times new roman",15),values=self.doc_extensions,state='readonly',justify=CENTER)
        self.doc_box.place(x=1010,y=230,width=270,height=35)
        self.doc_box.current(0)
        
        """All Image Icons"""
        self.image_icon=PhotoImage(file="images/im.png")
        self.audio_icon=PhotoImage(file="images/audios.png")
        self.video_icon=PhotoImage(file="images/videos.png")
        self.document_icon=PhotoImage(file="images/document.png")
        self.other_icon=PhotoImage(file="images/question-mark.png")
        
        
        """Section 3"""
        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=300,width=1250,height=300)
        
        self.lbl_total_files=Label(Frame1,text="Total Files : 150",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=10)
        
        self.lbl_total_images=Label(Frame1,text="Total Images:30",font=("times new roman",15,"bold"),bg="#0875B7",fg="white",image=self.image_icon,compound=TOP)
        self.lbl_total_images.place(x=20,y=60,width=230,height=230)
        
        self.lbl_total_audios=Label(Frame1,text="Total Images:30",font=("times new roman",15,"bold"),bg="#008EA4",fg="white",image=self.audio_icon,compound=TOP)
        self.lbl_total_audios.place(x=260,y=60,width=230,height=230)
        
        self.lbl_total_videos=Label(Frame1,text="Total Images:30",font=("times new roman",15,"bold"),bg="#DF002A",fg="white",image=self.video_icon,compound=TOP)
        self.lbl_total_videos.place(x=500,y=60,width=230,height=230)
        
        self.lbl_total_docs=Label(Frame1,text="Total Images:30",font=("times new roman",15,"bold"),bg="#008EA4",fg="white",image=self.document_icon,compound=TOP)
        self.lbl_total_docs.place(x=740,y=60,width=230,height=230)
        
        self.lbl_total_others=Label(Frame1,text="Total Images:30",font=("times new roman",15,"bold"),bg="gray",fg="white",image=self.other_icon,compound=TOP)
        self.lbl_total_others.place(x=980,y=60,width=230,height=230)
        
root=Tk()
obj=Sorting_App(root)
root.mainloop()        