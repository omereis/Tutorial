import tkinter as tk
import os
from tkinter import ttk

def on_button_click():
    print('Button clicked')

def on_TTT_click(option):
    print(option)

def set_window (root):
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

def main():
    root = tk.Tk()
    msg = tk.Label (root, text='This is a text')
    msg.pack()
    root.title('TkInter Tutorial Session 1')
    ttk.Label(root, text='Themed Label').pack()
    label = ttk.Label(root)
    label.config(text='TTk Label')
    label.pack()
    button = ttk.Button(root, text='Click Me', command=on_button_click)
    button.pack()
    set_window (root)
    path = os.getcwd()
    print(f'Current Directory: {path}')
    photo = tk.PhotoImage(file='./Python.png')
    print('Photo loaded')
    image_label = ttk.Label(
            root,
            text='Pyton',
            image=photo,
            padding=5,
            compound='left'
        )
    image_label.pack()
    print('Can you see the picture?')

    root.mainloop()

if __name__ == '__main__':
    main()