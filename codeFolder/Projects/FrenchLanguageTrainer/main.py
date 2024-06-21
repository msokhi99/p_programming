import tkinter
import tkinter.messagebox
import file_setup
import random
import pyttsx3
import pandas as pd
import os

voice_interpret=pyttsx3.init()
voice_interpret.setProperty("rate",50)
voice_interpret.setProperty("volume",1.0)

'''CONSTANTS'''
BG_COLOR="#a9def9"
CANVAS_COLOR="#d0f4de"
CANVAS_COLOR_WRONG="#fcf6bd"

'''DICT WORDS'''
french_words={row["French"]:row["English"] for (index,row) in file_setup.french_df.iterrows()}
keys_of_words_displayed=[]

'''FUNCTIONS'''
def generate_random_pair():
    global random_key
    global random_key_value
    if len(keys_of_words_displayed)==len(french_words):
        tkinter.messagebox.showerror(title="Error",message="You have correctly guessed all the words.\nTo play again, simply start the program again.")
        main_screen.quit()
    else:
        random_key=random.choice(list(french_words.keys()))
        if random_key in keys_of_words_displayed:
            generate_random_pair()
        else:
            random_key_value=french_words[random_key]
            keys_of_words_displayed.append(random_key)

def go_back():
    global random_key
    canvas.configure(bg=CANVAS_COLOR_WRONG)
    canvas.itemconfig(canvas_text_translation,text="French")
    canvas.itemconfig(canvas_text_word,text=random_key)
    speak_button.config(state=tkinter.NORMAL)

def go_front():
    global random_key_value
    canvas.configure(bg=CANVAS_COLOR)
    canvas.itemconfig(canvas_text_translation,text="English")
    generate_random_pair()
    canvas.itemconfig(canvas_text_word,text=random_key_value)
    speak_button.config(state=tkinter.DISABLED)

def pronounce_word():
    voice_interpret.say(random_key)
    voice_interpret.runAndWait()

'''UI SETUP'''

'''MAIN SCREEN'''
main_screen=tkinter.Tk()
main_screen.title(string="Language Trainer")
main_screen.config(padx=50,pady=10,bg=BG_COLOR)

'''LABEL'''
main_title=tkinter.Label(text="French Language Trainer",font=("Arial",30,"bold"),bg=BG_COLOR)
main_title.grid(column=0,row=0,columnspan=2,pady=20)

'''CANVAS'''
canvas=tkinter.Canvas(width=600,height=600,bg=CANVAS_COLOR,highlightthickness=2,highlightbackground="black")
canvas_text_translation=canvas.create_text(300,150, text="English",font=("Arial",30,"bold"))
generate_random_pair()
canvas_text_word=canvas.create_text(300,350,text=random_key_value,font=("Arial",20,"bold"),tag="Value")
canvas.grid(column=0,row=1,columnspan=2)

'''RIGHT BUTTON'''
right_image=tkinter.PhotoImage(file="/home/msokhi99/Desktop/py_programming/Day31/right.png")
right_button=tkinter.Button(image=right_image,highlightthickness=2,highlightbackground="black",command=go_front)
right_button.grid(column=0,row=2,pady=25)

'''WRONG BUTTON'''
wrong_image=tkinter.PhotoImage(file="/home/msokhi99/Desktop/py_programming/Day31/wrong.png")
wrong_button=tkinter.Button(image=wrong_image,highlightthickness=2,highlightbackground="black",command=go_back)
wrong_button.grid(column=1,row=2,pady=25)

'''SPEAK BUTTON:'''
speak_button=tkinter.Button(text="Pronounce",font=("Arial",10,"normal"),highlightthickness=2,highlightbackground="black",command=pronounce_word)
speak_button.grid(column=0,row=2,columnspan=2)
speak_button.config(state=tkinter.DISABLED)

main_screen.mainloop()

words_to_learn={key:value for (key,value) in french_words.items() if key not in keys_of_words_displayed}
updated_df=pd.DataFrame(data=list(words_to_learn.items()), columns=["French","English"])
updated_df.to_csv("/home/msokhi99/Desktop/py_programming/Day31/words_to_learn.csv",index=False)

if len(keys_of_words_displayed)==len(french_words):
    os.remove("/home/msokhi99/Desktop/py_programming/Day31/words_to_learn.csv")
