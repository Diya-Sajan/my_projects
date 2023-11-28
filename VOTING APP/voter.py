import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
from PIL import ImageTk, Image 
import biometric as bio

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, bg="#5B85AA",text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()

def log_server(root,frame1,client_socket,voter_ID,password):
    message = f"{voter_ID} {password}"
    client_socket.send(message.encode()) #2
    
    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Cast"
        failed_return(root,frame1,client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)



def voterLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1,bg="white", text="Voter Login", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1,bg="white", text="").grid(row = 1,column = 0)
    Label(frame1,bg="white" ,text="Voter ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1,bg="white", text="Password:   ", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    # bg="#5B85AA"
    voter_ID = tk.StringVar()
    name = tk.StringVar()
    password = tk.StringVar()
    
    def ff():
        return TRUE

    

    e1 = Entry(frame1, textvariable = voter_ID)
    e1.grid(row = 2,column = 2)
    e3 = Entry(frame1, textvariable = password, show = '*')
    e3.grid(row = 3,column = 2)
    sub = Button(frame1, bg="#F46036", text="Login", width=10, command = lambda: [fun()])
    Label(frame1,bg="white",text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    def fun():
        # print(e1)
        z=bio.face_b_flag(voter_ID.get())
        print(voter_ID.get())
        print("FUNN: ")
        print(z)
        if(z==False):
            message = "Invalid Voter"
            failed_return(root,frame1,client_socket,message)
        else:
            log_server(root, frame1, client_socket, voter_ID.get(), password.get())

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    # root.configure()
    root.configure(bg='#414770')
    frame1 = Frame(root)
    frame1.configure(bg="#5B85AA")
    # frame1.configure()
    voterLogin(root,frame1)
