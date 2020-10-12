import regex_check
from tkinter import *


# Functions

def pesel_check():
    output.delete('1.0', END)
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_pesel(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output.insert(END, final)
    else:
        output.insert(END, result)


def time_check():
    output.delete('1.0', END)
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_time(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output.insert(END, final)
    else:
        output.insert(END, result)


def id_check():
    output.delete('1.0', END)
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_id(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output.insert(END, final)
    else:
        output.insert(END, result)


def nip_check():
    output.delete('1.0', END)
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_nip(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output.insert(END, final)
    else:
        output.insert(END, result)


def phone_check():
    output.delete('1.0', END)
    input = text_to_check.get("1.0", END)
    result = regex_check.is_valid_phone(input)
    final = ""
    if isinstance(result, list):
        for element in result:
            final += f"{element}\n"
        output.insert(END, final)
    else:
        output.insert(END, result)


window = Tk()
window.wm_title("REGEX CHECKER")
window.geometry("800x600")

# Labels

l1 = Label(window, text="Text goes here:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Results:")
l2.grid(row=15, column=0)

output = Text(window, height=13, width=35, bg="light yellow")
output.grid(row=16, column=2)

# Input text

text_to_check = Text(window, height=20, width=60, bg="light cyan")
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
