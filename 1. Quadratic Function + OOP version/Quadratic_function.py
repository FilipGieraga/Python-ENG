import math


def choice():
    choi = input("Would you like to try again?(y/n)\n")
    if choi == "y":
        parameters()
    else:
        print("Thank you for using the program.")


def parameters(a=0, b=0, c=0):
    print("Quadratic function with formula ax^2+bx+c=0")
    while True:
        try:
            a = float(input("Provide parameter a: \n"))
            b = float(input("Provide parameter b: \n"))
            c = float(input("Provide parameter c : \n"))
        except Exception as error:
            print(f"Error occured: {error}\nWrong parameters value, please try again.")
        else:
            break

    if a == 0.0:
        print(f"This function is linear, not quadratic.\nIt's formula y={int(b)}x+{int(c)}")
        if c == 0.0:
            print("The zero of this linear function is the middle of the plot (0,0) ")
        elif b == 0.0:
            print("Function is constant.")
        else:
            p1 = c / (-b)
            print(f"The zero of this linear function is at x={round(p1, 2)}")
        choice()
    else:
        delta = b ** 2 - 4 * a * c
        d = [a, b, c, delta]
        print(f"Delta is equal to {delta}")
        return (m_zerowe(d))


def m_zerowe(d):
    delta = d[3]
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
    else:
        print("No root of delta .")
    p = -d[1] / (2 * d[0])
    q = -d[3] / (4 * d[0])
    p = round(p, 2)
    q = round(q, 2)
    print(f"The vertex of the function has coordinates x = {p} y = {q}")

    if d[3] < 0:
        print("No zeros.")
    elif d[3] == 0:
        m1 = -d[1] / (2 * d[0])
        m1 = round(m1, 2)
        print(f"Function has one zero, where x = {m1} ")
    else:
        m2 = (-d[1] - math.sqrt(d[3])) / (2 * d[0])
        m3 = (-d[1] + math.sqrt(d[3])) / (2 * d[0])
        m2 = round(m2, 2)
        m3 = round(m3, 2)
        print(f"Function has two zeros, where x1 = {m2} and x2 = {m3} ")
    choice()


if __name__ == "__main__":
    parameters()
