## AUTHOR - Sukanth ##
## BUS LOCATOR APP ##

import csv   # to work with data.csv file
from addBusStop import addBusStop_list  # using addBusStop_list (list var) from addBusStop program
csv.register_dialect('myDialect',delimiter=',')    #registering csv dialect

import requests     #to request location details from third-party website by sending IP address

import warnings     # to avoid displaying unwanted warnings(DeprecationWarning)
warnings.filterwarnings("ignore",category=DeprecationWarning)

import tkinter as tk    #importing tkinter module
from tkinter import *
from PIL import Image, ImageTk  #importing pillow module 

from ttkwidgets.autocomplete import AutocompleteCombobox #importing AutocompleteCombobox using ttkwidgets module

class App(tk.Tk):       # every functions are declared inside this class
    def __init__(self):     
        super().__init__()

        #window designs
        self.title("Bus Locator App")
        self.iconbitmap('assets/iconIMG.ico')
        self.configure(bg="#85C1E9")
        #setting app screen size--------------------------------------------------
        app_width = 400
        app_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)

        self.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        self.resizable(False, False) #disabling resisizing the app window

        #second window
        def secondWindow(index):
            window2 = Tk()
            #window designs
            window2.title("Bus Locator App")
            window2.iconbitmap('assets/iconIMG.ico')
            window2.configure(bg="#85C1E9")
            #setting app screen size--------------------------------------------------
            window2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            window2.resizable(False, False) #disabling resisizing the app window

            #label bus no
            bus_no = "Bus No.: " + list_bus[index][2]
            bus_no_label = Label(window2,text=bus_no,bg="#85C1E9",font="Arial 18 bold")
            bus_no_label.place(x=40,y=40)

            #list the stops and timings
            list_bus_len = len(list_bus[index])

            alignY = 80
            
            for i in range(3,list_bus_len,2):
                busStop = Label(window2,text=list_bus[index][i],bg="#85C1E9",font="Arial 9 bold")
                busStop.place(x=40,y=alignY)
                busTime = Label(window2,text=" - " + list_bus[index][i+1],bg="#85C1E9",font="Arial 9 bold")
                busTime.place(x=250,y=alignY)
                alignY += 25

            #bus location button
            def BusLocation():
                ip_address = list_bus[index][0]
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                location_data = {
                    "ip": ip_address,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country_name"),
                    "latitude": response.get("latitude"),
                    "longitude": response.get("longitude")
                }
                country = Label(window2,text="Country    : " + location_data["country"], font="Arial 9 bold",bg="#85C1E9")
                country.place(x=40,y=alignY+65)
                state = Label(window2,text="State         : " + location_data["region"], font="Arial 9 bold",bg="#85C1E9")
                state.place(x=40,y=alignY+85)
                city = Label(window2,text="City            : " + location_data["city"], font="Arial 9 bold",bg="#85C1E9")
                city.place(x=40,y=alignY+105)
               
                latitude_entry = Entry(window2,font="Arial 9 bold",bg="#85C1E9",bd=0,width=20)
                latitude_entry.insert(0,"Latitude    : " + str(location_data["latitude"]))
                latitude_entry.config(state="readonly")
                latitude_entry.place(x=40,y=alignY+125)

                longitude_entry = Entry(window2,font="Arial 9 bold",bg="#85C1E9",bd=0,width=20)
                longitude_entry.insert(0,"Longitude : " + str(location_data["longitude"]))
                longitude_entry.config(state="readonly")
                longitude_entry.place(x=40,y=alignY+145)

                #note
                noteString1 = "NOTE: KINDLY COPY THE LATITUDE AND LONGITUDE "
                noteString2 = "AND PASTE IN GOOGLE MAPS TO VIEW THE BUS LOCATION"
                note1 = Label(window2,text=noteString1, font="ArialBlack 8 bold",bg="#85C1E9")
                note1.place(x=40,y=alignY+175)
                note2 = Label(window2,text=noteString2, font="ArialBlack 8 bold",bg="#85C1E9")
                note2.place(x=40,y=alignY+195)

            busLoc = Button(window2,text="Click here to view Bus Location",bg="#1b1f1e",bd=1,fg="#fff",font="Arial 11 bold",command=BusLocation)
            busLoc.place(x=40,y=alignY+20)
        
        #app name
        appName = Label(self, text = "BUS LOCATOR APP", font="Arial 20 bold", bg="#85C1E9")
        appName.place(x=90,y=40)
        
        #app image
        global new_img
        img=Image.open("assets/appIMG.png")
        resized = img.resize((50,70), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized)
        mylabel = Label(self,image=new_img,bg="#85C1E9")
        mylabel.place(x=30,y=28)

        #from and to places
        fromLabel = Label(self, text="From", font="Arial 10 bold",bg="#85C1E9")
        fromLabel.place(x=50,y=130)
        from_place = AutocompleteCombobox(self,font="Arial 16 bold",width=25,completevalues=addBusStop_list)
        from_place.place(x=50,y=150)
        from_place.focus()

        toLabel = Label(self, text="To", font="Arial 10 bold",bg="#85C1E9")
        toLabel.place(x=50,y=180)
        to_place = AutocompleteCombobox(self,font="Arial 16 bold",width=25,completevalues=addBusStop_list)
        to_place.place(x=50,y=200)

        #search stops
        def checkStop() :   

            def clear():
                clearButton['state'] = DISABLED
                search['state'] = NORMAL
                from_place.delete(0,END)
                to_place.delete(0,END)
                from_place.focus()
                for item in frame1.winfo_children():
                    item.destroy()
                    
            
            search['state'] = DISABLED
            search.place(x=120,y=240)
            clearButton = Button(self,text="Clear",bg="#1b1f1e",bd=1,fg="#fff",font="Arial 11 bold",padx=10,command=clear)
            clearButton.place(x=210,y=240)

            fromPlaceNEW = from_place.get()
            toPlaceNEW = to_place.get()
            global list_bus
            list_bus = []
            f = open('data/data.csv','r')
            reader = csv.reader(f,dialect='myDialect')
            for row in reader:
                found1 = 0
                small_row = []
                for x in range(0,len(row)):
                    small_row.append(row[x].lower())
                length = len(row)
                for i in range(0,length):
                    if (fromPlaceNEW.lower() not in small_row) or (toPlaceNEW.lower() not in small_row):
                        break
                    if fromPlaceNEW.lower() == row[i].lower():
                        found1 = 1
                    if toPlaceNEW.lower() == row[i].lower():
                        found1 += 1
                if found1 == 2:
                    list_bus.append(row)
            f.close()
            #print(list_bus)

            #available busses
            avail_bus = Label(self,text="Available Busses :-",font="Arial 14 bold",bg="#85C1E9")
            avail_bus.place(x=50,y=288)

            list_count = len(list_bus)
            #print(list_count)

            frame1 = Frame(self,bd=2,bg="#85C1E9")
            frame1.place(x=50,y=310)
            r = 0

            for i in range(0,list_count):
                global busNo
                busNo = list_bus[i][2]
                busStart = list_bus[i][3]
                endStopIndex = len(list_bus[i])-2
                busEnd = list_bus[i][endStopIndex]
                busTime = list_bus[i][4]
                busString = busStart + " to " + busEnd + " - " + busTime

                busButton = Button(frame1,text=busNo,bg="#1b1f1e",bd=1,fg="#fff",font="Arial 8 bold",width=3,command=lambda i=i:secondWindow(i))  # control goes to secondWindow function
                busButton.grid(row=r,column=0)

                busStringLabel = Label(frame1,text=busString,font="Arial 10 bold",bg="#85C1E9",padx=15,pady=6)
                busStringLabel.grid(row=r,column=1)

                r+= 1

            if list_count < 1:
                exceptionLabel = Label(frame1,text="*No Busses for this stops or enter correct spelling",bg="#85C1E9",font="Arial 8 bold")
                exceptionLabel.grid(row=r,column=0)

        search = Button(self,text="Search",bg="#1b1f1e",bd=1,fg="#fff",font="Arial 11 bold",command=checkStop)
        search.place(x=150,y=240)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()