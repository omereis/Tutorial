from tkinter import *

root = Tk()

#txtbx = Entry (root, width=15, bg='Blue', fg="white", borderwidth=3)
txtbx = Entry (root, width=15, borderwidth=3)
txtbx.labelText ='Guess'
txtbx.insert(20, "What did you kill?")

lbl = Label (root, text=txtbx.get())
lbl.pack()

def on_click():
    global txtbx, lbl
    s = lbl.cget('text')
    if (s == 'get'):
        s = 'set'
    else:
        s = 'get'
    print(f's = {s}')
    lbl.config(text=s)#'get')
    lbl.pack()
    print (f'Width: {txtbx.winfo_width()}')


txtbx.pack()

btn = Button (root, text="Submit!", command=on_click)

txtbx.pack()
btn.pack()

#Start the main loop
root.mainloop()
