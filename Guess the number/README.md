# Program guess the number allows you to enter or randomly select a number, and then tries to guess it from the default or selected range.

Requirements: Python 3, random module

# Program:
- allows you to choose your lucky number or randomly pick it by the computer
- allows you to select the low and high range or stay at the default range <1,1000>
- after specifying ranges and lucky number, program checks if the number is in the range
- program picks a number from the given range and checks if it is a lucky number
- if the drawn number is smaller than the lucky number, the lower range increases
  to drawn number + 1 Example: 10 was drawn, lucky number 100, bottom range increased to 11
- if the drawn number is greater than the lucky number, the upper range decreases
  to the drawn number -1
- when hitting a lucky number, the program prints how many times it took and the final range from which it
was drawn
