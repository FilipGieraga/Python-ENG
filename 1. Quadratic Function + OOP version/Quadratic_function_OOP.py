import math


class QuadraticFunc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        if all(isinstance(i, (int, float)) for i in [self.a, self.b, self.c]):
            if self.a == 0.0:
                print(f"This function is linear, not quadratic.\nIt's formula y={int(self.b)}x+{int(self.c)}")
                if self.c == 0.0:
                    print("The zero of this linear function is the middle of the plot (0,0) ")
                elif self.b == 0.0:
                    print("Function is constant.")
                else:
                    p1 = self.c / (-self.b)
                    print(f"The zero of this linear function is at x={round(p1, 2)}")
            else:
                delta = self.b ** 2 - 4 * self.a * self.c
                print(f"Delta for this function equals to {delta}")
                p = -self.b / (2 * self.a)
                q = -delta / (4 * self.a)
                p = round(p, 2)
                q = round(q, 2)
                print(f"The vertex of the function has coordinates x = {p} and y = {q}")
                if self.a > 0:
                    print("Ascending function")
                else:
                    print("Descending function")
                if delta < 0:
                    print("No root of delta, no zeros.")
                elif delta == 0:
                    m1 = -self.b / (2 * self.a)
                    m1 = round(m1, 2)
                    print(f"Function has one zero, where x = {m1} ")
                else:
                    m2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
                    m3 = (-self.b + math.sqrt(delta)) / (2 * self.a)
                    m2 = round(m2, 2)
                    m3 = round(m3, 2)
                    print(f"Function has two zeros, where x1 = {m2} and x2 = {m3} ")
        else:
            print("You provided wrong parameters for this function")


example = QuadraticFunc(2, -6, 1)
example.calculate()
