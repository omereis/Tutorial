from tkinter import *
import sys

s = sys.version

root = Tk()
# creat the widget
lblLesson = Label(root, text='Lesson #2')
lblHi = Label(root, text='Hi There')
lblHeb = Label(root, text='שלום עליכם')

rowHi = 3

def onBtnClick():
    global rowHi, lblHi
    visible = lblHi.winfo_viewable()
    if visible:
        lblHi.grid_remove()
    else:
        lblHi.grid()
    #lbl = Label(text='On Click')
    #rowHi += 1
    #lbl.grid(row=rowHi, column=1)

btn = Button (root, text="כפתור ופרח...", padx=1, pady=5, command=onBtnClick, fg="#0026ff", bg="white")

lblLesson.grid(row=1, column=2)
lblHi.grid(row=rowHi, column=3)
lblHeb.grid(row=4, column=3)
btn.grid(row=3, column=2)
#Start the main loop
root.mainloop()
