import socket
from tkinter import *

root = Tk()

def send(listbox, entry, s):
    message = entry.get()
    listbox.insert('end', message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    receive(listbox, s)

def receive(listbox, s):
    message = s.recv(1000)
    listbox.insert('end',"Server: "+message.decode("utf-8"))

entry = Entry(root)
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry, s))
button.pack(side=BOTTOM)
rbutton = Button(root, text="Receive", command=lambda: receive(listbox, s))
rbutton.pack(side=BOTTOM)

root.title("Client")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME, PORT))

root.mainloop()


