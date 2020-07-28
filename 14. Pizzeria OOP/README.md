# Pizzeria program is based on object-oriented programming and simulates a pizzeria

Requirements: Python 3

# Class Pizza():
Each instance of the Pizza class that will be declared requires 4 parameters to be entered, ie name, ingredients, size and price.
Sample pizza added in this class: <br>
Wege = Pizza ( 'Wege' ( "mushrooms", "pepper", "corn", "peas") Pizza.size[0], 20) <br>
We declare pizzas with the smallest size, i.e. 28 cm, and the corresponding price. The variable name should reflect the name of the pizza.
Ingredients can be declared in words or as indexes of the list declared in class as Pizza.Ingredients.
When declaring pizzas in the background, item_nr is incremented so that you can tell how many class instances (i.e. our pizzas) we have.
The variable name is stored in the menu list for later use in the print_menu() method of the class.
When declaring each instance of a class, the ingredients in the pizza are also checked. We cannot instantiate the class in which
the ingredient doesn't exist in our list declared inside the class.

When our instances of a class are already declared, we can display each of them legibly thanks to the __repr__ method <br>
With the help of the class function Pizza.print_menu() we can display a menu that consists of all created pizzas. <br>
With the static method Pizza.open_hours() we can see when the pizzeria is open. <br>
The size_price method gives us the prices of the sizes for our pizzas by multiplying the size by the indicator <br>
For size 1, which is the smallest, there is no multiplication. <br>
For size 2, the indicator is 1.4 and for size three, the indicator is 2. <br>
To see the price of the largest Capricciosa size, just enter: print(Capricciosa.size_price(3)) <br>
Pizza.item_nr will show us how many instances are in the class <br>
The two most important methods in this class are self.order() and Pizza.do_it_yourself()


# Pizza.do_it_yourself() method:
This method does not refer to an instance of the class and allows us to create our own pizza from ingredients declared in the class.
First, we need to define how many ingredients we want in our pizza, from 1 to 4.
The ingredients from Pizza.ingredients list are displayed and numbered from one. We only choose the numbers of the ingredients
we want. Finally, we are only asked about the size. After entering this data, the program shows us the price, ingredients and size.


# self.order() method:
This method assumes we want a specific pizza from the menu. Self is a reference to its instance, eg Margerita.order() will allow you to order this
particular one class instance. First, the program asks for a size from 1 to 3. Then it asks if we want to make changes to the pizza.
If so, we can add, remove, replace the ingredient and finish making changes.
In all these operations, the price is adjusted to the changes, taking into account whether the ingredient is meat. <br>
If we subtract the normal ingredient -2 PLN, meat -3 PLN <br>
If we add the normal ingredient + 2 PLN, meat + 3 PLN
Conversion takes into account what is being changed and the prices are the same as for adding and removing, i.e. removing meat ingredient and adding normal
-3 PLN for meat +2 PLN for normal ingredient. The price will be lower by 1 PLN. <br>
Then the program asks us for the address and telephone number. Finally, the method displays that the order has been placed to a specific address and
phone number, price, size and what kind of pizza we will get.
