# This project was made on request

Requirements: Python 3, random module, json module, csv module, pandas module, matplotlib, pdfkit

# Project content:
Let's assume that we want to do a patient weight test all over Poland. For research purposes, we collect the following data from project participants:
name, surname, age, voivodeship, gender, height, weight. Additionally, each project participant receives an ID at the time of joining the project -
A 6-digit unique number. Data collection consists of two stages. The first stage is personal data and assigning an identification number.
This data is available in a CSV file (participants.csv) with the following structure:

name, surname, age, gender, voivodeship, id
"Jan", "Kowalski", 37, "m", "lubuskie", 134567
"Anna", "Nowak", 56, "k", "mazowieckie", 786543
(..)

The second part is an examination of patients performed on special software (e.g. a scale with data recording on a computer). As a result of this
research, we have a file in the json format(participants.json) in the form:
   [
     {'134567': {'height': 182,
             'weight': 76
        }},
     {'786543': {'height': 167,
                 'weight': 52
         }},
     {...}
   ]

The field that combines data from both files is the identifier.

The following steps should be performed in the project:

1. Generate the participants.csv file for at least 200 people. The identifiers must be unique. Names, Surnames and other needed data should be generated
randomly (e.g. from a list of first names, surnames and voivodeships). We assume that the age of participants is between 18-80.
2. Generate a file with random measurements for each participant from the participants.csv file. When generating data, assume that for men height is from
range 168cm-192cm, and weight 58kg-140kg. For women, height is a random number between 156cm-178cm and weight is 42kg-110kg.
4. For each patient, calculate the BMI index and determine the category in which the person is (Underweight, Correct weight, Overweight, Clinical obesity).
  Make statistics in individual groups broken down by women and men.
5. Make a separate BMI histogram for females and males.
6. Make a histogram of the BMI divided into women and men in the age range 18-35, 46-65, over 65.
7. Find the average, maximum and minimum BMI index in the group of women and men.
8. Make a graph of the average BMI (women and men) in individual voivodeships.
9. The results obtained in the analysis should be placed in a pdf file. <br> <br>


### For the html_to_pdf function to work properly, you need to download this program: <br>
https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf <br>
and provide a path to it in the variable path_wkhtmltopdf.
If something goes wrong with this function, the program will not throw an error, only a message.
