import datetime


def choice():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        count_days()
    else:
        print("Thank you for using this program.")


def count_days():
    while True:
        try:
            a = int(input("What day were you born?(1,31)\n"))
            b = int(input("What month?(1,12)\n"))
            c = int(input("Which year?\n"))
            birth = datetime.date(c, b, a)
        except:
            print("Wrong date format, please try again.")
        else:
            break
    birth = datetime.date(c, b, a)
    now = datetime.date.today()
    delt = (now - birth)
    if delt.days > 0:
        print(f"You live exactly : {delt.days} days, which is {delt.days * 24} hours,")
        print(f"which is {delt.days * 24 * 60} minutes.")
    elif delt.days < 0:
        print(
            f"If you were born today, in given year you would be : {-delt.days} days old, which is {-delt.days * 24} hours,")
        print(f"which is {-delt.days * 24 * 60} minutes.")
    else:
        print("You entered today's date.")
    choice()


count_days()
