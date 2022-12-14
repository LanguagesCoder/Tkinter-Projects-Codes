from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
from math import* 
import time


class Clock:
    def __init__ (self,root):
        self.root=root
        """ For Setting Up The Window """
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        """ For Labeling The Window"""
        title=Label(self.root,text="Analog Clock",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
    
        self.lbl=Label(self.root,bg="white",bd=20,relief=RAISED)
        self.lbl.place(x=450,y=150,width=400,height=400)
        
        # self.clock_image()
        self.working()
        
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        
        """For Clock Image """
        bg=Image.open("clock.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        """ Formula TO Rotate The Clock"""
        #angle_in_radian = angle_in_degrees * math.pi/180
        #line_lenght = 100
        #center_x = 250
        #center_y = 250
        #end_x = center_x + line_lenght * math.cos(angle in radians)
        #end_y = center_y + line_lenght * math.sin(angle in radians)
        
        origin = 200,200
        """ For Hour Line Image """    
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        """ For Minute Line Image """    
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        """ For Second Line Image """    
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=4)
        """For Circle Image"""
        draw.ellipse((195,195,210,210),fill="black")
        """ For Saving The Image """
        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        print(h,m,s)
        # print(hr,min_,sec_)
        self.clock_image(hr, min_, sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
obj=Clock(root)
root.mainloop()      
