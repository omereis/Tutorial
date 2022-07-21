import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    msg = tk.Label (root, text='This is a text')
    msg.pack()
    root.title('TkInter Tutorial Session 1')
    ttk.Label(root, text='Themed Label').pack()
    label = ttk.Label(root)
    label.config(text='TTk Label')
    label.pack()
    #root.geometry('600x400+50+50')
    window_width = 600
    window_height = 400

# get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

# find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(True, True)
    root.iconbitmap ('/Users/Omer/Documents/Tutorials/TkInter/bumps.ico')
    root.mainloop()

if __name__ == '__main__':
    main()