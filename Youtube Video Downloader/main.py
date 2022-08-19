Closed = "Window Closed!Have A Good"
from tkinter import*
from tkinter import ttk , messagebox
from plyer.facades import notification
from pytube import *
from PIL import Image,ImageTk
import requests
import io
import os

class Youtube_App :
    def __init__(self,root):
        self.root=root
        self.root.title("Youtube Video Downloader")
        self.root.geometry("500x440+300+50")
        self.root.resizable(True,True)   
        self.root.config(bg="white")

        title=Label(self.root,text="   Youtube Video Downloader",font=("times new roman",15),bg="#262626",fg="white",anchor="w").pack(side=TOP,fill=X)
         
        self.var_url=StringVar()
        lbl_url=Label(self.root,text="Video URL:",font=("times new roman",15,),bg="white").place(x=10,y=50)
        txt_url=Entry(self.root,font=("times new roman",13),bg="lightyellow",textvariable=self.var_url).place(x=120,y=50,width=350)
        
        self.var_filetype=StringVar()
        self.var_filetype.set("Video")
        lbl_filetype=Label(self.root,text="Filetype:",font=("times new roman",15),bg="white").place(x=10,y=90)
        self.video=Checkbutton(self.root,text = "Video",variable=self.var_filetype,onvalue="Video",offvalue="Audio",bg = "white",font=("times new roman",12),activebackground="white",activeforeground="white")
        self.video.place(x=120,y=90)
        self.audio=Checkbutton(self.root,text = "Audio",variable=self.var_filetype,onvalue="Audio",offvalue="Video",bg = "white",font=("times new roman",12),activebackground="white",activeforeground="white")
        self.audio.place(x=220,y=90)
    
        
        self.btn_search=Button(self.root,command=self.Search,text="Search",font=("times new roman",15),bg="blue",fg="white")
        self.btn_search.place(x=350,y=90,height=30,width=120)
        
        frame1=Frame(self.root,bd=2,relief=RIDGE,bg="lightyellow")
        frame1.place(x=10,y=130,height=180,width=480)
        
        self.video_title=Label(frame1,text="Video Title",font=("times new roman",12),bg="#262626",fg="white",anchor="w")
        self.video_title.place(x=0,y=0,relwidth=1)
        
        self.video_image=Label(frame1,text="Video \nImage",font=("times new roman",15),bg="#262626",fg="white",bd=2,relief=RIDGE)
        self.video_image.place(x=5,y=30,width=180,height=140)
        
        lbl_decs=Label(frame1,text="Description",font=("times new roman",15),bg="lightyellow",fg="#262626").place(x=190,y=30)
        
        self.video_decs=Text(frame1,font=("times new roman",12),state=DISABLED,bg="lightyellow",fg="#262626",bd=5,relief=RIDGE)
        self.video_decs.place(x=190,y=60,width=280,height=110)        
        
        self.lbl_size=Label(self.root,text="Video Size : 0MB ",font=("times new roman",15,),bg="white",bd=2,relief=RIDGE)
        self.lbl_size.place(x=50,y=320)
        
        self.lbl_percentage=Label(self.root,text="Downloading : 0% ",font=("times new roman",15,),bg="white",bd=2,relief=RIDGE)
        self.lbl_percentage.place(x=250,y=320)
        
        self.btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="green",fg="white",command=self.clear)
        self.btn_clear.place(x=170,y=350,height=25,width=70)
        self.btn_download=Button(self.root,text="Download",font=("times new roman",15),bg="green",fg="white",command=self.Download,state=DISABLED)
        self.btn_download.place(x=250,y=350,height=25,width=90)
        
        self.prog=ttk.Progressbar(self.root,orient=HORIZONTAL,mode='determinate')
        self.prog.place(x=10,y=380,width=485,height=20) 
        
        self.lbl_messages=Label(self.root,text=" ",font=("times new roman",15,),bg="white")
        self.lbl_messages.place(x=0,y=405,relwidth=1)
        
        if os.path.exists('Videos')==False:
            os.mkdir('Videos')
        if os.path.exists('Audios')==False:
            os.mkdir('Audios')
        
    def Search(self):
        if self.var_url.get()=="":
            self.lbl_messages.config(text="To Search Please Enter The URL",fg='red')
        else:        
            yt=YouTube(self.var_url.get())
            response=requests.get(yt.thumbnail_url) 
            img_byte=io.BytesIO(response.content)
            self.img=Image.open(img_byte)
            self.img=self.img.resize((180,140),Image.ANTIALIAS)
            self.img=ImageTk.PhotoImage(self.img)
            self.video_image.config(image=self.img)
            
            if self.var_filetype.get()=='Video':
                select_file=yt.streams.filter(progressive=True).last()
            if self.var_filetype.get()=='Audio':    
                select_file=yt.streams.filter(only_audio=True).last()
            
            self.size_in_Bytes=select_file.filesize
            max_size=self.size_in_Bytes/1024000
            self.mb=str(round(max_size,2))+'MB'
            self.lbl_size.config(text="Video Size : "+self.mb)
    
            self.video_title.config(text=yt.title)
            self.video_decs.delete('1.0',END)
            self.video_decs.config(state=NORMAL)
            self.video_decs.insert(END,yt.description[:10000])
            self.video_decs.config(state=DISABLED)
            self.btn_download.config(state=NORMAL)
    
    def progress (self,streams,chunk,bytes_remaining):
        percentage=(float(abs(bytes_remaining-self.size_in_Bytes)/self.size_in_Bytes))*float(100)
        self.prog['value']=percentage
        self.prog.update()
        self.lbl_percentage.config(text=f"Downloading : {str(round(percentage,2))}%")
        if (round(percentage,2)) < 100:
            self.btn_clear.config(state=DISABLED)
            self.btn_download.config(state=DISABLED)
            self.btn_search.config(state=DISABLED)
        if (round(percentage,2)) == 100:
            self.lbl_messages.config(text="Download Completed",fg='green')
            self.btn_download.config(state=NORMAL)
            self.btn_search.config(state=NORMAL)
            self.btn_clear.config(state=NORMAL)
    
    def clear (self):
        self.var_filetype.set('Video')
        self.var_url.set(' ')
        self.prog['value']=0
        self.btn_download.config(state=DISABLED)
        self.lbl_messages.config(text=' ')
        self.video_title.config(text="Video Title")
        self.video_image.config(text="Video \nImage",image="")
        self.video_decs.delete('1.0',END)
        self.lbl_size.config(text="Video Size : 0MB")
        self.lbl_percentage.config(text="Downloading : 0% ")
        self.btn_clear.config(state=NORMAL)
        self.btn_search.config(state=NORMAL)
        self.video_decs.config(state=NORMAL)
        self.video_decs.delete('1.0',END)
        self.video_decs.config(state=DISABLED)
        
    def Download (self):
        yt=YouTube(self.var_url.get(),on_progress_callback=self.progress)
            
        if self.var_filetype.get()=='Video':
            select_file=yt.streams.filter(progressive=True).last()
            select_file.download('Videos/')
        if self.var_filetype.get()=='Audio':    
            select_file=yt.streams.filter(only_audio=True).last()
            select_file.download('Audios/')
        
     
root=Tk()
obj=Youtube_App(root)
root.mainloop()
print(Closed)
