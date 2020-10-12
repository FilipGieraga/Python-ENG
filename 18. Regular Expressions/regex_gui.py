import regex_check
from tkinter import *

# Functions

def pesel_check():
    global output
    output.grid_forget()
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_pesel(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output = Label(window, text=final)
        output.grid(row=16, column=2)
    else:
        output = Label(window, text=result)
        output.grid(row=16, column=2)

def time_check():
    global output
    output.grid_forget()
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_time(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output = Label(window, text=final)
        output.grid(row=16, column=2)
    else:
        output = Label(window, text=result)
        output.grid(row=16, column=2)

def id_check():
    global output
    output.grid_forget()
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_id(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output = Label(window, text=final)
        output.grid(row=16, column=2)
    else:
        output = Label(window, text=result)
        output.grid(row=16, column=2)

def nip_check():
    global output
    output.grid_forget()
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_nip(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output = Label(window, text=final)
        output.grid(row=16, column=2)
    else:
        output = Label(window, text=result)
        output.grid(row=16, column=2)

def phone_check():
    global output
    output.grid_forget()
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_phone(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        # output = Entry(window, text=final, exportselection=0)
        output = Label(window, text=final)
        output.grid(row=16, column=2)
    else:
        output = Label(window, text=result)
        output.grid(row=16, column=2)

window = Tk()
window.wm_title("REGEX CHECKER")
window.geometry("800x600")

# Labels

l1 = Label(window, text="Text goes here:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Results:")
l2.grid(row=15, column=0)

output = Label(window, text="")
output.grid(row=16, column=2)

# Input text

text_to_check = Text(window, height=20, width=60)
text_to_check.grid(row=1, column=1, rowspan=10, columnspan=8)

# Buttons

b1 = Button(window, text="Pesel", width=12, command=pesel_check)
b1.grid(row=3, column=10, sticky=NE)

b2 = Button(window, text="NIP", width=12, command=nip_check)
b2.grid(row=4, column=10, sticky=NE)

b3 = Button(window, text="Polish ID", width=12, command=id_check)
b3.grid(row=5, column=10, sticky=NE)

b4 = Button(window, text="Phone Number", width=12, command=phone_check)
b4.grid(row=6, column=10, sticky=NE)

b5 = Button(window, text="Time", width=12, command=time_check)
b5.grid(row=7, column=10, sticky=NE)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=8, column=10, sticky=NE)

window.mainloop()
