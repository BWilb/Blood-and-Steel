"""from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p %Y")
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")

label.pack(anchor="center")
time()

mainloop()"""
import random
import time

"""c = "\"C:\\My Documents\""
print(c)"""

"""tax = round(random.uniform(0.5, 10.0), 2)
print(f"{tax}%")"""
import keyboard

def printhi():
    print("hhi")
pressed = False
while not pressed:
    if keyboard.is_pressed('b'):
        printhi()
        pressed = True
    else:
        print("hi")
    time.sleep(1)