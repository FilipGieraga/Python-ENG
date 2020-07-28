# Program Company_structure_p2:

Requirements: Python 3, pandas module, xlsxwriter module

## Documentation:
This is a continuation of the Corporate structure program, in which a json file was generated that stores data of all employees.
The data is not sorted in any way, so in the second part we structure the hierarchy. Thanks to this, the CEO is at the top, and ordinary
workers at the bottom. The core of this part of the project is function ** excel_company **, which creates an excel with our data. The first row is
locked to make the data easier to read. All employee data is in the first spreadsheet. To make the file more pleasing to the eye, there are also added
cell formattings for colums such as Gender, Work experience(in days), Annual earnings and Monthly earnings.
Depending on the gender, the cells have red or blue fonts. <br>
Work experience (in days), Annual earnings and Monthly earnings have data bars. <br>
<br>

The second spreadsheet contains statistics that are counted inside the excel_company using smaller, predefined functions that use
pandas module.
The statistics spreadsheet contains information such as:
- Average earnings on all positions
- Median earnings on all positions
- Average age of employees on a given position
- Number of people on a given position
- Number of people in a given department
- The number of women and men in the company
- Average earnings of women and men on the lowest positions

<br>
A column chart is also created showing the average and median monthly earnings for each position.

## The program only shows us the message that the excel file has been saved in the path where the program is located.
