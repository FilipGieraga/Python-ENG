import random
import argparse
from argparse import RawTextHelpFormatter

digits = "0123456789"
upper_case = "ABCDEFGHIJKLMNOPRSTQUWXYZ"
lower_case = "abcdefghijklmnoprqstuwxyz"
special_characters = "!@#$%^&*(){}[]\|:\"'<>?,./"


def specified_pass(**kwargs):
    p = ''
    for k, v in kwargs.items():
        if k == 'd' and v != 0:
            for i in range(v):
                p += random.choice(digits)
        if k == 'u' and v != 0:
            for i in range(v):
                p += random.choice(upper_case)
        if k == 'l' and v != 0:
            for i in range(v):
                p += random.choice(lower_case)
        if k == 's' and v != 0:
            for i in range(v):
                p += random.choice(special_characters)
    p = ''.join(random.sample(p, len(p)))
    return print(f"Your specified password : {p}")


def random_generated_pass(y):
    x = digits + upper_case + lower_case + special_characters
    x = ''.join(random.sample(x, len(x)))
    x = x[:y]
    return f"Your random password : {x}"


parser = argparse.ArgumentParser(description="Generate random password", formatter_class=RawTextHelpFormatter)

parser.add_argument("o", metavar="Options", type=str, help="r - random password\n"
                                                           "[-n number] optional number of characters in a completely random password, default is 8\n"
                                                           "p - precise password\n"
                                                           "[-d number] opcjonalna ilość cyfr w sprecyzowanym haśle, domyślnie 0\n"
                                                           "[-l number] opcjonalna ilość małych liter w sprecyzowanym haśle, domyślnie 0\n"
                                                           "[-u number] opcjonalna ilość duzych liter w sprecyzowanym haśle, domyślnie 0\n"
                                                           "[-s number] opcjonalna ilość znaków specjalnych w sprecyzowanym haśle, domyślnie 0\n",
                    choices=["r", "p"], nargs="?")

args, sub_args = parser.parse_known_args()

if args.o == 'r':
    parser.add_argument('-n', type=int, default=8)
    args = parser.parse_args(sub_args)
    print(random_generated_pass(args.n))
elif args.o == 'p':
    parser.add_argument('-d', type=int, default=0)
    parser.add_argument('-l', type=int, default=0)
    parser.add_argument('-u', type=int, default=0)
    parser.add_argument('-s', type=int, default=0)
    args = parser.parse_args(sub_args)
    specified_pass(d=args.d, l=args.l, u=args.u, s=args.s)
else:
    pass
