from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Interesting stuff...', 'This would be the place to put some good data.')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print(' =: - P ')

root.mainloop()