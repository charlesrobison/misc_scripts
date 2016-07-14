from tkinter import *

root = Tk() # creates the container calling it root
theLabel = Label(root, text="This is some very basic text for the container")
theLabel.pack() # puts the label into the container
root.mainloop() # keeps the container open - continues the loop until broken by closing
