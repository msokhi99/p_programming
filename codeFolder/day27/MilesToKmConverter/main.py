# Disclaimer: 
"""
Remember to hit 'reset' after each conversion.
"""
import tkinter 

main_window=tkinter.Tk()
main_window.title(string="MILES TO KM CONVERTER")
main_window.config(width=400,height=400,padx=30,pady=30)

# Miles Label:
miles_label=tkinter.Label(text="MILES",font=("Impact",20,"normal"))
miles_label.grid(column=0,row=0,padx=5,pady=15)

# Miles Entry:
miles_entry_filed=tkinter.Entry()
miles_entry_filed.config(width=10,borderwidth=3,justify="center")
miles_entry_filed.insert(index=0,string="0")
miles_entry_filed.grid(column=0,row=1,padx=10,pady=10)

# Interchange Label:
interchange_label=tkinter.Label(text="<>",font=("Impact",20,"normal"))
interchange_label.grid(column=1,row=0,padx=5,pady=15)

# Kilometer Label: 
km_label=tkinter.Label(text="KM'S",font=("Impact",20,"normal"))
km_label.grid(column=2,row=0,padx=5,pady=15)

# Kilometer Entry:
km_entry_filed=tkinter.Entry()
km_entry_filed.config(width=10,borderwidth=3,justify="center")
km_entry_filed.insert(index=0,string="0")
km_entry_filed.grid(column=2,row=1,padx=10,pady=10)

# Logic: 
def convert_distance():
    miles_value=miles_entry_filed.get()
    km_value=km_entry_filed.get()

    if miles_value != "0" and miles_value != "":
        user_miles = float(miles_value)
        converted_miles_to_km = round(user_miles * 1.609, 2)
        km_entry_filed.delete(0, tkinter.END)
        km_entry_filed.insert(0, str(converted_miles_to_km))
    elif km_value != "0" and km_value != "":
        user_km = float(km_value)
        converted_km_to_miles = round(user_km / 1.609, 2)
        miles_entry_filed.delete(0, tkinter.END)
        miles_entry_filed.insert(0, str(converted_km_to_miles))
    else:
        km_entry_filed.delete(0, tkinter.END)
        km_entry_filed.insert(0, "0")
        miles_entry_filed.delete(0, tkinter.END)
        miles_entry_filed.insert(0, "0")

def reset_button():
    km_entry_filed.delete(0, tkinter.END)
    km_entry_filed.insert(0, "0")
    miles_entry_filed.delete(0, tkinter.END)
    miles_entry_filed.insert(0, "0")

# Convert Button: 
convert_button=tkinter.Button(text="Convert",font=("Impact",8,"normal"),command=convert_distance)
convert_button.grid(column=1,row=1)

# Reset Button:
reset_button=tkinter.Button(text="Reset",font=("Impact",8,"normal"),command=reset_button)
reset_button.grid(column=1,row=2)

main_window.mainloop()
