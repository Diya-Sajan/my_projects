import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin
from PIL import ImageTk, Image  
# from voter import ff

c1 = "#FF6700"
c2 = "white"
def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    Button(frame2, text="Home", bg=c2, command = lambda: Home(root, frame1, frame2)).grid(row=0,column=0)
    Label(frame2, bg=c2,text="                                                                         ").grid(row = 0,column = 1)
    Label(frame2, bg=c2,text="                                                                         ").grid(row = 0,column = 2)
    Label(frame2, bg=c2,text="         ").grid(row = 1,column = 1)
    frame2.pack(side=TOP)

    root.title("Home")

    Label(frame1, bg=c2,text="Home",font=('Proxima Nova', 28, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    #Admin Login
    admin = Button(frame1, bg=c1, text="Admin Login", width=15, command = lambda: AdmLogin(root, frame1))

    #Voter Login
    voter = Button(frame1, bg=c1, text="Voter Login", width=15, command = lambda: voterLogin(root, frame1))

    #New Tab
    newTab = Button(frame1, bg=c1, text="New Window", width=15, command = lambda: sb_p.call('start python homePage.py', shell=True))

    Label(frame1, bg=c2, text="").grid(row = 1,column = 0)
    Label(frame1, bg=c2, text="").grid(row = 2,column = 0)
    Label(frame1, bg=c2, text="").grid(row = 4,column = 0)
    Label(frame1, bg=c2, text="").grid(row = 6,column = 0)
    admin.grid(row = 3, column = 1, columnspan = 2)
    voter.grid(row = 5, column = 1, columnspan = 2)
    newTab.grid(row = 7, column = 1, columnspan = 2)
    frame1.configure(bg=c2)
    frame2.configure(bg=c2)

    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.title("MyVote") 
    root.geometry("1300x750")
    root.resizable(False,False)
    bg=PhotoImage(file="17717.png")
    bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    label1=Label(root,text="Welcome To MyVote",fg="#028A0f",bg="white",font=("Mocrosoft YaHei UI Bold",46))
    label1.pack()
    label2=Label(root,text="You can vote for your party and your favourate candidate from anywhere",fg="#028A0f",bg="white",font=("Mocrosoft YaHei UI Light",14))
    label2.pack()
    
    frame1 = Frame(root)
    frame2 = Frame(root)
    Home(root, frame1, frame2)  


if __name__ == "__main__":
    new_home()
