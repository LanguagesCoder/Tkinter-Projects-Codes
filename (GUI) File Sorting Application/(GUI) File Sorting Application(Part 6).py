from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil

class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("File Sorting Application")
        self.root.geometry("1350x700+0+0")
        
        self.root.config(bg="white")
        
        self.logo_icon=PhotoImage(file="images/folder_image.png")
        title=Label(self.root,text="Files Sorting Appliction",font=("impact",40),bg="#023548",fg="white",anchor="w",image=self.logo_icon,compound=LEFT,padx=10).place(x=0,y=0,relwidth=1)
        

        """All Variables"""
        self.var_folder_name=StringVar()
        
        """All Extensions"""
        self.image_extensions=["Image Extentions",".jpeg",".jpg",".png"]
        self.audio_extensions=["Audio Extentions",".mp3",".wav",".amr",".m4a","M4A"]
        self.video_extensions=["Video Extentions",".mp4",".mov",".avi",".mkv"]
        self.doc_extensions=["Document Extentions",".doc",".xlsx",".ppt",".pptx",".xls",".pdf",".zip",".rar",".cvs",".docx",".txt"]
        
        """Folders"""
        self.folders={
                'images':self.image_extensions,
                'audios':self.audio_extensions,
                'videos':self.video_extensions,
                'documents':self.doc_extensions,
                }
        
        """All Image Icons"""
        self.image_icon=PhotoImage(file="images/im.png")
        self.audio_icon=PhotoImage(file="images/audios.png")
        self.video_icon=PhotoImage(file="images/videos.png")
        self.document_icon=PhotoImage(file="images/document.png")
        self.other_icon=PhotoImage(file="images/question-mark.png")
        

        """Section 1"""
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman",25),bg="white").place(x=50,y=100)
        txt_folder_name=Entry(self.root,font=("times new roman",15),bg="lightyellow",state='readonly',textvariable=self.var_folder_name).place(x=250,y=100,height=40,width=600)
        btn_browse=Button(self.root,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2",command=self.browse_function).place(x=900,y=100,height=40,width=150)
        btn_exit=Button(self.root,text="EXIT",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2",command=self.exit_f).place(x=1100,y=100,height=40,width=150)
        hr=Label(self.root,bg="lightgray").place(x=50,y=160,height=2,width=1250)
        
        
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
        
        
        """Section 3"""
        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=300,width=1250,height=300)
        
        self.lbl_total_files=Label(Frame1,text="Total Files : 0",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=10)
        
        self.lbl_total_images=Label(Frame1,text="",font=("times new roman",15,"bold"),bg="#0875B7",fg="white",image=self.image_icon,compound=TOP,bd=2,relief=RAISED)
        self.lbl_total_images.place(x=20,y=60,width=230,height=230)
        
        self.lbl_total_audios=Label(Frame1,text="",font=("times new roman",15,"bold"),bg="#008EA4",fg="white",image=self.audio_icon,compound=TOP,bd=2,relief=RAISED)
        self.lbl_total_audios.place(x=260,y=60,width=230,height=230)
        
        self.lbl_total_videos=Label(Frame1,text="",font=("times new roman",15,"bold"),bg="#DF002A",fg="white",image=self.video_icon,compound=TOP,bd=2,relief=RAISED)
        self.lbl_total_videos.place(x=500,y=60,width=230,height=230)
        
        self.lbl_total_docs=Label(Frame1,text="",font=("times new roman",15,"bold"),bg="#008EA4",fg="white",image=self.document_icon,compound=TOP,bd=2,relief=RAISED)
        self.lbl_total_docs.place(x=740,y=60,width=230,height=230)
        
        self.lbl_total_others=Label(Frame1,text="",font=("times new roman",15,"bold"),bg="gray",fg="white",image=self.other_icon,compound=TOP,bd=2,relief=RAISED)
        self.lbl_total_others.place(x=980,y=60,width=230,height=230)
        
        
        """Section 4"""
        lbl_status=Label(self.root,text="STATUS:",font=("times new roman",20),bg="white").place(x=50,y=620)
        
        """Total Files"""
        self.lbl_st_total=Label(self.root,text="",font=("times new roman",18),bg="white",fg="green")
        self.lbl_st_total.place(x=300,y=620)
        
        """Files Moved"""
        self.lbl_st_moved=Label(self.root,text="",font=("times new roman",18),bg="white",fg="blue")
        self.lbl_st_moved.place(x=500,y=620)
        
        """Files Left"""
        self.lbl_st_left=Label(self.root,text="",font=("times new roman",18),bg="white",fg="orange")
        self.lbl_st_left.place(x=700,y=620)
        
        
        """Button Clear"""
        self.btn_clear=Button(self.root,text="CLEAR",font=("times new roman",15,"bold"),bg="#607d8b",fg="white",activebackground="#607d8b",activeforeground="white",cursor="hand2",command=self.clear,state=DISABLED)
        self.btn_clear.place(x=880,y=610,height=40,width=200)
        
        """Button Start"""
        self.btn_start=Button(self.root,text="START",font=("times new roman",15,"bold"),bg="#ff5722",fg="white",activebackground="#ff5722",activeforeground="white",cursor="hand2",command=self.start_function,state=DISABLED)
        self.btn_start.place(x=1100,y=610,height=40,width=200)
    
    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        cambine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    #print(folder_name)
                    for x in folder_name[1]:
                        cambine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents+=1
        
        """For Calculating Oher Files Only"""
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                ext="."+i.split(".")[-1]                
                if ext.lower() not in cambine_list:
                    others+=1
        
       
        self.lbl_total_images.config(text="Total Images:"+str(images))      
        self.lbl_total_videos.config(text="Total Videos:"+str(videos))
        self.lbl_total_audios.config(text="Total Audios:"+str(audios))
        self.lbl_total_docs.config(text="Total Documents:"+str(documents)) 
        self.lbl_total_others.config(text="Others :"+str(others))       
        self.lbl_total_files.config(text="Total Files:"+str(self.count))
        self.lbl_st_left.config(text="LEFT : 0")
        self.lbl_st_moved.config(text="MOVED : 0")
        self.lbl_st_total.config(text="TOTAL : "+str(self.count))
    
    def browse_function(self):
        op=filedialog.askdirectory(title="Select Folder For Sorting")
        if op != None:
            # print(op)
            self.var_folder_name.set(str(op))
            self.directry=self.var_folder_name.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directry)
            lenght=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            self.btn_clear.config(state=NORMAL)
            """
            print(self.all_files)
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                    # print("YES")
                    self.create_move(i.split(".")[-1],i)    
                print(f"Total Files:{lenght}| Done:{count}| Left:{lenght-count}")
                count+=1    
            """
    def start_function (self):
        if self.var_folder_name.get()!="":
            self.btn_clear.config(state=DISABLED)
            self.btn_start.config(state=DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                    # print("YES")
                    
                    c+=1 
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL : "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED : "+str(c))
                    self.lbl_st_left.config(text="LEFT : "+str(self.count-c))
                # print(f"Total Files:{lenght}| Done:{count}| Left:{lenght-count}")
                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()
            messagebox.showinfo("Success","The Files Have Been Sorted Successfully🙂🙂🙂")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please Choose The Folder First")
            
    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder))==True:
               os.rename(os.path.join(self.directry,folder),os.path.join(self.directry,folder.lower()))
        

    def create_move(self,ext,file_name):
        find=False 
        for folder_name in self.folders:
             if"."+ext in self.folders[folder_name]:
                 if folder_name not in os.listdir(self.directry):
                     os.mkdir(os.path.join(self.directry,folder_name))
                 shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,folder_name))
                 find=True
                 break
        if find!= True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry,self.other_name))
            shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,self.other_name))    
    
    
    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_folder_name.set("")
        self.lbl_total_files.config(text="Total Files : 0")
        self.lbl_st_left.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_total.config(text="")
        self.lbl_total_audios.config(text="")
        self.lbl_total_docs.config(text="")
        self.lbl_total_images.config(text="")
        self.lbl_total_others.config(text="")
        self.lbl_total_videos.config(text="")

    def exit_f (self):
        self.root.destroy()
    
root=Tk()
obj=Sorting_App(root)
root.mainloop()        