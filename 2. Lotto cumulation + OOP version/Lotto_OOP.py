import random


class Lotto:
    def __init__(self, *args):
        """You can either create an instance of a class with your 6 numbers, or without any.
        Instance without numbers will have them generated automatically"""
        self.args = args

    def one_check(self):
        """This method checks if the numbers on the coupon meet conditions
        (6 ints from range <1,49> without duplicates)"""

        def single_check():
            """Function makes one cumulation and check for hits"""
            cumulation = set(random.sample(range(1, 50), 6))
            print(f"The results of this lottery: {sorted(cumulation)}")
            print(f"Our lucky numbers: {sorted(self.args)}")
            common = (self.args.intersection(cumulation))
            if len(common) == 0:
                print("Unfortunately, no hits :(")
            else:
                print(f"Number of hits {len(common)}, common numbers are {sorted(common)}")

        self.args = set(self.args)
        if len(self.args) == 6:
            if all(isinstance(arg, int) and arg in range(1, 50) for arg in self.args):
                single_check()
            else:
                raise ValueError("Wrong parameter has been provided \nPossible errors:\nNumber out of range <1,49>\n"
                                 "It is not an integer number\nThere is a duplication in your picks")
        elif len(self.args) == 0:
            self.args = set(random.sample(range(1, 50), 6))
            single_check()
        else:
            print("Amount of given picks is not equal to 6")

    def check_until(self, hits):
        def many_checks():
            """Function run cumulations and check with our coupon until the number of given hits is met."""
            q = 1
            common = []
            while len(common) < hits:
                cumulation = set(random.sample(range(1, 50), 6))
                common = self.args.intersection(cumulation)
                print(f"{q} Lottery hits : {sorted(cumulation)}, intersection {len(common)}")
                q += 1
            else:
                print(f"Your picks {sorted(self.args)}")
                print(f"Number of tries to hit {hits} in this lottery: {q - 1}, common numbers are {sorted(common)}.")

        self.args = set(self.args)
        if len(self.args) == 6:
            if all(isinstance(arg, int) and arg in range(1, 50) for arg in self.args):
                many_checks()
            else:
                raise ValueError(
                    "Wrong parameter has been provided \nPossible errors:\nNumber out of range <1,49>\n"
                    "It is not an integer number\nThere is a duplication in your picks")
        elif len(self.args) == 0:
            self.args = set(random.sample(range(1, 50), 6))
            many_checks()
        else:
            print("Amount of given picks is not equal to 6")


coupon = Lotto(13, 26, 41, 15, 7, 34)
coupon.check_until(3)
coupon.one_check()
