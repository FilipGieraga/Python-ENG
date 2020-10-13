from tkinter import *
import tkinter.messagebox

string = "abcdefghijklmnopqrstuvwxyz"


# Functions

def get_password():
    global password, l5, l2
    password = password_here.get()
    l2.configure(text="")
    try:
        password = password.upper()
        x = password.split()
        y = [l for l in password]
        if len(x) > 1:
            raise ValueError
        elif len(password) == 0:
            raise ValueError
        for i in y:
            if i not in string.upper():
                raise ValueError
    except:
        l2.configure(text="Wrong password. Try again..")
        password_here.delete(0, END)
    else:
        b1.config(state='disabled')
        set_game()


def set_game():
    global b3, guess_here, encrypted_list, encrypted_string, used_letters, attempts
    used_letters = set()
    attempts = 10
    l2.configure(text="Password has been set.")
    password_here.delete(0, END)
    encrypted_list = ["_" for l in password]
    encrypted_string = ' '.join([str(elem) for elem in encrypted_list])
    l5.configure(text=f"Password contains of {len(password)} letters.")
    l6.configure(text="Password:")
    l7.configure(text=encrypted_string)
    l8.configure(text="It's your time to guess:")
    l9.configure(text=f"Attempts: {attempts}")
    l11.configure(text=f"Used letters: {used_letters}")
    b3 = Button(window, text="TRY", width=12, command=guess)
    b3.grid(row=11, column=1)
    guess_here = Entry(window, bg="light green", width=20)
    guess_here.grid(row=10, column=1)


def guess():
    global attempts, encrypted_string, used_letters
    letter = guess_here.get()
    print(letter)
    if len(letter) > 1:
        if letter.upper() == password.upper():
            tkinter.messagebox.showinfo(title="Message", message="Congratulations, you found password :)")
            guess_here.delete(0, END)
            b3.config(state='disabled')
        else:
            l10.configure(text="It was not the password, try again")
            guess_here.delete(0, END)
            attempts -= 1
            l9.configure(text=f"Attempts: {attempts}")
    elif letter.upper() in used_letters or len(letter) == 0 or letter.upper() not in string.upper():
        l10.configure(text="You used space, forbidden character,\n or a letter you already tried.")
        guess_here.delete(0, END)
    elif letter.upper() in password:
        l10.configure(text=f"Letter {letter.upper()} is in the password!")
        position = [index for index, x in enumerate(password) if x == letter.upper()]
        for i in position:
            encrypted_list[i] = letter.upper()
            encrypted_string = ' '.join([str(elem) for elem in encrypted_list])
        l7.configure(text=encrypted_string)
        guess_here.delete(0, END)
    else:
        l10.configure(text="No such letter in the password!!\n Try again!")
        used_letters.add(letter.upper())
        attempts -= 1
        l9.configure(text=f"Attempts: {attempts}")
        l11.configure(text=f"Used letters: {used_letters}")
        guess_here.delete(0, END)
    if attempts == 0 and "_" in encrypted_string:
        b3.config(state='disabled')
        tkinter.messagebox.showinfo(title="Message", message=f"You lost. The password to guess was : {password}")
    elif "_" not in encrypted_string:
        b3.config(state='disabled')
        tkinter.messagebox.showinfo(title="Message", message="Congratulations, you found password :)")


def reset_game():
    global password,guess_here, b3
    try:
        b3.winfo_exists()
    except:
        pass
    else:
        guess_here.grid_forget()
        b3.grid_forget()
    password_here.delete(0, END)
    b1.config(state='normal')
    password=""
    l2.configure(text="")
    l5.configure(text="")
    l6.configure(text="")
    l7.configure(text="")
    l8.configure(text="")
    l9.configure(text="")
    l10.configure(text="")
    l11.configure(text="")

window = Tk()
window.wm_title("HANGMAN GAME")
window.geometry("600x400")

# Labels

# static info
l1 = Label(window, text="Please provide password:")
l1.grid(row=1, column=0)

# potential error/success message
l2 = Label(window, text="")
l2.grid(row=3, column=1)

# static info
l3 = Label(window, text="Password should be a single word.\n"
                        "List of allowed letters: abcdefghijklmnopqrstuvwxyz\n"
                        "Password is not case sensitive.")
l3.grid(row=4, column=1)

# static info
l4 = Label(window, text="Information:")
l4.grid(row=5, column=0)

# password contain x letters
l5 = Label(window, text="")
l5.grid(row=5, column=1)

# static info
l6 = Label(window, text="", font=("Courier", 18))
l6.grid(row=6, column=1)

# encrypted string
l7 = Label(window, text="", font=("Courier", 16))
l7.grid(row=7, column=1)

# static info
l8 = Label(window, text="")
l8.grid(row=8, column=0, ipady=8)

# attempts
l9 = Label(window, text="")
l9.grid(row=9, column=2)

# messaging
l10 = Label(window, text="")
l10.grid(row=12, column=1)

# used letters
l11 = Label(window, text="")
l11.grid(row=13, column=1)

# Input password

password_here = Entry(window, bg="light cyan", width=20)
password_here.grid(row=2, column=1)

# Buttons

b1 = Button(window, text="START", width=12, command=get_password)
b1.grid(row=2, column=3, sticky=NE)

b2 = Button(window, text="RESET", width=12, command=reset_game)
b2.grid(row=4, column=3, sticky=NE)

window.mainloop()
