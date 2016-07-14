from tkinter import *

root = Tk() # creates the container calling it root

one = Label(root, text="One", bg="red", fg="white") # there seem to be color issues with macs
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X) # dynamically fills horizontally
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y) # dynamically fills vertically

root.mainloop() # keeps the container open - continues the loop until broken by closing