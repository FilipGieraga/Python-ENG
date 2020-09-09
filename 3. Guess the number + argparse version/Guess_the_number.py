import random


def choice():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        main()
    else:
        print("Thank you for using this program.")


def main():
    while True:
        try:
            decision_1 = input("Would you like to provide your lucky number? (y/n)\n")
            if decision_1 not in "yYnN":
                raise ValueError("Incomprehensible decision")
        except Exception as error1:
            print(f"Error log: {error1}\nInput decision y/n.")
        else:
            break
    decision_1 = decision_1.lower()
    if decision_1 == "y":
        while True:
            try:
                lucky_number = int(input("Provide your lucky number: \n"))
            except Exception as error:
                print(f"Error log: {error}\nWrong input, please try again.")
            else:
                break
        print(f"Your lucky number is: {lucky_number}")
    elif decision_1 == "n":
        lucky_number = random.randint(1, 1000)
        print(f"Random lucky number is: {lucky_number}")

    while True:
        try:
            decision_2 = input("Would you like to provide a range? (y/n)\n")
            if decision_2 not in "yYnN":
                raise ValueError("Incomprehensible decision")
        except Exception as error:
            print(f"Error log: {error}\nInput decision y/n.")
        else:
            break

    decision_2 = decision_2.lower()
    if decision_2 == "y":
        while True:
            try:
                bottom_range = int(input("Bottom range: "))
                upper_range = int(input("Upper range: "))
                if bottom_range >= upper_range:
                    raise ValueError("Bottom range should be less than the upper range.")
            except Exception as error1:
                print(f"Error log: {error1}\nTry again.")
            else:
                break
        print(f"Range selected by you : [{bottom_range} , {upper_range}]")
    elif decision_2 == "n":
        bottom_range = 1
        upper_range = 1000
        print(f"Default range is : [{bottom_range} , {upper_range}]")

    if lucky_number not in range(bottom_range, (upper_range + 1)):
        print("Lucky number is not in range.")
        choice()
    else:
        calculate(lucky_number, bottom_range, upper_range)


def calculate(lucky_number, bottom_range, upper_range):
    attempt_nr = 1
    drawn_nr = 0
    while drawn_nr != lucky_number:
        drawn_nr = random.randint(bottom_range, upper_range)
        print(f"Attempt nr: {attempt_nr}, drawn nr: {drawn_nr}, lucky number: {lucky_number}, "
              f"range [{bottom_range} , {upper_range}]")
        attempt_nr += 1
        if drawn_nr > lucky_number:
            upper_range = drawn_nr - 1
            print(f"Too high, lucky number is lower, decreasing upper range to {upper_range}.\n")
        elif drawn_nr < lucky_number:
            bottom_range = drawn_nr + 1
            print(f"Too low, lucky number is higher, increasing bottom range to {bottom_range}.\n")
        else:
            print("It's a hit :)")
    else:
        print(f"Program found the lucky number in attempt number {attempt_nr - 1}")
    choice()


if __name__ == '__main__':
    main()
