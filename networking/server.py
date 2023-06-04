import socket
from tkinter import *

root = Tk()

def send(listbox, entry, client):
    message = entry.get()
    listbox.insert('end', "Server: "+message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))

def receive(listbox):
    message_from_client = client.recv(1000)
    listbox.insert('end', "Client: "+message_from_client.decode("utf-8"))

entry = Entry(root)
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry, client))
button.pack(side=BOTTOM)
rbutton = Button(root, text="Receive", command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

root.title("Server")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.bind((HOST_NAME, PORT))
s.listen(4)

client, address = s.accept()

root.mainloop()
