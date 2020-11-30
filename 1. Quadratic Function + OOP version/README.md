# Quadratic function program let us calculate delta and determine zeros, if any.

Requirements : Python 3, math module

# Program:
- checks if the function is quadratic
- in case of a linear function, gives the point of intersection
- computes the delta of the quadratic function
- counts the vertex
- takes numerical input which must be int or float, otherwise asks for the correct parameters
- counts and gives the number of zeros (if any) based on the delta
- determines zero places

# Detailed description:
First, the parameters() function is called, which takes the values ​​of 3 parameters a, b, c from the user.
If any of the parameters is entered incorrectly, you have to start over.
Valid parameters are integers and decimals.
Then the program checks if the value of the parameter a is zero, if so, it counts the zero place for linear
function and prints the result, calling choice().
If not, it counts the delta and calls the m_zero() function, which passes a parameter list a, b, c and the result of delta.
In m_zero() function, the last parameter from the list is assigned to the delta variable, we check whether delta
is greater than zero. If it's not, you cannot take a square from it. However, you can always count the vertex
coordinates and it's done in the next step.
If delta is less than zero, we print no zeros, <br>if it is equal to zero we have one zero that
is calculated from the formula, rounded to 2 decimal places and printed.<br>
If delta is greater than zero, we have two zeros which are also rounded and printed.<br>
Finally, after printing the results, the function choice() is called, which allows you to call the paramaters() function again.
and start counting again or end the program.
