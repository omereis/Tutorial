from tkinter import *
import sys

s = sys.version

root = Tk()
# creat the widge
lbl = Label(root, text='Hi There')

#pack the widget
lbl.pack()

#print(dir(lbl))

lbl2 = Label(root, text=s)
lbl2.pack()

lbl3 = Label(root)
lbl3.text="___+++___"
lbl3.pack()

#Start the main loop
root.mainloop()
