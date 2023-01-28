from tkinter import *
import time
from datetime import time as t

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
countdown_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    global countdown_timer
    window.after_cancel(countdown_timer)
    checkmark.config(text="")
    title.config(text="Timer")
    bg_image.itemconfig(timer, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global checkmarks
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8 :
        count_down(long_break_sec)
        title.config(text=f"Long Break", fg=RED)
        reset_timer()
    elif reps % 2 == 0 and reps != 0:
        count_down(short_break_sec)
        title.config(text=f"Short Break", fg=RED)
    else:
        count_down(work_sec)
        title.config(text=f"Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    global checkmarks
    minutes, seconds = divmod(time, 60)

    if seconds < 10:
        seconds = "0" + str(seconds)

    if minutes < 10:
        minutes = "0" + str(minutes)

    bg_image.itemconfig(timer, text=f"{minutes}:{seconds}")

    if time:
        global countdown_timer
        countdown_timer = window.after(2, count_down, time - 1)
    else:
        checkmarks = ""
        for rep in range(0, reps, 2):
            checkmarks += ("✓")

        checkmark.config(text=checkmarks)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

bg_image = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
bg_image.create_image(100, 110, image=tomato_img)
bg_image.grid(column=0, row=1, rowspan=3, columnspan=3)
timer = bg_image.create_text(100, 140, text=f"00:00", font=(FONT_NAME, 35, "bold"))

reset_btn = Button()
reset_btn.config(text="Reset", command=reset_timer, background=YELLOW, highlightbackground=YELLOW, )
reset_btn.grid(column=2, row=5)

start_btn = Button()
start_btn.config(text="Start", command=start_timer, highlightbackground=YELLOW, bg=YELLOW)
start_btn.grid(column=0, row=5)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.config(text="", font=(FONT_NAME, 30, "bold"))
checkmark.grid(column=1, row=6)

title = Label(fg=GREEN, bg=YELLOW)
title.config(text="Timer", font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)

# countdown(2)

window.mainloop()
