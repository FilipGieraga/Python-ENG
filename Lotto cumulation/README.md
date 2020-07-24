# The Lotto program simulates the lotto cumulation allowing the user to select their numbers, pick them automatically, check how many numbers have been hit and draw automatically as long as picked amount of numbers is hit.

Requirements: Python 3, random module

# Program:
- allows you to enter your lucky numbers, i.e. 6 integers,
  range from 1 to 49, no repetitions
- allows you to generate your lucky number automatically
- draws the results of lotto cumulation
- checks if there are any hits in lucky numbers and counts them
- asks the user how many hits he would like to get from 1 to 6
- draws as long as it hits the amount of hits specified by us,
  lotto cumulation result remains unchanged
- the results of rollover and our lottery tickets are sorted in ascending order,
  to make them easier to read

# Detailed description:
The program starts by calling the lotto () function, asking the user if he wants to choose his numbers.
If so, it creates an empty set (set()) that will hold our chosen numbers. Program
allows you to enter individual elements, while checking whether the numbers are in the appropriate range,
whether they are not repeated and whether they are integers at all.
If the user chooses not to enter them, they will be selected automatically.
Then, the results of the jackpots are drawn and printed, along with ours for comparison and the number of our hits.
The program asks the user how many hits he would like to get. The number that can be entered here is in
range from 1 to 6, otherwise the program asks for re-input.
A while loop is executed which runs until the number of automatically generated hits matches
with cumulation results to the extent that was previously determined.
The program prints us how many times it has looped to hit the given number and shows what numbers have overlapped
in case of drawn numbers and cumulation results.
Finally, the choice function is called, which allows you to start all over again or exit the program.
