from tkinter import *
import sys

s = sys.version

root = Tk()
# creat the widge
lblHi = Label(root, text='Hi There')
lblHeb = Label(root, text='שלום עליכם')

lblHi.grid(row=1, column=2)
lblHeb.grid(row=2, column=3)

#Start the main loop
root.mainloop()
