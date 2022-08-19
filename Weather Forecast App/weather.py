from threading import local
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather Forecast App")
root.geometry("890x470+300+100")
root.config(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city = textfield.get() 
    
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    time_zone.config(text=result)
    long_lat.config(text=f"   Latitude:{round(location.latitude, 4)}°N\nLongitude:{round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #=====Weather=====
    api = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=d583808e8dee8d7e9fd2e9caa9db3177"
    json_data = requests.get(api).json()

    #=====Current=====
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))

    #=====First Cell=====
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']

    photo1 = ImageTk.PhotoImage(file=f'icon/{firstdayimage}@2x.png')
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day:{tempday1}°C\nNight:{tempnight1}°C")
    #=====Second Cell=====
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']

    img = (Image.open(f'icon/{seconddayimage}@2x.png'))
    resized_image = img.resize((75, 75))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.config = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day:{tempday2}°C\nNight:{tempnight2}°C")
    #=====Third Cell=====
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    img = (Image.open(f'icon/{thirddayimage}@2x.png'))
    resized_image = img.resize((75, 75))
    photo2 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo2)
    thirdimage.config = photo2

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day:{tempday3}°C\nNight:{tempnight3}°C")
    #=====Fourth Cell=====
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    img = (Image.open(f'icon/{fourthdayimage}@2x.png'))
    resized_image = img.resize((75, 75))
    photo2 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo2)
    fourthimage.config = photo2

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day:{tempday4}°C\nNight:{tempnight4}°C")
    #=====Fifth Cell=====
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    img = (Image.open(f'icon/{fifthdayimage}@2x.png'))
    resized_image = img.resize((75, 75))
    photo2 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo2)
    fifthimage.config = photo2

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day:{tempday5}°C\nNight:{tempnight5}°C")
    #=====Sixth Cell=====
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    img = (Image.open(f'icon/{sixthdayimage}@2x.png'))
    resized_image = img.resize((75, 75))
    photo2 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo2)
    sixthimage.config = photo2

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day:{tempday6}°C\nNight:{tempnight6}°C")
    #=====Seventh Cell=====
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img = (Image.open(f'icon/{seventhdayimage}@2x.png'))
    resized_image = img.resize((75, 75))
    photo2 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo2)
    seventhimage.config = photo2

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day:{tempday7}°C\nNight:{tempnight7}°C")

    #=====Days=====
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

#=====Icon=====
image_icon = PhotoImage(file='images/logo.png')
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file='images/Rounded Rectangle 1.png')
Label(root, image=Round_box, bg="#57adff").place(x=30,y=110)

#=====Labels=====
label1 = Label(root, text='Temperature :- ', font=('Helvetica', 11), fg='white', bg='#203243').place(x=50, y=120)
label2 = Label(root, text='Humidity :- ', font=('Helvetica', 11), fg='white', bg='#203243').place(x=50, y=140)
label3 = Label(root, text='Pressure :- ', font=('Helvetica', 11), fg='white', bg='#203243').place(x=50, y=160)
label4 = Label(root, text='Wind Speed :- ', font=('Helvetica', 11), fg='white', bg='#203243').place(x=50, y=180)
label5 = Label(root, text='Decription :- ', font=('Helvetica', 11), fg='white', bg='#203243').place(x=50, y=200)

#=====Search Box=====
Search_image = PhotoImage(file='images/Rounded Rectangle 3.png')
myimage = Label(image=Search_image, bg='#57adff').place(x=270, y=120)

weat_image = PhotoImage(file='images/Layer 7.png')
weather_image = Label(root, image=weat_image, bg='#203243').place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 20, 'bold'),bg='#203243', border=0, fg='white')
textfield.place(x=370, y=127)

Search_icon = PhotoImage(file='images/Layer 6.png')
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor='hand2', bg='#203243',activebackground='#203243', command=getWeather).place(x=645, y=124)

#=====Bottom Box=====
frame = Frame(root, width=900, height=180, bg='#212120')
frame.pack(side=BOTTOM)

#=====Bottom Boxes=====
firstbox = PhotoImage(file='images/Rounded Rectangle 2.png')
secondbox = PhotoImage(file='images/Rounded Rectangle 2 copy.png')

Label(frame, image=firstbox, bg='#212120').place(x=30, y=20)
Label(frame, image=secondbox, bg='#212120').place(x=300, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=400, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=500, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=600, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=700, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=800, y=30)

#=====Clock (here we will place time)=====
clock = Label(root, font=('Helvetica', 30, 'bold'), fg='white', bg='#57adff')
clock.place(x=30, y=20)

#=====Timezone=====
time_zone = Label(root, font=('Helvetica', 20, 'bold'), fg='white', bg='#57adff')
time_zone.place(x=700, y=20)
long_lat = Label(root, font=('Helvetica', 10, 'bold'), fg='white', bg='#57adff',justify=CENTER)
long_lat.place(x=700, y=55)

#=====Temperature, Humidity, Pressure, Wind Speed, Description (THPWD)=====
t=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
t.place(x=150, y=120)
h=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
h.place(x=150, y=140)
p=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
p.place(x=150, y=160)
w=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
w.place(x=150, y=180)
d=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
d.place(x=150, y=200)

#=====First Cell=====
firstframe = Frame(root, width=230, height=131, bg='#282829')
firstframe.place(x=35, y=315)

day1 = Label(firstframe, font=('arial', 15), bg="#282829", fg="#fff")
day1.place(x=105, y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, bg='#282829',fg='#57adff', font=('arial', 13, 'bold'))
day1temp.place(x=110, y=50)
#=====Second Cell=====
secondframe = Frame(root, width=71, height=115, bg='#282829')
secondframe.place(x=305, y=325)

day2 = Label(secondframe, bg="#282829", fg="#fff", font=('arial',10))
day2.place(x=0, y=5)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=0, y=25)

day2temp = Label(secondframe, bg='#282829', fg='#fff')
day2temp.place(x=0, y=85)
#=====Third Cell=====
thirdframe = Frame(root, width=71, height=115, bg='#282829')
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe, bg="#282829", fg="#fff", font=('arial',10))
day3.place(x=0, y=5)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=0, y=25)

day3temp = Label(thirdframe, bg='#282829', fg='#fff')
day3temp.place(x=0, y=85)
#=====Fourth Cell=====
fourthframe = Frame(root, width=71, height=115, bg='#282829')
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, bg="#282829", fg="#fff", font=('arial',10))
day4.place(x=0, y=5)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=0, y=25)

day4temp = Label(fourthframe, bg='#282829', fg='#fff')
day4temp.place(x=0, y=85)
#=====Fifth Cell=====
fifthframe = Frame(root, width=71, height=115, bg='#282829')
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, bg="#282829", fg="#fff", font=('arial',10))
day5.place(x=0, y=5)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=0, y=25)

day5temp = Label(fifthframe, bg='#282829', fg='#fff')
day5temp.place(x=0, y=85)
#=====Sixth Cell=====
sixthframe = Frame(root, width=71, height=115, bg='#282829')
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, bg="#282829", fg="#fff", font=('arial',10))
day6.place(x=0, y=5)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=0, y=25)

day6temp = Label(sixthframe, bg='#282829', fg='#fff')
day6temp.place(x=0, y=85)
#=====Seventh Cell=====
seventhframe = Frame(root, width=71, height=115, bg='#282829')
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, bg="#282829", fg="#fff", font=('arial',10))
day7.place(x=0, y=5)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=0, y=25)

day7temp = Label(seventhframe, bg='#282829', fg='#fff')
day7temp.place(x=0, y=85)

root.mainloop()