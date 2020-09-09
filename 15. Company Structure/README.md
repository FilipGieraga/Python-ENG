# Program Corporate structure:

Requirements: Python 3, random module, json module, pandas module, datetime module

## Documentation:
In this program, I tried to create fictitious employees in the company, while maintaining a structure similar to that which may exist in a corporation.
The main core of the entire program are two functions, ie **employees()** and **company structure()**. <br>
The first function employees() gets two pieces of information that are defined at the end of the program.
These are number_of_employees and company_name. The number of employees should not be less than 100 and no more than 699. I will explain why so, later
in this documentation. The company_name variable is used here for generating emails for all employees and should be given in quotation marks as
string e.g. company_name = "Google". Based on these two pieces of information, the function starts to generate basic data, ie: <br>
- **Employee_ID** - it is a unique five-digit employee identifier, which is randomly selected from range <10000,99999> <br>
- **Gender** - randomly selected Female or Male <br>
- **First name** - on the basis of gender, the employee's first name is drawn from the group of female or male names <br>
- **Surname** - drawn from the surname variable, but if the gender is female, the program additionally checks whether the last letter of the surname is "i"
  and if it is, it changes it to "a". Thanks to this we have eg "Marta Kowalska" instead of "Marta Kowalski" <br>
- **E-mail** - e-mail is generated on the basis of the variables: name, surname and company name,
  example 'przemysław.wiśniewski@google.com'. Everything is lowercase here because email is not case sensitive. <br>
- **Date of birth** - uses a smaller function defined as random_age() and generates a date
  ranged from early 1975 to early 1992. This range is closely related to another variable
  named start date. <br>
- **Age** - based on date of birth variable, function age_counter() counts the age for each employee. <br>
- **Start date** - uses random_start_date() function, which generates us a date from the beginning of 2010 to today. The oldest employee in the company may
  have a start date not before the beginning of 2010. That's why, I wanted the date of birth to be no more than 1992, because then our theoretically
  youngest employee with the longest experience, would have to be at least 18 to start working. <br>
- **Work experience** - given in days, counted by subtracting today's date from start date.
  An employee who would start working on January 27, 2014 would have a work experience of 2357 days on July 11, 2020.
The employees() function after generating mentioned data for each employee, returns
it as a dictionary called company, which is intercepted by the second main function called company_structure(). <br>


The function **company_structure()** takes two variables, i.e. the company that has already been generated from the function employees()
and company_name.
It's purpose is to define both vertical and horizontal structure. **The vertical structure is determined by work experience,
while the horizontal structure is defined by the company_size variable.** <br>
**Company_size** is one of the most important variables in the entire program and the number of employees on individual positions depends on it.
To be able to start assigning data for individual employees, this function must initially fill two variables, which are lists named internship_list and
keys_list with data, i.e. internships of individual employees and corresponding identifiers. Then the company_size variable is calculated, which is
the number_of_employees divided by 100 and rounded down. <br>
The first employee to whom the data will be assigned is the CEO, the variable key_1 looks for the index of the longest work experience in the list
named internships_list. Then the indicated index number is found in the list keys_list and its value, i.e. a specific employee_ID, is assigned to the variable key_2.
CEO is the only employee in the company who has a unique e-mail address, eg "kuba.szulc-CEO@google.com". His annual earnings and earnings of all other
employees depend on the comapny_size.
Earnings are always a random number from a specific range depending on company_size variable. The higher this variable is, the higher everyone's earnings.
CEO is also the only employee who doesn't have an assigned department. Monthly earnings of all employees are the annual earnings divided by 12. <br>
The number of employees for President position and number of departments is equal to the company_size. Departments are randomly selected from the following:<br>
**Research and Development, Accounting, Compliance, IT, Logistics, Marketing** <br>
There are also **HR employees** in the company, which I will mention later. All employees on higher positions are there because of their work experience.
The longer it is, the higher the position.
For each employee on President position one Vice-President is assigned. His earnings are lower and they decrease with every degree in the structure.<br>
The number of managers depends on the company_size and constant l_menadzerow = 10. If company_size is 5, the company will have 50 managers. <br>
The number of supervisors in the company will be twice the number of managers, so that each manager has two supervisors under him.<br>
Now we move on to HR employees, they constitute around 3% of the company. HR department is the only department that doesn't have a President and a Vice-President over it.
There can only be one or two HR Managers, depending on company_size, who have employees dealing with: Recruitment, Compensation and Benefits,
Safety and health, Training and Development, Industrial relations. <br>
Finally, we have regular employees who are divided into individual departments (except HR) more or less equally. <br>
As for the number of employees that can be created, it follows that with 700 employees the company_size would be 7 and there would be no
department to draw, because there are only six. With a number of employees less than 100, the ratio would be 0 and no departments would be drawn.
Besides that, less than 100 employees is more of a company than a corporation. <br>
All employees are saved in the file **Employees.json**
This program has a second part.

![alt tag](https://github.com/FilipGieraga/Python-ENG/blob/master/15.%20Company%20Structure/Structure.png)
![alt tag](https://github.com/FilipGieraga/Python-ENG/blob/master/15.%20Company%20Structure/excel.PNG)
