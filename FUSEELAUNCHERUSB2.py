import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import *
import os
import webbrowser
import pathlib

payload = 'payload.bin'

#How to launch ? --> https://github.com/Qyriad/fusee-launcher/wiki/Instructions-(Windows)

def makeProgress(V):
    PROGRESSBAR['value'] = PROGRESSBAR['value'] + V
    root.update_idletasks()


def menosProgress(V):
    PROGRESSBAR['value'] = PROGRESSBAR['value'] - V
    root.update_idletasks()


def payload():
    global e
    global payload
    if e == None:
        return('0')
    else:
        payload = e.get()

def launching():
    os.system('sudo python3 fusee-launcher.py --override-checks %s' % payload)
    makeProgress(50)


def getCheckboxValue():
    global checkedOrNot
    checkedOrNot = cbVariable.get()


def btnClickFunction():
    getCheckboxValue()
    webbrowser.open('http://example.com')


def launch():
    run = True
    getCheckboxValue()
    if checkedOrNot == 0:
        mb.showerror("License", "Sorry, license is unchecked")
    if checkedOrNot == 1:
        makeProgress(25)
        path = pathlib.Path('history.txt')
        done = path.exists()
        if done == False:
            os.system('sudo python3 patch.py')
            f = open("history.txt", "w+")
            f.write("System Patched !\nDO NOT ERASE THIS ELSE YOUR SYSTEM CAN GET DAMMAGED , I WARNED YOU")
            f.close()
        else:
            mb.showwarning("System", "System should be already patched, launching fusee gelee")
        makeProgress(25)
        launching()


root = Tk()
cbVariable = tk.IntVar()

e = Entry(root)
e.pack()
e.focus_set()

root.geometry('768x522')
root.configure(background='#FAEBD7')
root.title('FUSEE LAUNCHER UBUNTU AND DEBIAN USB 2.0')

PROGRESSBAR_style = ttk.Style()
PROGRESSBAR_style.theme_use('clam')
PROGRESSBAR_style.configure('PROGRESSBAR.Horizontal.TProgressbar', foreground='#FF4040', background='#FF4040')

PROGRESSBAR = ttk.Progressbar(root, style='PROGRESSBAR.Horizontal.TProgressbar',orient='horizontal', length=519, mode='determinate', maximum=100, value=1)
PROGRESSBAR.place(x=189, y=93)

Label(root, text='Progression', bg='#FAEBD7', font=('arial', 12, 'normal')).place(x=185, y=67)
Label(root, text='payload(by default : payload.bin', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=320, y=16)

CHECK = Checkbutton(root, text='read and accepted',variable=cbVariable, bg='#FF4040', font=('arial', 12, 'normal'))
CHECK.place(x=418, y=293)

Button(root, text='License', bg='#98F5FF', font=('arial', 12, 'normal'),command=btnClickFunction).place(x=331, y=291)

Button(root, text='launch', bg='#7FFF00', font=('arial', 12, 'normal'), command=launch).place(x=186, y=109)

root.mainloop()
