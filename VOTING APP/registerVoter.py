import tkinter as tk
import dframe as df
import Admin as adm
from tkinter import ttk
from Admin import *
from tkinter import *
from dframe import *
from PIL import ImageTk, Image 

def reg_server(root,frame1,aadhar_num,name,age,sex,zone,city,passw):
    if passw in ['', ' ']:
        msg = Message(frame1, text="Error: Missing Fields", width=500)
        msg.grid(row = 10, column = 0, columnspan = 5)
        return -1

    vid = df.taking_data_voter(aadhar_num,name,age,sex,zone,city,passw)
    for widget in frame1.winfo_children():
        widget.destroy()
    txt = "Registered Voter with\n\n VOTER I.D. = " + str(vid)
    Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)


def Register(root,frame1):

    root.title("Register Voter")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Register Voter", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, bg="#5B85AA",text="").grid(row = 1,column = 0)
    Label(frame1, bg="#5B85AA",text="Aadhar Number:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, bg="#5B85AA",text="Name:         ", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    Label(frame1, bg="#5B85AA",text="Sex:              ", anchor="e", justify=LEFT).grid(row = 4,column = 0)
    Label(frame1, bg="#5B85AA",text="Age:           ", anchor="e", justify=LEFT).grid(row = 5,column = 0)
    Label(frame1, bg="#5B85AA",text="Zone:             ", anchor="e", justify=LEFT).grid(row = 6,column = 0)
    Label(frame1, bg="#5B85AA",text="City:             ", anchor="e", justify=LEFT).grid(row = 7,column = 0)
    Label(frame1, bg="#5B85AA",text="Password:   ", anchor="e", justify=LEFT).grid(row = 8,column = 0)

    aadhar_num = tk.StringVar()
    name = tk.StringVar()
    sex = tk.StringVar()
    age = tk.StringVar()
    zone = tk.StringVar()
    city = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = aadhar_num).grid(row = 2, column = 2)
    e2 = Entry(frame1, textvariable = name).grid(row = 3, column = 2)
    e5 = Entry(frame1, textvariable = age).grid(row = 5, column = 2)
    e6 = Entry(frame1, textvariable = zone).grid(row = 6, column = 2)
    e7 = Entry(frame1, textvariable = city).grid(row = 7, column = 2)
    e8 = Entry(frame1, textvariable = password).grid(row = 8, column = 2)

    e4 = ttk.Combobox(frame1, textvariable = sex, width=17)
    e4['values'] = ("Male","Female","Transgender")
    e4.grid(row = 4, column = 2)
    e4.current()

    reg = Button(frame1, bg="#F46036",text="Register", command = lambda: reg_server(root, frame1, aadhar_num.get(), name.get(), sex.get(), age.get(), zone.get(), city.get(), password.get()), width=15)
    Label(frame1, bg="#5B85AA",text="").grid(row = 10,column = 0)
    reg.grid(row = 9, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    root.configure(bg='#414770')
    frame1 = Frame(root)
    frame1.configure(bg="#5B85AA")
    Register(root,frame1)
