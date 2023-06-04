from tkinter import *
from server import entry, listbox, send

root = Tk()

entry.pack(side=BOTTOM)
listbox.pack()

button = Button(root, text="Send", command=send)
button.pack(side=BOTTOM)

root.mainloop()
