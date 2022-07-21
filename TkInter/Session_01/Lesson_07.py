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
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

# find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(True, True)

def on_exit_click(root):
    print('Clicked')
    root.quit()

def main():
    root = tk.Tk()
    root.title('TkInter Tutorial Session 1, Lesson #7')
    set_window (root)

    root.iconbitmap ('/Users/Omer/Documents/Tutorials/TkInter/bumps.ico')

    print(f'Current directory: {os.getcwd()}')
    photo = tk.PhotoImage(file='./Session_01/Python.png')
    image_label = ttk.Label(
            root,
            text='Pyton',
            image=photo,
            padding=5,
            compound='left'
        )
    image_label.pack()

    #btnExit = ttk.Button(root, text='Exit', command=lambda:root.quit())
    photo = tk.PhotoImage(file='./Session_01/exit.png')
    btnExit = ttk.Button(root,
                    text='Exit',
                    command=lambda:on_exit_click(root), image=photo)
    btnExit.pack(expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()