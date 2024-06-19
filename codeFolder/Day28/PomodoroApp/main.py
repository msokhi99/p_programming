import tkinter
import math

''' CONSTANTS: '''
BG_COLOR_YELLOW="#f7f5dd"
FG_COLOR_LABEL_GREEN="#9bdeac"
FG_COLOR_LABEL_RED="#e7305b"
FG_COLOR_LABEL_PINK="#e2979c"
WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20

''' GLOBAL VAR: '''
total_reps=0
timer=None

main_screen=tkinter.Tk()
main_screen.title(string="Pomodoro")
main_screen.config(padx=100,pady=20, bg=BG_COLOR_YELLOW)

''' FUNCTION: '''
def loop_timer(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=main_screen.after(1000,loop_timer,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(total_reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        checkmark_label.config(text=mark)


def start_timer():
    global total_reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    total_reps+=1

    if total_reps%8==0:
        loop_timer(long_break_sec)
        timer_label.config(text="BREAK",fg=FG_COLOR_LABEL_RED)
    elif total_reps%2==0:
        loop_timer(short_break_sec)
        timer_label.config(text="BREAK",fg=FG_COLOR_LABEL_PINK)
    else:
        loop_timer(work_sec)
        timer_label.config(text="WORK",fg=FG_COLOR_LABEL_GREEN)

def reset_timer():
    global timer
    global total_reps
    main_screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="TIMER",font=("Courier",30,"normal"),fg=FG_COLOR_LABEL_GREEN,bg=BG_COLOR_YELLOW)
    checkmark_label.config(text="")
    total_reps=0
    

''' WIDGETS: '''
timer_label=tkinter.Label(text="TIMER",font=("Courier",30,"normal"),fg=FG_COLOR_LABEL_GREEN,bg=BG_COLOR_YELLOW)
timer_label.grid(column=1,row=1)
checkmark_label=tkinter.Label(font=("Courier",20,"normal"),fg=FG_COLOR_LABEL_GREEN,bg=BG_COLOR_YELLOW)
checkmark_label.grid(column=1,row=4)
start_button=tkinter.Button(text="START",command=start_timer)
start_button.grid(column=0,row=3)
reset_button=tkinter.Button(text="RESET",command=reset_timer)
reset_button.grid(column=2,row=3)

''' UI Setup: '''
canvas=tkinter.Canvas(width=201,height=224,highlightthickness=0,bg=BG_COLOR_YELLOW)
image_on_canvas=tkinter.PhotoImage(file="/home/msokhi99/Desktop/py_programming/Day29/PomodoroProject/tomato.png")
canvas.create_image(101,112,image=image_on_canvas)
timer_text=canvas.create_text(101,135,text="00:00",font=("Courier",35,"bold"))
canvas.grid(column=1,row=2)
main_screen.mainloop()
