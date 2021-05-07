# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import scrolledtext
import socket
import threading


def c_clicked():

    res = "Connected {}".format(gip.get())
    lbl.configure(text=res)
    s.connect((gip.get(), PORT))
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()


def s_clicked():
    message = f':msg:{msg.get()}'
    s.send(message.encode('utf-8'))


def receive():
    while True:
        try:
            message = s.recv(1024).decode('utf-8')
            chat.insert(tkinter.INSERT, message)
        except:
            print("An error occured!")
            s.close()
            break


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


window = Tk()
PORT = 9090
window.title("DnD chat")
window.geometry('800x600')


lbl = Label(window, text="Enter IP: ")
lbl.grid(column=0, row=0)


gip = Entry(window, width=80)
gip.grid(column=1, row=1)
gip.focus()


con = Button(window, text="Connect", command=c_clicked)
con.grid(column=2, row=1)


chat = scrolledtext.ScrolledText(window, width=70, height=30)
chat.grid(column=1, row=2)


lbl1 = Label(window, text="Enter message: ")
lbl1.grid(column=0, row=3)


msg = Entry(window, width=80)
msg.grid(column=1, row=4)


snd = Button(window, text="Send", command=s_clicked)
snd.grid(column=2, row=4)


window.mainloop()
