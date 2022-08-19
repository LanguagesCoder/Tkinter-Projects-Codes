from tkinter import *
import phonenumbers

# Imported From The Phone Numbers Library
from phonenumbers import geocoder
from phonenumbers import carrier

class Phone_Number_Details:
    def __init__(self, root):
        self.root = root
        blankSpace = " "
        self.root.title(50 * blankSpace + "Phone Number Details")
        self.root.geometry("500x310+500+200")
        self.root.resizable(False, False)
        self.root.config(bg = "white")

        """Variables"""
        self.number = StringVar()
        self.country = StringVar()
        self.ser_pro = StringVar()
        self.number_info = StringVar()

        title = Label(self.root, text="Phone Number Details", font=("Goudy Old Style",35,"bold"), bd = 5, relief = RIDGE)
        title.pack(fill = X)

        decs = Label(self.root,
                     text="Please Enter The Country Code Before Your Number.",
                     font=("Goudy Old Style", 14, 'bold'), bg="#FFD966", fg="#262626")
        decs.place(x=0, y=66, relwidth=1)

        """Labels"""
        lbl_number = Label(self.root, text="Phone Number :", font=('times new roman', 15, 'bold'), bg = "white")
        lbl_number.place(x=20, y=115)

        lbl_country = Label(self.root, text="Country :", font=('times new roman', 15, 'bold'), bg="white")
        lbl_country.place(x=20, y=155)

        lbl_service_provider = Label(self.root, text="Service Provider :", font=('times new roman', 15, 'bold'), bg="white")
        lbl_service_provider.place(x=20, y=195)

        """Entry Fields"""

        txt_number = Entry(self.root, font=('times new roman', 12, 'bold'), bg='lightyellow', width=29, textvariable=self.number)
        txt_number.place(x=230, y=115)

        txt_country = Entry(self.root, font=('times new roman', 12, 'bold'), bg='lightyellow', width=29, textvariable=self.country)
        txt_country.place(x=230, y=155)

        txt_ser_pro = Entry(self.root, font=('times new roman', 12, 'bold'), bg='lightyellow', width=29, textvariable=self.ser_pro)
        txt_ser_pro.place(x=230, y=195)

        btn_reveal=Button(self.root,text="Reveal Information",font=("times new roman",18,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white",command=self.reveal_information)
        btn_reveal.place(x=150,y=250,height=30,width=220)

    def reveal_information(self):
        ch_number = phonenumbers.parse(self.number.get(), "CH")
        country =  str(geocoder.description_for_number(ch_number, "en"))
        self.country.set(country)

        ser_pro_number = phonenumbers.parse(self.number.get(), "RO")
        ser_pro = str(carrier.name_for_number(ser_pro_number, "en"))
        self.ser_pro.set(ser_pro)


root = Tk()
obj = Phone_Number_Details(root)
root.mainloop()