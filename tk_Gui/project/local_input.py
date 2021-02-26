from tkinter import *

import localization as lz

# master = Tk()
# var = IntVar()
# master.title("LIM")

class local_input:
    def __init__(self, master):
        l1=Label(master, text="XL:").grid(row=0,column=0)
        l2=Label(master, text="XR:").grid(row=1,column=0)
        l3=Label(master, text="YL:").grid(row=2,column=0)
        l4=Label(master, text="YR:").grid(row=3,column=0)

        self.e1 = Entry(master,highlightcolor='red', highlightthickness=1)
        self.e2 = Entry(master,highlightcolor='red', highlightthickness=1)
        self.e3 = Entry(master,highlightcolor='red', highlightthickness=1)
        self.e4 = Entry(master,highlightcolor='red', highlightthickness=1)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)

        # photo = PhotoImage(file='out.gif')
        # label = Label(image=photo)
        # label.image = photo
        # label.grid(row=0, column=2, columnspan=2, rowspan=4, sticky=W+E+N+S, padx=10, pady=10)

        Label(master, text="Please only enter the number \n (ie.0.8,-1)").grid(row=4, column=1)














