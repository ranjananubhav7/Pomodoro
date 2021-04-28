from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 25
reps = 0
window = Tk()
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    check_mark["text"] = ""
    canvas.itemconfig(timer_text, text='00:00')
    label["text"] = 'Timer'
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_time = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps == 1:
        check_mark["text"] = "✔"
    elif reps == 3:
        check_mark["text"] = "✔✔"
    elif reps == 5:
        check_mark["text"] = "✔✔✔"
    elif reps == 7:
        check_mark["text"] = "✔✔✔✔"

    if reps % 2 == 0:
        countdown(work_time)
        label["text"] = "Work"
    elif reps % 2 != 0 and reps < 7:
        countdown(short_break)
        label["text"] = "Break"
        label["fg"] = RED
    elif reps % 2 != 0 and reps > 7:
        countdown(long_break)
        label["text"] = "Break"
        label["fg"] = PINK
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global timer
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count//60}:{'%02d' %(count%60)}")
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=image)
timer_text = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)
label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
check_mark = Label(text="", font=(FONT_NAME, 15, "bold"), fg=RED, bg=YELLOW)
label.grid(row=1, column=2)
check_mark.grid(row=4, column=2)
start_button = Button(text="start", command=start_timer)
reset_button = Button(text="reset", command=reset_timer)
start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)

window.mainloop()
