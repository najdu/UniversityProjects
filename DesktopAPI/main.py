import os
import tkinter as tk
from PIL import Image, ImageTk

appdata = os.getenv('APPDATA')
path = '{}\\Microsoft\\Windows\\Themes\\TranscodedWallpaper'.format(appdata)

desktop = Image.open(os.path.realpath(path))

#tkinter
root = tk.Tk()

tkdesktop = ImageTk.PhotoImage(desktop, root)
desk = tk.Label(root, image=tkdesktop)
desk.pack()

root.mainloop()