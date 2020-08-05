def hangman():
    print("Password should be a single word.")
    string = "abcdefghijklmnopqrstuvwxyz"

    while True:
        try:
            password = input("Provide password to guess:\n")
            password = password.upper()
            x = password.split()
            y = [l for l in password]
            if len(x) > 1:
                print("Password is longer than one word.")
                raise ValueError
            if len(password) == 0:
                print("You didn't provide the password.")
                raise ValueError
            for i in y:
                if i not in string.upper():
                    print("Password contains forbidden letters.")
                    print(f"List of allowed letters: {string}")
                    raise ValueError
        except:
            print("Try again..")
        else:
            break

    print(f"Your password is : {password}")
    zaszyfrowane_lista = ["_" for l in password]
    zaszyfrowane_string = ' '.join([str(elem) for elem in zaszyfrowane_lista])
    for i in range(20):
        print("\n")
    print(f"Password contains of {len(password)} letters.")
    print("Password is not case sensitive.")
    print(zaszyfrowane_string)
    uzyte_litery = set()

    l_podejsc = 10

    while "_" in zaszyfrowane_string:
        litera = input("Provide a letter or whole passsword:\n")
        pozycja = []
        if len(litera) > 1:
            if litera.upper() == password.upper():
                print("Congratulations, you found it :)")
                break
            else:
                print(f"It was not the password, try again {zaszyfrowane_string}")
                l_podejsc -= 1
                print(f"Attempts left: {l_podejsc}")
        elif litera.upper() in uzyte_litery or len(litera) == 0 or litera.upper() not in string.upper():
            print("You used space, forbidden character, or a letter you already tried.")
        elif litera.upper() in password:
            print(f"Letter {litera.upper()} is in the password!")
            pozycja = [index for index, x in enumerate(password) if x == litera.upper()]
            for i in pozycja:
                zaszyfrowane_lista[i] = litera.upper()
                zaszyfrowane_string = ' '.join([str(elem) for elem in zaszyfrowane_lista])
            print(zaszyfrowane_string)
        else:
            print("No such letter in the password!!")
            uzyte_litery.add(litera.upper())
            l_podejsc -= 1
            print(f"Try again : {zaszyfrowane_string}")
            print(f"Attempts left: {l_podejsc}. List of already used letters:{uzyte_litery}")

        if l_podejsc == 0 and "_" in zaszyfrowane_string:
            print(f"Unfortunately, you lost. The password to guess was : {password}")
            break
    else:
        print("Congratulations, you found it :)")
    choice()


def choice():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        hangman()
    elif choi == "n":
        print("Thank you for using this program.")
    else:
        print(f"Sorry, I think i don't understand {choi}")
        choice()


hangman()
