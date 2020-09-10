import random
import argparse
import string
from argparse import RawTextHelpFormatter

def specified_pass(**kwargs):
    p = ''
    for k, v in kwargs.items():
        if k == 'd' and v != 0:
            for i in range(v):
                p += random.choice(string.digits)
        if k == 'u' and v != 0:
            for i in range(v):
                p += random.choice(string.ascii_uppercase)
        if k == 'l' and v != 0:
            for i in range(v):
                p += random.choice(string.ascii_lowercase)
        if k == 's' and v != 0:
            for i in range(v):
                p += random.choice(string.punctuation)
    p = ''.join(random.sample(p, len(p)))
    return print(f"Your specified password : {p}")


def random_generated_pass(y):
    x = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    x = ''.join(random.sample(x, len(x)))
    x = x[:y]
    return f"Your random password : {x}"


parser = argparse.ArgumentParser(description="Generate random password", formatter_class=RawTextHelpFormatter)

parser.add_argument("o", metavar="Options", type=str, help="r - random password\n"
                                                           "[-n number] optional number of characters in a completely random password, default 8\n"
                                                           "p - precise password\n"
                                                           "[-d number] optional number of digits in a specified password, default 8\n"
                                                           "[-l number] optional number of lower cases in a specified password, default 8\n"
                                                           "[-u number] optional number of upper cases in a specified password, default 8\n"
                                                           "[-s number] optional number of special characters in a specified password, default 8\n",
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
