'''
Desktop Duplicator
6-15-22
Developed by Najdu
'''

# import dependencies
import os
import tkinter as tk
from tracemalloc import start
from PIL import Image, ImageTk
import ctypes
from click import command
import keyboard
import subprocess

# get screen resolution
_user32 = ctypes.windll.user32
WIDTH = _user32.GetSystemMetrics(0)
HEIGHT = _user32.GetSystemMetrics(1)

ICON_SIZE = 64

# set path to desktop background and save in {desktop}
_appdata = os.getenv('APPDATA')
_user = os.getenv('USERPROFILE')

desktopPath = '{}\\Microsoft\\Windows\\Themes\\TranscodedWallpaper'.format(_appdata)
dsk = Image.open(os.path.realpath(desktopPath)).resize((WIDTH, HEIGHT))
mpc = Image.open(os.path.realpath("./mypc.ico")).resize((ICON_SIZE, ICON_SIZE))
trsh = Image.open(os.path.realpath("./recycle.ico")).resize((ICON_SIZE, ICON_SIZE))
expl = Image.open(os.path.realpath("./folder.ico")).resize((ICON_SIZE, ICON_SIZE))

# tkinter starts
root = tk.Tk()

def mycomputer():
    subprocess.Popen('explorer /select,"This PC"')
def trash():
    pass
def explorer():
    subprocess.Popen('explorer')
def startkey():
    keyboard.send('win')

_desktop = ImageTk.PhotoImage(dsk, root)
desktop = tk.Label(root, image=_desktop, width=WIDTH, height=HEIGHT)
desktop.pack()

taskbar = tk.Button(root, width=ICON_SIZE, height=HEIGHT,bg='black', fg='white',
                    text='Start', command=startkey)
taskbar.place(relheight=0.05, relwidth=1.0, rely= 0.95)

_mypc = ImageTk.PhotoImage (mpc, root)
mypc = tk.Button(root, image=_mypc, command=mycomputer)
mypc.place(x=5, y=5)

_trash = ImageTk.PhotoImage (trsh, root)
recyclebin = tk.Button(root, image=_trash, command=trash)
recyclebin.place(x=5, y=96)

_explorer = ImageTk.PhotoImage (expl, root)
folder = tk.Button(root, image=_explorer, command=explorer)
folder.place(x=5, y=187)

root.mainloop()