from tkinter import *

root = Tk()

def printName(event):
    print("Button clicked!")

button_1 = Button(root, text="Print something")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
