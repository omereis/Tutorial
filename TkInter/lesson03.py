from tkinter import *

root = Tk()

def on_click():
    lbl = Label (root, text='Clicked')
    lbl.pack()

txtbx = Entry (root)
btn = Button (root, text="Submit!", command=on_click)

txtbx.pack()
btn.pack()

#Start the main loop
root.mainloop()
