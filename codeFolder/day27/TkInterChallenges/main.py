import tkinter

main_screen=tkinter.Tk()
main_screen.title(string="Test Screen")
main_screen.minsize(width=800,height=500)

# Label:
label_one=tkinter.Label(text="Label One")
label_one.grid(column=0,row=0)

def change_label_text(label=label_one):
    label["text"]=entry_one.get()

# Button:
button_one=tkinter.Button(text="Button One",command=change_label_text)
button_one.grid(column=1,row=1)

# Button 2:
button_two=tkinter.Button(text="Button Two")
button_two.grid(column=2,row=0)

# Entry:
entry_one=tkinter.Entry()
entry_one.grid(column=3,row=2)

main_screen.mainloop()
