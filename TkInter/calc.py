from tkinter import *
import numbers

root = Tk()
root.title ('Calculator')

txtbx = Entry (root, width=35, borderwidth=3)
txtbx.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

aButtons=[]

nOperand1=nOperand2=0
fOperand1=True
#------------------------------------------------------------------------------
def init_calc_vars():
    global nOperand1, nOperand2, fOperand1
    nOperand2=nOperand1=0
    fOperand1=True
#------------------------------------------------------------------------------
def set_text (nResult):
    global txtbx
    txtbx.delete(0,END)
    txtbx.insert (0, str(nResult))
#------------------------------------------------------------------------------
def add_digit (num, nDigit):
    #print(f'num={num}, nDigit={nDigit}')
    try:
        num *= 10
        num += int(nDigit)
    except Exception as e:
        print (f'Runtime error:{e}')
        num = 777#nDigit
    #print(f'num={num}, nDigit={nDigit}')
    return (num)
lbl = Label (root)
lbl.grid(row=1, column=0, columnspan=3)
#lbl.config(bg='yellow')

#------------------------------------------------------------------------------
def on_button_click(arg):
    global nOperand1, nOperand2, fOperand1, lbl
    try:
        nArg = int(arg)
    except:
        nArg = arg
    #print('=============================================')
    #print(f'nOperand1={nOperand1}')
    if (isinstance(nArg,numbers.Number)):
        if fOperand1:
            nOperand1 = add_digit (nOperand1, arg)
            set_text (nOperand1)
            lbl.config(text=str(nOperand1))
        else:
            nOperand2 = add_digit (nOperand2, arg)
    else:
        if arg == '+':
            if fOperand1:
                fOperand1 = False
                lbl.config(text=str(nOperand1) + '+')
            else:
                nOperand1 += nOperand2
                nOperand2 = 0
        elif arg == 'C':
            init_calc_vars()
            lbl.config(text='')
            set_text('')
        elif arg == '=':
            nResult = nOperand1 + nOperand2
            set_text (nResult)
    print('+++++++++++++++++++++++++++++++++++++++++++++++')
    #print(f'arg={arg}')
    #print(f'type(arg)={type(arg)}')
    print(f'nOperand1={nOperand1}')
    print(f'nOperand2={nOperand2}')
    return
#------------------------------------------------------------------------------
def on_widget_click(event):
    on_button_click(event.widget.cget('text'))
#------------------------------------------------------------------------------
for n in range(9):
    #btn = Button(root, text=str(n+1), padx=40, pady=20, command=on_button_click)
    txt = str(n+1)
    btn = Button(root, text=txt, padx=40, pady=20, command=lambda arg=txt: on_button_click(arg))
    btn.grid(row=2 + (int)(n / 3), column=n % 3)
    aButtons.append(btn)
rowButton=4
btn = Button(root, text='0', padx=40, pady=20, command=lambda: on_button_click(0))
btn.grid(row=rowButton+1, column=1)
aButtons.append(btn)

btnPlus = Button(root, text='+', padx=40, pady=20)
btnPlus.grid(row=rowButton+1, column=0)
# source:
# https://coderslegacy.com/python/tkinter-which-widget-called-function-event/
btnPlus.bind('<Button-1>', on_widget_click)
aButtons.append(btnPlus)

btn = Button(root, text='C', padx=40, pady=20)
btn.grid(row=rowButton+1, column=2)
btn.bind('<Button-1>', on_widget_click)
aButtons.append(btn)

btn = Button(root, text='=', padx=40, pady=20)
btn.grid(row=rowButton+2, column=1)
btn.bind('<Button-1>', on_widget_click)
aButtons.append(btn)

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


#Start the main loop
root.mainloop()
