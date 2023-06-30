PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ROUND_NUM = 0
TIMER = None

from tkinter import *
import math

def start_timer():
    global ROUND_NUM
    ROUND_NUM += 1
    if ROUND_NUM % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        title.config(text="BREAK" ,fg="red", bg=YELLOW,font=(FONT_NAME,50))    
    elif ROUND_NUM % 2 == 0 and ROUND_NUM != 8:
        count_down(SHORT_BREAK_MIN*60)
        title.config(text="BREAK" ,fg="pink", bg=YELLOW,font=(FONT_NAME,50))  
    else:
        count_down(WORK_MIN*60)
        title.config(text="WORK" ,fg="green", bg=YELLOW,font=(FONT_NAME,50))      

def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000,count_down,count-1)
    else:
        checks = math.floor(ROUND_NUM/2)
        check.config(text=f"{'✔'*checks}",fg="green",bg=YELLOW,font=(FONT_NAME,10))
        start_timer()    

def reset_timer():
    window.after_cancel(TIMER)
    title.config(text="TIMER" ,fg="green", bg=YELLOW,font=(FONT_NAME,50))
    canvas.itemconfig(timer_text,text="00:00")
    global ROUND_NUM
    ROUND_NUM = 0 
    check.config(text=f"",fg="green",bg=YELLOW,font=(FONT_NAME,10))


window = Tk()
window.title("Pomodoro")
window.config(padx=150,pady=100,bg=YELLOW)

title = Label(text="TIMER" ,fg="green", bg=YELLOW,font=(FONT_NAME,50))
title.grid(column=1,row=0)

canvas = Canvas(width=300,height=300,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(150,112,image=image)
timer_text = canvas.create_text(150,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start=Button(text="Start" ,highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)


check = Label(fg="green",bg=YELLOW,font=(FONT_NAME,10))
check.grid(column=1,row=2)

window.mainloop()
