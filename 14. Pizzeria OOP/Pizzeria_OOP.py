class Pizza:
    menu = []

    item_nr = 0

    ingredients = ["cheese", "ham", "mushrooms", "jalapeno", "bacon", "onion", "corn", "peas", "sausage", "tomato",
                   "pickled cucumber", "tabasco", "sun-dried tomatoes", "paprika", "parmesan", "mozzarella", "basil",
                   "arugula", "oregano"]

    size = ["28cm", "40cm", "52cm"]

    def __init__(self, pizza, ingr, size, price):
        for s in ingr:
            if s.lower() not in Pizza.ingredients:
                raise ValueError("We don't have such ingredient :(")
        self.__class__.menu.append(pizza)
        self.pizza = pizza
        self.ingredient = ingr
        self.size = size
        self.price = price
        self.number = Pizza.item_nr + 1
        Pizza.item_nr += 1

    def size_price(self, size):
        if size == 1:
            price = self.price
        elif size == 2:
            price = 1.4 * self.price
        elif size == 3:
            price = 2 * self.price
        return f"{round(price)}zł"

    @classmethod
    def do_it_yourself(cls):
        list_1 = []
        while True:
            try:
                x = int(input("How many ingredients?\n"))
                if x not in range(1, 5):
                    raise ValueError
            except:
                print("The allowed number of ingredients range from 1 to 4")
            else:
                break
        q = x
        for i, ingredient in enumerate(Pizza.ingredients, start=1):
            print(i, ingredient)
        for x in range(0, x):
            s = int(input("Which ingredient would you like to choose?\n"))
            t = Pizza.ingredients[s - 1]
            list_1.append(t)
        for i, size in enumerate(Pizza.size, start=1):
            print(i, f"Size: {size}")
        s = int(input("What size?\n"))
        if q == 2 and s == 1:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 20 zł")
        elif q == 3 and s == 1:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 22 zł")
        elif q == 4 and s == 1:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 24 zł")
        elif q == 2 and s == 2:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 24 zł")
        elif q == 3 and s == 2:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 26 zł")
        elif q == 4 and s == 2:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 28 zł")
        elif q == 2 and s == 3:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 32 zł")
        elif q == 3 and s == 3:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 34 zł")
        elif q == 4 and s == 3:
            print(f"Ingredients: {list_1}, size: {Pizza.size[s - 1]}, price 36 zł")
        else:
            print("Order error")

    def order(self):
        for i, size in enumerate(Pizza.size, start=1):
            print(i, f"Size: {size}, Price: {self.size_price(i)} zł.")
        size = int(input("What size for pizza?\n"))
        price = self.size_price(size)
        size = Pizza.size[size - 1]
        modification = input("Do you want to change anything?(y/n)\n")

        if modification == "n":
            address = input("Enter the street and apartment number:\n")
            phone = int(input("Enter phone number (without dashes):\n"))
            print(f"The order has been placed for the address: {address}. If necessary, we will call on: {phone}")
            print("Your order:")
            print(f"Pizza name: {self.pizza}\nIngredients: {self.ingredient}\nSize: {size}\nPrice: {price}")


        elif modification == "y":
            ingr = self.ingredient.copy()
            meat = ["ham", "bacon", "sausage"]
            price = price[:2]
            price = int(price)
            decision = int(input("What would you like to change?\n1-Add ingredient\n2-Remove ingredient\n"
                                 "3-Replace ingredient\n4-End changes\n"))

            while decision != 4:
                if decision == 1:
                    for i, ingredient in enumerate(Pizza.ingredients, start=1):
                        print(i, ingredient)
                    s = int(input("Which ingredient do you want to add?\n"))
                    if Pizza.ingredients[s - 1] in meat:
                        price += 3
                    else:
                        price += 2
                    print(f"Price: {price}")
                    ingr.append(Pizza.ingredients[s - 1])
                    print(ingr)


                elif decision == 2:
                    for i, ingredient in enumerate(ingr, start=1):
                        print(i, ingredient)
                    u = int(input("Which ingredient do you want to remove?\n"))
                    if Pizza.ingredients[u - 1] in meat:
                        price -= 3
                    else:
                        price -= 2
                    print(f"Price: {price}")
                    ingr.pop(u - 1)
                    print(ingr)


                elif decision == 3:
                    for i, ingredient in enumerate(ingr, start=1):
                        print(i, ingredient)
                    z = int(input("Which ingredient do you want to remove?\n"))
                    for i, ingredient in enumerate(Pizza.ingredients, start=1):
                        print(i, ingredient)
                    z1 = int(input(f"Which ingredient instead of {ingr[z - 1]}?\n"))
                    if Pizza.ingredients[z - 1] in meat:
                        price -= 3
                    else:
                        price -= 2
                    if Pizza.ingredients[z1 - 1] in meat:
                        price += 3
                    else:
                        price += 2
                    print(f"Price: {price}")
                    ingr.pop(z - 1)
                    ingr.append(Pizza.ingredients[z1 - 1])
                    print(ingr)

                decision = int(input(
                    "What would you like to change?\n1-Add ingredient\n2-Remove ingredient\n3-Replace ingredient\n4-End changes\n"))

            if isinstance(price, int):
                price = str(price) + "zł"
            print("Changes have been made.")
            address = input("Enter the street and apartment number:\n")
            phone = int(input("Enter phone number (without dashes):\n"))
            print(f"The order has been placed for the address: {address}. If necessary, we will call on: {phone}")
            print("Your order:")
            print(f"Pizza name: {self.pizza}\nIngredients: {ingr}\nSize: {size}\nPrice: {price}")

    def __repr__(self):
        return (f"Pizza name: {self.pizza},\nIngredients: {self.ingredient},"
                f"\nPrice for {Pizza.size[0]}:{self.size_price(1)}\n          {Pizza.size[1]}:{self.size_price(2)} \n"
                f"          {Pizza.size[2]}:{self.size_price(3)}"
                f"\nPizza nr: {self.number}")

    @classmethod
    def print_menu(cls):
        print("Our Menu:")
        for i, instance in enumerate(cls.menu, start=1):
            print(i, instance)

    @staticmethod
    def open_hours():
        print("Opening hours are:\nMon-FR 9:00 AM-10:00 PM\nSat: 10:00 AM -00:00 AM")


Margerita = Pizza("Margerita", [Pizza.ingredients[0], Pizza.ingredients[-1]], Pizza.ingredients[0], 18)
Capricciosa = Pizza("Capricciosa", (Pizza.ingredients[0], Pizza.ingredients[1], Pizza.ingredients[2]), Pizza.size[0],
                    20)
Rimini = Pizza("Rimini", ("bacon", "onion"), Pizza.size[0], 20)
Wege = Pizza("Wege", ("mushrooms", "paprika", "corn", "peas"), Pizza.size[0], 20)

# -------------
# Print menu:
Pizza.print_menu()
print("\n\n")

# -------------
# Open hours:
Pizza.open_hours()
print("\n\n")
#
# --------------
# Size price, where size is given in brackets 1- small, 2 - medium 3 - large:
print(Margerita.size_price(3))
print("\n\n")

# --------------
# Pizza will be printed this way:
print(Capricciosa)
print("\n\n")

# --------------
# We can make a pizza on our own with ingredients declared in Pizza class:
Pizza.do_it_yourself()
print("\n\n")
#
# --------------
# We can order pizza from the menu:
Margerita.order()
print("\n\n")

# --------------
# Total nr of pizzas in pizzeria:
print(Pizza.item_nr)
print("\n\n")

print(Margerita.__dict__)
