import random

digits = "0123456789"
upper_case = "ABCDEFGHIJKLMNOPRSTQUWXYZ"
lower_case = "abcdefghijklmnoprqstuwxyz"
special_characters = "!@#$%^&*(){}[]\|:\"'<>?,./"

def specified_pass():
    p = ""
    while True:
        try:
            d1 = input("Do you want digits?(y/n)\n")
            if d1 not in "yn":
                raise ValueError("Incomprehensible decision")
        except Exception as error:
            print(f"Error log: {error}\nInput decision y/n.")
        else:
            break
    if d1 == "y":
        while True:
            try:
                i1 = int(input("How many?\n"))
            except Exception as error:
                print(f"Error log: {error}\nInput integer number.")
            else:
                break
        for i in range(i1):
            p += random.choice(digits)
    else:
        pass

    while True:
        try:
            d2 = input("Do you want upper case letters?(y/n)\n")
            if d2 not in "yn":
                raise ValueError("Incomprehensible decision")
        except Exception as error:
            print(f"Error log: {error}\nInput decision y/n.")
        else:
            break
    if d2 == "y":
        while True:
            try:
                i2 = int(input("How many?\n"))
            except Exception as error:
                print(f"Error log: {error}\nInput integer number.")
            else:
                break
        for i in range(i2):
            p += random.choice(upper_case)
    else:
        pass

    while True:
        try:
            d3 = input("Do you want lower case letters?(y/n)\n")
            if d3 not in "yn":
                raise ValueError("Incomprehensible decision")
        except Exception as error:
            print(f"Error log: {error}\nInput decision y/n.")
        else:
            break
    if d3 == "y":
        while True:
            try:
                i3 = int(input("How many?\n"))
            except Exception as error:
                print(f"Error log: {error}\nInput integer number.")
            else:
                break
        for i in range(i3):
            p += random.choice(lower_case)
    else:
        pass

    while True:
        try:
            d4 = input("Do you want special characters?(y/n)\n")
            if d4 not in "yn":
                raise ValueError("Incomprehensible decision")
        except Exception as error:
            print(f"Error log: {error}\nInput decision y/n.")
        else:
            break
    if d4 == "y":
        while True:
            try:
                i4 = int(input("How many?\n"))
            except Exception as error:
                print(f"Error log: {error}\nInput integer number.")
            else:
                break
        for i in range(i4):
            p += random.choice(special_characters)
    else:
        pass
    return p


def random_generated_pass(digits, upper_case, lower_case, special_characters):
    x = digits + upper_case + lower_case + special_characters
    while True:
        try:
            y = int(input("How many characters for the password?\n"))
        except Exception as error:
            print(f"Error log: {error}\nInput integer number.")
        else:
            break

    x = ''.join(random.sample(x, len(x)))
    x = x[:y]
    return f"Your password : {x}"


def decide():
    while True:
        try:
            choice = input("Do you want to specify the number of individual characters in the password, "
                           "i.e. upper and lower case letters?(y/n)\n")
            if choice == "y":
                p = specified_pass()
                p = ''.join(random.sample(p, len(p)))
                print(f"Your password : {p}")
                again()
            elif choice == "n":
                print(random_generated_pass(digits, upper_case, lower_case, special_characters))
                again()
            else:
                raise ValueError("Incomprehensible decision")
        except Exception as error:
            print(f"Error log: {error}\nSomething went wrong. Try again...")
        else:
            break


def again():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        decide()
    else:
        print("Thank you for using this program.")


if __name__ == '__main__':
    decide()
