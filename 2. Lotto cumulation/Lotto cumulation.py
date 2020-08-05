import random


def lotto():
    d = input("Would you like to provide your lucky numbers?(y/n)\n")
    if d == "y":
        lucky_numbers = set()
        for i in range(1, 7):
            while True:
                try:
                    number = int(input(f"Provide {i} number:\n"))
                    if number not in range(1, 50) or number in lucky_numbers:
                        raise ValueError
                    lucky_numbers.add(number)
                    if i < 6:
                        print(f"Your lucky numbers so far: {sorted(lucky_numbers)}")
                    else:
                        pass
                except:
                    print("Possible errors:\nNumber out of range <1,49>\nIt is not an integer number"
                          "\nYou have already given this number before")
                    print(f"Your lucky numbers so far: {sorted(lucky_numbers)}")
                else:
                    break
    else:
        print("Your first coupon will be generated automatically.")

    if d == "y":
        coupon = lucky_numbers
    else:
        coupon = set(random.sample(range(1, 50), 6))
    cumulation = set(random.sample(range(1, 50), 6))
    common = (coupon.intersection(cumulation))

    print(f"The results of this lottery: {sorted(cumulation)}")
    print(f"Our lucky numbers: {sorted(coupon)}")

    if len(common) == 0:
        print("Unfortunately, no hits :( ")
    else:
        print(f"Number of hits {len(common)},\ncommon numbers are {list(common)}")

    while True:
        try:
            x = int(input("Enter the number of hits you want to get.\n"))
            if x not in range(1, 7):
                raise ValueError
            else:
                pass
        except:
            print("You entered a number out of range <1.6>, or it is not an integer.")
        else:
            break

    q = 2
    while len(common) < x:
        coupon = set(random.sample(range(1, 50), 6))
        print(f"Lottery hits : {sorted(cumulation)}")
        common = (coupon.intersection(cumulation))
        print(f"Coupon nr. {q}: {sorted(coupon)}, common numbers are {len(common)}")
        q += 1
    else:
        print(f"Number of tries to hit {x} in this lottery: {q - 1}, common numbers are {sorted(common)}.")
    choice()


def choice():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        lotto()
    else:
        print("Thank you for using this program.")


lotto()
