from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
time_counter = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    my_window.after_cancel(time_counter)
    check_marks.config(text="")
    canva.itemconfig(time_text, text="00:00")
    timer_heading.config(text="    Timer")
    global reps
    reps=0


def exit_program():
    quit()
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    global reps
    reps += 1
    if reps%8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_heading.config(text="Long Break", fg="brown")

    elif reps%2 != 0:
        count_down(WORK_MIN * 60)
        timer_heading.config(text="Work Time", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_heading.config(text="Short Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = count//60
    count_sec = count%60
    if count_sec < 10:
        count_sec = str(count_sec)
        count_sec = "0" + count_sec
    canva.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global time_counter
        time_counter = my_window.after(1000, count_down, count-1)
    if count==0:
        my_window.attributes('-topmost',1)
        my_window.attributes('-topmost', 0)
        my_window.bell()
        start_timer()
        marks= " "
        work_sessions = reps//2
        for n in range(work_sessions):
            marks += CHECK_MARK
            check_marks.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #


my_window = Tk()
my_window.title("Pomodoro")
my_window.config(pady=100,padx=100, bg=YELLOW)


canva = Canvas(width=250, height=260, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(120, 110, image=tomato_img)
time_text = canva.create_text(120, 130, text="000", fill="white", font=(FONT_NAME, 28))
canva.pack()

# count_down(10)

timer_heading = Label(text="   TIMER", font=("Arial", 35), fg=RED, bg=YELLOW)
timer_heading.place(x=20, y=-80)

start_button = Button(text="START", fg="green", command=start_timer)
start_button.place(x=10, y=250)

reset_button = Button(text="RESET", fg=RED, command=reset)
reset_button.place(x=192, y=250)

check_marks= Label(text=" ", font=(FONT_NAME, 12), fg="blue", bg=YELLOW)
check_marks.place(x=100, y=230)

exit_button= Button(text="EXIT", fg="orange", command=exit_program)
exit_button.place(x=110, y=290)

my_window.mainloop()

