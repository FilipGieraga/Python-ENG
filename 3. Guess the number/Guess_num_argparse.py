import random
import argparse


def calculate(**kwargs):
    attempt_nr = 1
    drawn_nr = 0
    lucky_number = kwargs.get("lucky_number")
    bottom_range = kwargs.get("range")[0]
    upper_range = kwargs.get("range")[1]
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


parser = argparse.ArgumentParser(
    description="Program that guesses a random or given number from a random or given range")

parser.add_argument('-r', type=str, metavar='bottom & upper range', help="range, default <1,1000>",
                    default="1,1000")

parser.add_argument('-l', type=int, metavar='lucky number',
                    help="lucky number, default range <1,1000>",
                    default=random.randint(1, 1000))
args = parser.parse_args()

my_list = [int(item) for item in args.r.split(',')]

if __name__ == '__main__':
    if my_list[0] >= my_list[1]:
        print("Specified range is not valid.")
    elif args.l not in range(my_list[0], my_list[1] + 1):
        print("Lucky number is not in range.")
    else:
        calculate(lucky_number=args.l, range=my_list)
