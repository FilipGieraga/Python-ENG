# Program solving simple sudoku

Requirements: Python 3, numpy module

# Function sudoku_examples():
It displays 5 sudoku examples and allows you to choose which one will be solved with the next solve_sudoku() function.
Unfortunately, the program is not perfect and only solves them in the way I know. One of these sudoku examples is
partially filled in so that the program can solve it, and one shows the problem of the entire algorithm that I created.
The remaining 3 are pure website templates that fill up with no additional conditions.



Wyświetla nam przykładowe sudoku, których jest pięć i pozwala wybrać które z nich ma być rozwiązane za pomocą kolejnej funkcji solve().
Program niestety nie jest idealny i rozwiązuje je jedynie takim sposobem jaki jest mi znany. Jedno z tych przykładowych sudoku jest
częsciowo wypełnione aby mogło się rozwiązać, a jedno pokazuje problem całego algorytmu, który stworzyłem, bez szukania gotowych odpowiedzi.
Pozostałe 3 to czyste szablony ze stron internetowych wypełniające się bez dodatkowych warunków

# Function solve()
After selecting a specific sudoku, the program goes to search for a solution and runs until all zeros disappear in sudoku, or 15 loops were executed.
At the beginning it creates a list of possible numbers to enter in our sudoku, numbers from 1 to 9. An empty dictionary is also declared.
The function iterates through each nonzero element in sudoku and brakes it into appropriate squares like those used in sudoku. Fields already filled
remain intact. For each non-zero field in sudoku, an empty solutions list is created that stores solutions for specific coordinates.
In order for a solution to be included in the solutions list, it must meet three conditions: <br>
missing a given number vertically, horizontally and in a given square <br>
This condition is checked for all numbers that can be entered from 1 to 9.
For each non-zero element, the coordinates and solutions are written in the declared dictionary in the example form ..., (3, 2): [7, 8], (3, 6): [8], ...<br>
We can see here that the element with coordinates (3,2) has two solutions and in this iteration of a loop it will not be entered into sudoku, while the
coordinates (3,6) have only one solution that is 8, and will be filled in in this iteration of the loop in sudoku.
If a given item has only one solution, it is entered into sudoku, as there is no doubt that it must go there.
The program only partially completes the sudoku at each iteration, only when it is sure. At the end of each iteration, it shows us: <br>
Dictionary of coordinates and solutions for a given iteration, <br> displays approach number<br> number of sudoku inserts<br>
Unfortunately, sudoku is not that simple, that we only need to check the number vertically, horizontally and in square. There are sudoku puzzles which,
for each non-zero element have many solutions and this is the case with sudoku no. 3, where the program cannot insert anything at the first iteration, so
it loops 15 times and ends.<br>
Despite the undoubted flaws that this program has, I am sharing it because it took me a lot of time to get to the solution of even some of the possible sudoku
puzzles.


![alt tag](https://github.com/FilipGieraga/Python-ENG/blob/master/9.%20Sudoku%20Solver/Example_solved.PNG)
