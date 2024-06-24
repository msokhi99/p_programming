import tkinter as gui
from quiz_brain import QuizBrain

RIGHT_IMG="/home/msokhi99/Desktop/py_programming/Day34/images/true.png"
WRONG_IMG="/home/msokhi99/Desktop/py_programming/Day34/images/false.png"
BG_COLOR_MENU="#ffcad4"
CANVAS_COLOR="#f4acb7"

class UserInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz_brain=quiz_brain
        self.main_screen=gui.Tk()
        self.main_screen.title("QUIZLET APP")
        self.main_screen.config(padx=20,pady=20,bg=BG_COLOR_MENU)
        self.score_label=gui.Label(text="Score: 0", font=("Courier",10,"bold"),fg="black",bg=BG_COLOR_MENU,highlightthickness=1,highlightbackground="black")
        self.score_label.grid(column=0,row=0,columnspan=2,pady=10)
        self.canvas=gui.Canvas(height=250,width=300,highlightthickness=1,highlightbackground="black",bg=CANVAS_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2)
        right_img=gui.PhotoImage(file=RIGHT_IMG)
        wrong_img=gui.PhotoImage(file=WRONG_IMG)
        self.right_button=gui.Button(image=right_img,highlightthickness=1,highlightbackground="black",command=self.pressed_the_right_button)
        self.right_button.grid(column=0,row=2,pady=10)
        self.wrong_button=gui.Button(image=wrong_img,highlightthickness=1,highlightbackground="black",command=self.pressed_the_wrong_button)
        self.wrong_button.grid(column=1,row=2,pady=10)
        self.quiz_text=self.canvas.create_text(150,135,text="Test",font=("Courier",10,"normal"),width=300)
        self.disp_question()
        self.main_screen.mainloop()
    
    def disp_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            new_question=self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quiz_text,text=new_question)
        else:
            self.canvas.itemconfig(self.quiz_text,text="The End")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    
    def pressed_the_right_button(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))
    
    def pressed_the_wrong_button(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.main_screen.after(1000, self.disp_question)