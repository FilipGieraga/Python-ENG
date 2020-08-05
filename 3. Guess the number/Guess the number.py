import random as r


def choice():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        wprowadzanie()
    else:
        print("Thank you for using this program.")


def wprowadzanie():
    while True:
        try:
            decyzja_1 = input("Would you like to provide your lucky number? (y/n)\n")
            if decyzja_1 not in "yYnN":
                raise TypeError
        except:
            print("Input decision y/n.")
        else:
            break
    decyzja_1 = decyzja_1.lower()
    if decyzja_1 == "y":
        while True:
            try:
                lucky_number = int(input("Provide your lucky number: \n"))
            except:
                print("Wrong input, please try again.")
            else:
                break
        print(f"Your lucky number is: {lucky_number}")
    elif decyzja_1 == "n":
        lucky_number = r.randint(1, 1000)
        print(f"Random lucky number is: {lucky_number}")

    while True:
        try:
            decyzja_2 = input("Would you like to provide a range? (y/n)\n")
            if decyzja_2 not in "yYnN":
                raise TypeError
        except:
            print("Input decision y/n.")
        else:
            break

    decyzja_2 = decyzja_2.lower()
    if decyzja_2 == "y":
        while True:
            try:
                dolna_granica = int(input("Bottom range: "))
                gorna_granica = int(input("Upper range: "))
                if dolna_granica >= gorna_granica:
                    raise ValueError
            except:
                print("Wrong input, please try again.")
            else:
                break
        print(f"Range selected by you : [{dolna_granica} , {gorna_granica}]")
    elif decyzja_2 == "n":
        dolna_granica = 1
        gorna_granica = 1000
        print(f"Default range is : [{dolna_granica} , {gorna_granica}]")

    if lucky_number not in range(dolna_granica, (gorna_granica + 1)):
        print("Lucky number is not in range.")
        choice()
    else:
        calculate(lucky_number, dolna_granica, gorna_granica)


# lucky_number- szczesliwy nr wygenerowany bądź wprowadzony
# dolna_granica- dolna granica wygenerowana bądź wprowadzona
# gorna_granica- gorna granica wygenerowana bądź wprowadzon
# wylosowany_nr- liczba wylosowana przez komputer
# nr_podejscia- ilosc podejsc komputera do zgadniecia liczby
# lucky_number- musi sie miescic w [dolna_granica,gorna_granica]

def calculate(lucky_number, dolna_granica, gorna_granica):
    attempt_nr = 1
    drawn_nr = 0
    while drawn_nr != lucky_number:
        drawn_nr = r.randint(dolna_granica, gorna_granica)
        print(f"Attempt nr: {attempt_nr}, drawn nr: {drawn_nr}, lucky number: {lucky_number}, "
              f"range [{dolna_granica} , {gorna_granica}]")
        attempt_nr += 1
        if drawn_nr > lucky_number:
            gorna_granica = drawn_nr - 1
            print(f"Too high, lucky number is lower, decreasing upper range to {gorna_granica}.\n")
        elif drawn_nr < lucky_number:
            dolna_granica = drawn_nr + 1
            print(f"Too low, lucky number is higher, increasing bottom range to {dolna_granica}.\n")
        else:
            print("It's a hit :)")
    else:
        print(f"Program found the lucky number in attempt number {attempt_nr - 1}")
    choice()


wprowadzanie()
