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
                raise ValueError("Password is longer than one word.")
            if len(password) == 0:
                raise ValueError("You didn't provide the password.")
            for i in y:
                if i not in string.upper():
                    raise ValueError(f"Password contains forbidden letters.\nList of allowed letters: {string}")
        except Exception as error:
            print(f"Error log: {error}\nTry again..")
        else:
            break

    print(f"Your password is : {password}")
    encrypted_list = ["_" for l in password]
    encrypted_string = ' '.join([str(elem) for elem in encrypted_list])
    for i in range(20):
        print("\n")
    print(f"Password contains of {len(password)} letters.")
    print("Password is not case sensitive.")
    print(encrypted_string)
    used_letters = set()

    attempts = 10

    while "_" in encrypted_string:
        letter = input("Provide a letter or whole passsword:\n")
        position = []
        if len(letter) > 1:
            if letter.upper() == password.upper():
                print("Congratulations, you found it :)")
                break
            else:
                print(f"It was not the password, try again {encrypted_string}")
                attempts -= 1
                print(f"Attempts left: {attempts}")
        elif letter.upper() in used_letters or len(letter) == 0 or letter.upper() not in string.upper():
            print("You used space, forbidden character, or a letter you already tried.")
        elif letter.upper() in password:
            print(f"Letter {letter.upper()} is in the password!")
            position = [index for index, x in enumerate(password) if x == letter.upper()]
            for i in position:
                encrypted_list[i] = letter.upper()
                encrypted_string = ' '.join([str(elem) for elem in encrypted_list])
            print(encrypted_string)
        else:
            print("No such letter in the password!!")
            used_letters.add(letter.upper())
            attempts -= 1
            print(f"Try again : {encrypted_string}")
            print(f"Attempts left: {attempts}. List of already used letters:{used_letters}")

        if attempts == 0 and "_" in encrypted_string:
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


if __name__ == '__main__':
    hangman()
