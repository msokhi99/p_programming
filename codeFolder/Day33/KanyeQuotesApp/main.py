import tkinter 
import requests

'''CONSTANTS'''
BG_COLOR="#FFAFCC"

'''FUNCTIONS'''
def get_quote():
    response=requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    api_data=response.json()["quote"]
    main_canvas.itemconfig(canvas_text,text=api_data)

'''UI SETUP'''
try:
    main_screen=tkinter.Tk()
    main_screen.title(string="Kanye Quote App")
    main_screen.config(padx=50,pady=50,bg=BG_COLOR)
    canvas_background_img=tkinter.PhotoImage(file="/home/msokhi99/Desktop/py_programming/Day33/KanyeQuotesApp/background.png")
    kanye_button_img=tkinter.PhotoImage(file="/home/msokhi99/Desktop/py_programming/Day33/KanyeQuotesApp/kanye.png")
except FileNotFoundError as error_message:
    print(f"{error_message} not found. Please try again.")
else:
    main_canvas=tkinter.Canvas(width=500,height=510,bg=BG_COLOR,highlightthickness=0)
    main_canvas.create_image(250,300,image=canvas_background_img)
    canvas_text=main_canvas.create_text(250,270,font=("courier",15,"bold"),width=250,justify="center",fill="white")
    main_canvas.grid(column=0,row=0)
    kanye_button=tkinter.Button(image=kanye_button_img,highlightbackground="black",highlightthickness=1,command=get_quote)
    kanye_button.grid(column=0,row=1,pady=20)
    main_screen.mainloop()
