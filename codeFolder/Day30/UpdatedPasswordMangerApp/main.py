import tkinter
import random
import tkinter.dialog
import tkinter.messagebox
import letters_symbols_numbers
import os
import json

'''CONSTANTS'''
CANVAS_HEIGHT=200
CANVAS_WIDTH=200
MAIN_SCREEN_PADX=20
MAIN_SCREEN_PADY=20
PASSWORD_IMG="/home/msokhi99/Desktop/py_programming/Day30/UpdatedPasswordManagerCode/password_image.png"
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
    new_data={
        web_entry:{
            "Email":email_entry,
            "Password":password_entry
        }
    }
    if web_entry!="" and email_entry!="" and password_entry!="":
        try:
            with open("/home/msokhi99/Desktop/py_programming/Day30/UpdatedPasswordManagerCode/saved_passwords.json",mode="r") as file_one:
                data=json.load(file_one)
        except FileNotFoundError:
            with open("/home/msokhi99/Desktop/py_programming/Day30/UpdatedPasswordManagerCode/saved_passwords.json",mode="w") as file_one:
                json.dump(new_data,file_one,indent=4)
        else:
            data.update(new_data)
            with open("/home/msokhi99/Desktop/py_programming/Day30/UpdatedPasswordManagerCode/saved_passwords.json",mode="w") as file_one:
                json.dump(data,file_one,indent=4)
        finally:
            web_entry_field.delete(0,tkinter.END)
            email_field.delete(0,tkinter.END)
            password_field.delete(0,tkinter.END)
            web_entry_field.focus()
    else:
        tkinter.messagebox.showerror(title="Empty Fields",message="You have empty fields.")

def reset_file():
    confirm_box=tkinter.messagebox.askokcancel(title="Reset",message="Are you sure you want to reset ?")
    if confirm_box:
        try:
            os.remove("/home/msokhi99/Desktop/py_programming/Day30/UpdatedPasswordManagerCode/saved_passwords.json")
        except:
            tkinter.messagebox.showerror(title="Error",message="File does not exist.")

def search_for_key():
    try:
        search_file=open("/home/msokhi99/Desktop/py_programming/Day30/UpdatedPasswordManagerCode/saved_passwords.json",mode="r")
    except:
        tkinter.messagebox.showerror(title="Error",message="File does not exist.")
    else:
        contents_of_file=json.load(search_file)
        key_to_search=web_entry_field.get()
        if key_to_search in contents_of_file:
            tkinter.messagebox.showinfo(title=key_to_search,message=f"Email: {contents_of_file[key_to_search]['Email']}\nPassword: {contents_of_file[key_to_search]['Password']}")
        else:
            tkinter.messagebox.showerror(title="Error",message="Key does not exist.")
        search_file.close()
        
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
web_entry_field=tkinter.Entry(width=23,justify="left")
web_entry_field.focus()
web_entry_field.insert(0,"Enter Some Text ...")
web_entry_field.grid(column=1,row=1,pady=3)

'''EMAIL WIDGET'''
email_label=tkinter.Label(text="Email or Username:",font=("Courier",10,"normal"),bg=BG_COLOR)
email_label.grid(column=0,row=2)
email_field=tkinter.Entry(width=34,justify="left")
email_field.grid(column=1,row=2,columnspan=2,pady=3)

'''PASSWORD WIDGET:'''
password_label=tkinter.Label(text="Password:",font=("Courier",10,"normal"),bg=BG_COLOR)
password_label.grid(column=0,row=3)
password_field=tkinter.Entry(width=23,justify="left")
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

'''SEARCH WIDGET'''
search_button=tkinter.Button(text="Search",font=("Courier",10,"normal"),bg=BG_COLOR,highlightthickness=0,command=search_for_key)
search_button.grid(column=2,row=1,pady=3)

main_screen.mainloop()
