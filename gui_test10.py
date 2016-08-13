# this script does not work as is - image problem

from tkinter import *

root = Tk()

# photo = PhotoImage(file="data2.png")
phot = PhotoImage(file='/Users/robisoc/PycharmProjects/misc_scripts/data2.png')
label = Label(root, image=photo)
label.pack()

root.mainloop()
