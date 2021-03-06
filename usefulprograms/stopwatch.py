#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
secs = 0
mins = 0
hrs = 0
def printTime(s, m, h):
    canvas.create_rectangle(0, 0, 700, 700, fill="springgreen")
    canvas.create_text(350, 560, text="Press r to Restart; Press l to lap", font=("helvetica", 20))
    if h < 10:
        canvas.create_text(250, 350, text="0" + str(h), font=("helvetica", 40))
    else:
        canvas.create_text(250, 350, text=str(h))
    canvas.create_text(300, 350, text=": ", font=("helvetica", 40))
    if m < 10:
        canvas.create_text(350, 350, text="0" + str(m), font=("helvetica", 40))
    else:
        canvas.create_text(350, 350, text=str(m))
    canvas.create_text(400, 350, text=": ", font=("helvetica", 40))
    if s < 10:
        canvas.create_text(450, 350, text="0" + str(s), font=("helvetica", 40))
    else:
        canvas.create_text(450, 350, text=str(s), font=("helvetica", 40))
    tk.update()
secs = 0
hrs = 0
mins = 0
pSecs = secs
pMins = mins
pHrs = hrs
while True:
    def lap(h, m, s):
        if h < 10:
            print("0"+str(h), end="", flush=True)
        else:
            print(str(h), end="", flush=True)
        print(": ", end="", flush=True)
        if m < 10:
            print("0"+str(m), end="", flush=True)
        else:
            print(str(m), end="", flush=True)
        print(": ", end="", flush=True)
        if s < 10:
            print("0"+str(s))
        else:
            print(s)
    def restart(h, m, s):
        h = 0
        m = 0
        s = 0
    def OPTIONS(event):
        if event.char == "l":
            lap(hrs, mins, secs)
        elif event.char == "r":
            pSecs = 0
            pMins = 0
            pHrs = 0
    canvas.bind_all("<KeyPress-l>", OPTIONS)
    canvas.bind_all("<KeyPress-r>", OPTIONS)
    printTime(secs, mins, hrs)
    time.sleep(1)
    secs = secs + 1
    if secs == 60:
        secs = 0
        mins = mins + 1
    if mins == 60:
        mins = 0
        hrs = hrs + 1
    tk.update()
canvas.mainloop()
