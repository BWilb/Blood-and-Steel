from time import strftime
from tkinter import *
from tkinter.ttk import *
from datetime import datetime, timedelta
import time

"""root = Tk()

root.title("Clock")

date = datetime(1914, 1, 1)
def time2(date):
    string = strftime("%H:%M:%S %p")
    label.config(text=date)
    label.after(50, time2)


label = Label(root, font=("ds-digital", 80), background="blue", foreground="black")

label.pack(anchor="center")
time2()
mainloop()

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
for i in range(1, 60):
    time2(date)
    time.sleep(0.5)
    date += timedelta(days=1)

mainloop()
"""
date = datetime(1914, 1, 1, 0, 0, 0)


date_string = time.asctime(date.year)
print(date_string)