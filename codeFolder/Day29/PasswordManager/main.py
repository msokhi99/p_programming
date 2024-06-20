import tkinter
import random
import tkinter.dialog
import tkinter.messagebox
import letters_symbols_numbers
import os

'''CONSTANTS'''
CANVAS_HEIGHT=200
CANVAS_WIDTH=200
MAIN_SCREEN_PADX=20
MAIN_SCREEN_PADY=20
PASSWORD_IMG="/home/msokhi99/Desktop/py_programming/Day29/Password Manager App/password_image.png"
BG_COLOR="#a2d2ff"

'''FUNCTIONS'''

def generate_password():
    password_field.delete(0,tkinter.END)
    letters=letters_symbols_numbers.letters
    symbols=letters_symbols_numbers.symbols
    numbers=letters_symbols_numbers.numbers
    random_list=[letters,symbols,numbers]
    random_password=""
    for _ in range(11):
        random_call=random.choice(random_list)
        random_password+=random.choice(random_call)
    password_field.insert(0,random_password)

def add_to_file():
    web_entry=web_entry_field.get()
    email_entry=email_field.get()
    password_entry=password_field.get()
    if web_entry!="" and email_entry!="" and password_entry!="":
        confirm_box=tkinter.messagebox.askokcancel(title=web_entry,message=f"You have entered:\nEmail: {email_entry}\nPassword: {password_entry}")
        if confirm_box:
            with open("/home/msokhi99/Desktop/py_programming/Day29/Password Manager App/saved_passwords.txt",mode="a") as file_one:
                file_one.writelines(f"{web_entry} ||| {email_entry} ||| {password_entry}\n")
            web_entry_field.delete(0,tkinter.END)
            email_field.delete(0,tkinter.END)
            password_field.delete(0,tkinter.END)
            web_entry_field.focus()
    else:
        tkinter.messagebox.showerror(title="Empty Fields",message="You have empty fields.")

def reset_file():
    confirm_box=tkinter.messagebox.askokcancel(title="Reset",message="Are you sure you want to reset ?")
    if confirm_box:
        if os.path.isfile("/home/msokhi99/Desktop/py_programming/Day29/Password Manager App/saved_passwords.txt"):
            os.remove("/home/msokhi99/Desktop/py_programming/Day29/Password Manager App/saved_passwords.txt")
        else:
            tkinter.messagebox.showerror(title="Error",message="File does not exist.")

'''UI SETUP'''

'''MAIN SCREEN SETUP'''
main_screen=tkinter.Tk()
main_screen.title(string="Password Manager")
main_screen.config(bg=BG_COLOR,padx=MAIN_SCREEN_PADX,pady=MAIN_SCREEN_PADY)

'''CANVAS SETUP'''
bg_img=tkinter.Canvas(height=CANVAS_HEIGHT,width=CANVAS_WIDTH,bg=BG_COLOR,highlightthickness=0)
password_img=tkinter.PhotoImage(file=PASSWORD_IMG)
bg_img.create_image(100,100,image=password_img)
bg_img.grid(column=1,row=0)

'''WEBSITE WIDGET'''
web_label=tkinter.Label(text="Website:",font=("Courier",10,"normal"),bg=BG_COLOR)
web_label.grid(column=0,row=1)
web_entry_field=tkinter.Entry(width=35,justify="left")
web_entry_field.focus()
web_entry_field.insert(0,"Enter Some Text ...")
web_entry_field.grid(column=1,row=1,columnspan=2,pady=3)

'''EMAIL WIDGET'''
email_label=tkinter.Label(text="Email or Username:",font=("Courier",10,"normal"),bg=BG_COLOR)
email_label.grid(column=0,row=2)
email_field=tkinter.Entry(width=35,justify="left")
email_field.grid(column=1,row=2,columnspan=2,pady=3)

'''PASSWORD WIDGET:'''
password_label=tkinter.Label(text="Password:",font=("Courier",10,"normal"),bg=BG_COLOR)
password_label.grid(column=0,row=3)
password_field=tkinter.Entry(width=24,justify="left")
password_field.grid(column=1,row=3,columnspan=1,pady=3)

'''GEN. PASSWORD WIDGET'''
gen_password=tkinter.Button(text="Generate",font=("Courier",10,"normal"),bg=BG_COLOR,highlightthickness=0,width=8,command=generate_password)
gen_password.grid(column=2,row=3,padx=2)

'''ADD WIDGET'''
add_button=tkinter.Button(text="Add",font=("Courier",10,"normal"),bg=BG_COLOR,highlightthickness=0,command=add_to_file)
add_button.grid(column=0,row=4,pady=4)

'''RESET WIDGET'''
reset_button=tkinter.Button(text="Reset",font=("Courier",10,"normal"),bg=BG_COLOR,highlightthickness=0,command=reset_file)
reset_button.grid(column=0,row=5)

main_screen.mainloop()
