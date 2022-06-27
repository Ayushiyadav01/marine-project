from cProfile import label
from tkinter import *
from math import *
import serial
import time

ser = serial.Serial('COM5', 4800, timeout=2)

def show_data():
    global UTC, long, lat
    while True:   
        data_raw = str(ser.readline())
        data_li = list(data_raw.split(","))
        if (data_li[0]=='b\'$GPGGA'):
            UTC = data_li[1] 
            # print(UTC)  
            l10.config(text=UTC)

            lat = data_li[2]
            # print(lat)
            l8.config(text=lat)
            
            long = data_li[4]
            # print(long)
            l9.config(text=long)
            # break
        # else:
            # l8=Label(window,text="different string")
            # print("different string")
            # break
        window.update()  #screen refresh 
        # show_data()
  
window=Tk()
window.title("GPS")
window.geometry("250x100")
window.minsize(200,100)
window.maxsize(500,500)
global l10
global l8
global l9
l2=Label(window,text="Latitede : ")
l2.grid(row=1,column=0)
l4=Label(window,text="Longitude : ")
l4.grid(row=2,column=0)
l6=Label(window,text="UTC : ")
l6.grid(row=3,column=0)
l8=Label(window,text="lat")
l8.grid(row=1,column=2)
l9=Label(window,text="long")
l9.grid(row=2,column=2)
l10=Label(window,text="utc")
l10.grid(row=3,column=2)
b2=Button(window,text="Start",command=show_data)
b2.grid(row=4,column=2)
window.mainloop()

