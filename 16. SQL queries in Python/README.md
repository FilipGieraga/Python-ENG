# The SQL query program allows us to display selected information about the 2018/2019 season in laliga.

Requirements: Python 3, pandas module, pandasql module <br><br>

First, the data from laliga.csv file is read.<br>

The sql_df() function is used in function queries() and gets the content of each query, printing the result to us. <br>
<br>
There are 11 queries in total and each one of them is described.
Some inquiries collect information from the user, such as what team he wants to display.
To facilitate use of this program, when the user is required to enter a position or team,
they are displayed and you just need to copy them without the quotes.
<br><br>
The main body of the program is the queries() function, which displays what queries we can execute.
They are numbered and we just need to provide the number of query and click enter.
After each query, the program waits for an enter key to continue.
Sometimes, unfortunately, enter moves the line to a new line and then re-enter ends the program.
To prevent this from happening, if the program takes us to a new line, hit backspace and then enter.
To end the program, type end or any string when selecting the query.

