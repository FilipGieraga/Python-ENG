import random
import datetime
import json



imiona_męskie = """Adam, Adolf, Adrian, Albert, Aleksander, Aleksy, Alfred, Amadeusz, Andrzej, Antoni, Arkadiusz, Arnold, Artur,
Bartłomiej, Bartosz, Benedykt, Beniamin, Bernard, Błażej, Bogdan, Bogumił, Bogusław, Bolesław, Borys, Bronisław,
Cezary, Cyprian, Cyryl, Czesław,
Damian, Daniel, Dariusz, Dawid, Dionizy, Dominik, Donald,
Edward, Emanuel, Emil, Eryk, Eugeniusz,
Fabian, Feliks, Ferdynand, Filip, Franciszek, Fryderyk,
Gabriel, Gerard, Grzegorz, Gustaw,
Henryk, Herbert, Hilary, Hubert,
Ignacy, Igor, Ireneusz,
Jacek, Jakub, Jan, Janusz, Jarosław, Jerzy, Joachim, Józef, Julian, Juliusz,
Kacper, Kajetan, Kamil, Karol, Kazimierz, Klaudiusz, Konrad, Krystian, Krzysztof,
Lech, Leon, Leszek, Lucjan, Ludwik,
Łukasz,
Maciej, Maksymilian, Marceli, Marcin, Marek, Marian, Mariusz, Mateusz, Michał, Mieczysław, Mikołaj, Miłosz, Mirosław,
Nikodem, Norbert,
Olaf, Olgierd, Oskar,
Patryk, Paweł, Piotr, Przemysław,
Radosław, Rafał, Remigiusz, Robert, Roman, Rudolf, Ryszard,
Sebastian, Seweryn, Sławomir, Stanisław, Stefan, Sylwester, Szymon,
Tadeusz, Teodor, Tomasz,
Wacław, Waldemar, Wiesław, Wiktor, Witold, Władysław, Włodzimierz, Wojciech,
Zbigniew, Zdzisław, Zenon, Zygmunt"""

imiona_męskie = imiona_męskie.replace('\n',' ')
imiona_męskie=imiona_męskie.split(", ")

imiona_żeńskie="""Ada, Adela, Adelajda, Adrianna, Agata, Agnieszka, Aldona, Aleksandra, Alicja, Alina, Amanda, Amelia, Anastazja,
Andżelika, Aneta, Anita, Anna, Antonina,
Barbara, Beata, Berenika, Bernadeta, Blanka, Bogusława, Bożena,
Cecylia, Celina, Czesława,
Dagmara, Danuta, Daria, Diana, Dominika, Dorota,
Edyta, Eliza, Elwira, Elżbieta, Emilia, Eugenia, Ewa, Ewelina,
Felicja, Franciszka,
Gabriela, Grażyna,
Halina, Hanna, Helena,
Iga, Ilona, Irena, Irmina, Iwona, Izabela,
Jadwiga, Janina, Joanna, Jolanta, Jowita, Judyta, Julia, Julita, Justyna,
Kamila, Karina, Karolina, Katarzyna, Kazimiera, Kinga, Klaudia, Kleopatra, Kornelia, Krystyna,
Laura, Lena, Leokadia, Lidia, Liliana, Lucyna, Ludmiła, Luiza,
Łucja,
Magdalena, Maja, Malwina, Małgorzata, Marcelina, Maria, Marianna, Mariola, Marlena, Marta, Martyna, Marzanna, Marzena, Matylda,
Melania, Michalina, Milena, Mirosława, Monika,
Nadia, Natalia, Natasza, Nikola, Nina,
Olga, Oliwia, Otylia,
Pamela, Patrycja, Paula, Paulina,
Regina, Renata, Roksana, Róża, Rozalia,
Sabina, Sandra, Sara, Sonia, Stanisława, Stefania, Stella, Sylwia,
Tamara, Tatiana, Teresa,
Urszula,
Weronika, Wiesława, Wiktoria, Wioletta,
Żaneta,
Zofia, Zuzanna, Zyta"""

imiona_żeńskie = imiona_żeńskie.replace('\n',' ')
imiona_żeńskie=imiona_żeńskie.split(", ")

surnames= """
 Nowak Kowalski Wiśniewski Wójcik Kowalczyk Kamiński Lewandowski Zieliński Szymański Woźniak Dąbrowski\
 Kozłowski  Jankowski  Mazur  Wojciechowski  Kwiatkowski  Krawczyk  Kaczmarek  Piotrowski  Grabowski\
 Zając Pawłowski Michalski Król Wieczorek Jabłoński Wróbel Nowakowski Majewski Olszewski Stępień\
 Malinowski Jaworski Adamczyk Dudek Nowicki Pawlak Górski Witkowski Walczak Sikora Baran Rutkowski\
 Michalak Szewczyk Ostrowski Tomaszewski Pietrzak Zalewski Wróblewski Marciniak Jasiński Zawadzki\
 Bąk Jakubowski Sadowski Duda Włodarczyk Wilk Chmielewski Borkowski Sokołowski Szczepański Sawicki\
 Kucharski Lis Maciejewski Kubiak Kalinowski Mazurek Wysocki Kołodziej Kaźmierczak Czarnecki Sobczak\
 Konieczny Urbański Głowacki Wasilewski Sikorski Zakrzewski Krajewski Krupa Laskowski Ziółkowski Gajewski\
 Mróz Brzeziński Szulc Szymczak Makowski Baranowski Przybylski Kaczmarczyk Borowski Błaszyk Adamski Górecki\
 Chojnacki Kania Leszczyński Janik Szczepaniak Czerwiński Kozioł Mucha Lipiński Wesołowski Kozak Cieślak\
 Kowalewski Andrzejewski Mikołajczyk Jarosz Musiał Zięba Kowalik Kołodziejczyk Markowski Brzozowski Kopeć\
 Nowacki Orłowski Domański Żak Tomczyk Kurek Piątek Pawlik Tomczak Markiewicz Ciesielski Wawrzyniak Kot\
 Wójtowicz Polak Wolski Kruk Stasiak Stankiewicz Sowa Łuczak Wierzbicki Jastrzębski Urbaniak Karpiński\
 Czajkowski Piasecki Gajda Nawrocki Bednarek Stefański Klimek Janicki Jóźwiak Dziedzic Sosnowski Bielecki\
 Majchrzak Madej Leśniak Milewski Maj Kowal Małecki Śliwiński Socha Skiba Marek Dobrowolski Domagała\
 Bednarczyk Wrona Urban Olejniczak Pająk Matuszewski Romanowski Kasprzak Świątek Wilczyński Ratajczak\
 Kurowski Michalik Owczarek Orzechowski Grzelak Łukasik Olejnik Sobolewski Rogowski Mazurkiewicz Barański\
 Bukowski Matusiak Sroka Kosiński Kędzierski Skowroński Marcinkowski"""


surnames=surnames.split()

departments=["Research and development", "Accounting", "Compliance", "IT", "Logistics", "Marketing", "HR"]
hr_positions=["HR Manager", "Recruitment", "Compensation and Benefits",
               "Safety and Health","Training and Development","Industrial relations"]


def random_start_date():
    """A random date between early 2010 and today"""
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date.today()
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%d-%m-%Y")


def random_age():
    """A random date between 1975 and 1992"""
    start_date = datetime.date(1975, 1, 1)
    end_date = datetime.date(1992, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def age_counter(data_urodzenia):
    """Age couter for company employers"""
    dzisiaj = datetime.date.today()
    wiek = dzisiaj.year - data_urodzenia.year -((dzisiaj.month, dzisiaj.day)<(data_urodzenia.month, data_urodzenia.day))
    return wiek


def employers(number_of_employees, company_name):
    """Personal data generator"""
    company = {}
    x=set(random.sample(range(10000,100000),k=1000))


    for i in range(number_of_employees):
        employee_id = x.pop()
        gender = random.choice(["M", "K"])
        if gender == "M":
            name= random.choice(imiona_męskie)
            gender= "Man"
        else:
            name = random.choice(imiona_żeńskie)
            gender = "Woman"
        surname= random.choice(surnames)
        if gender == "Woman":
            list_surname = list(surname)
            if list_surname[-1]== "i":
                list_surname[-1] = "a"
                surname = ''.join(list_surname)
        email= name.lower() + "." + surname.lower() + "@" + company_name.lower() + ".com"
        start_date = random_start_date()
        start_date1= datetime.datetime.strptime(start_date, "%d-%m-%Y")
        work_experience= datetime.datetime.today() - start_date1
        work_experience= work_experience.days
        date_of_birth = random_age()
        age= age_counter(date_of_birth)
        date_of_birth=date_of_birth.strftime("%d-%m-%Y")

        company.update({employee_id :
                          {"Name":name,
                           "Surname":surname,
                           "Gender":gender,
                           "E-mail":email,
                           "Date of birth": date_of_birth,
                           "Age": age,
                           "Start date": start_date,
                           "Work experience(in days)": work_experience,
                           }
                        })
    return company

def company_structure(company, company_name):
    """Generating company structure, job positions and salaries"""
    list_staz=[]
    list_klucze=[]
    for k,v in company.items():
        list_staz+=([v["Work experience(in days)"]])
        list_klucze+=[k]


    company_size= len(company) / 100
    company_size=int(company_size)


    l_menadzerow=10
    l_supervisorow=20
    l_hr=(len(company)*0.03)
    l_hr= round(l_hr,0)
    l_hr=int(l_hr)
    wykorzystane_dzialy = random.sample(departments[0:-1], company_size)
    used_departaments1=wykorzystane_dzialy.copy()
    stanowiska_hr1=hr_positions.copy()


    for i in range(len(company)):
        if i==0:
            klucz_1=list_staz.index(max(list_staz)) # index najwyzszej wartosci w liscie staz
            klucz_2=list_klucze[klucz_1] # wartosc
            company[klucz_2]["Position"] = 'CEO'
            company[klucz_2]["E-mail"] = company[klucz_2]["Name"].lower()+"."+company[klucz_2]["Surname"].lower()+"-CEO@"+company_name.lower()+".com"
            if company_size==1:
                earnings = random.randint(200000, 250000)
                earnings=round(earnings, -1)
            elif company_size==2:
                earnings = random.randint(230000, 280000)
                earnings = round(earnings, -1)
            elif company_size==3:
                earnings = random.randint(265000, 300000)
                earnings = round(earnings, -1)
            elif company_size==4:
                earnings = random.randint(290000, 330000)
                earnings = round(earnings, -1)
            elif company_size==5:
                earnings = random.randint(320000, 400000)
                earnings = round(earnings, -1)
            elif company_size==6:
                earnings = random.randint(380000, 500000)
                earnings = round(earnings, -1)
            company[klucz_2]["Annual earnings"] = str(earnings) + " zł"
            company[klucz_2]["Monthly earnings"] = str(int(earnings / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment1=i


        elif i in range(i, increment1 + company_size + 1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            company[klucz_2]["Position"] = 'President'
            ### Oddział
            company[klucz_2]["Department"] = used_departaments1.pop()
            if company_size==1:
                earnings = random.randint(150000, 175000)
                earnings=round(earnings, -1)
            elif company_size==2:
                earnings = random.randint(160000, 180000)
                earnings = round(earnings, -1)
            elif company_size==3:
                earnings = random.randint(175000, 190000)
                earnings = round(earnings, -1)
            elif company_size==4:
                earnings = random.randint(190000, 210000)
                earnings = round(earnings, -1)
            elif company_size==5:
                earnings = random.randint(200000, 240000)
                earnings = round(earnings, -1)
            elif company_size==6:
                earnings = random.randint(230000, 260000)
                earnings = round(earnings, -1)
            company[klucz_2]["Annual earnings"] = str(earnings) + " zł"
            company[klucz_2]["Monthly earnings"] = str(int(earnings / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment2 = i


        elif i in range(i, increment2 + company_size + 1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            company[klucz_2]["Position"] = 'Vice-President'
            ### Oddział
            if len(used_departaments1)==0:
                used_departaments1 = wykorzystane_dzialy.copy()
            company[klucz_2]["Department"] = used_departaments1.pop()
            if company_size==1:
                earnings = random.randint(100000, 115000)
                earnings=round(earnings, -1)
            elif company_size==2:
                earnings = random.randint(120000, 140000)
                earnings = round(earnings, -1)
            elif company_size==3:
                earnings = random.randint(130000, 160000)
                earnings = round(earnings, -1)
            elif company_size==4:
                earnings = random.randint(150000, 175000)
                earnings = round(earnings, -1)
            elif company_size==5:
                earnings = random.randint(160000, 180000)
                earnings = round(earnings, -1)
            elif company_size==6:
                earnings = random.randint(175000, 199000)
                earnings = round(earnings, -1)
            company[klucz_2]["Annual earnings"] = str(earnings) + " zł"
            company[klucz_2]["Monthly earnings"] = str(int(earnings / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment3 = i


        elif i in range(i, increment3 + (l_menadzerow * company_size) + 1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            company[klucz_2]["Position"] = 'Manager'
            ### Oddział
            if len(used_departaments1)==0:
                used_departaments1 = wykorzystane_dzialy.copy()
            company[klucz_2]["Department"] = used_departaments1.pop()
            if company_size==1:
                earnings = random.randint(70000, 95000)
                earnings=round(earnings, -1)
            elif company_size==2:
                earnings = random.randint(78000, 95000)
                earnings = round(earnings, -1)
            elif company_size==3:
                earnings = random.randint(85000, 100000)
                earnings = round(earnings, -1)
            elif company_size==4:
                earnings = random.randint(95000, 105000)
                earnings = round(earnings, -1)
            elif company_size==5:
                earnings = random.randint(100000, 110000)
                earnings = round(earnings, -1)
            elif company_size==6:
                earnings = random.randint(105000, 115000)
                earnings = round(earnings, -1)
            company[klucz_2]["Annual earnings"] = str(earnings) + " zł"
            company[klucz_2]["Monthly earnings"] = str(int(earnings / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment4 = i


        elif i in range(i, increment4 + (l_supervisorow * company_size) + 1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            company[klucz_2]["Position"] = 'Supervisor'
            ### Oddział
            if len(used_departaments1)==0:
                used_departaments1 = wykorzystane_dzialy.copy()
            company[klucz_2]["Department"] = used_departaments1.pop()
            if company_size==1:
                earnings = random.randint(50000, 65000)
                earnings=round(earnings, -1)
            elif company_size==2:
                earnings = random.randint(60000, 70000)
                earnings = round(earnings, -1)
            elif company_size==3:
                earnings = random.randint(70000, 80000)
                earnings = round(earnings, -1)
            elif company_size==4:
                earnings = random.randint(85000, 98000)
                earnings = round(earnings, -1)
            elif company_size==5:
                earnings = random.randint(95000, 103000)
                earnings = round(earnings, -1)
            elif company_size==6:
                earnings = random.randint(100000, 107000)
                earnings = round(earnings, -1)
            company[klucz_2]["Annual earnings"] = str(earnings) + " zł"
            company[klucz_2]["Monthly earnings"] = str(int(earnings / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment5 = i
            kierownik = 1

        elif i in range(i,increment5+l_hr+1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            if len(stanowiska_hr1)==0:
                stanowiska_hr1 = hr_positions.copy()
                stanowiska_hr1=stanowiska_hr1[1:]
            if company_size > 3 and kierownik < 2:
                company[klucz_2]["Position"] = stanowiska_hr1[0]
                kierownik+=1
            else:
                company[klucz_2]["Position"] = stanowiska_hr1.pop(0)
            ### Oddział
            company[klucz_2]["Department"] = departments[-1]
            if company_size==1 and company[klucz_2]["Position"] == 'Kierownik':
                earnings = random.randint(70000, 95000)
                earnings = round(earnings, -1)
            elif company_size==2 and company[klucz_2]["Position"] == 'Kierownik':
                earnings = random.randint(78000, 95000)
                earnings = round(earnings, -1)
            elif company_size==3 and company[klucz_2]["Position"] == 'Kierownik':
                earnings = random.randint(85000, 100000)
                earnings = round(earnings, -1)
            elif company_size==4 and company[klucz_2]["Position"] == 'Kierownik':
                earnings = random.randint(95000, 105000)
                earnings = round(earnings, -1)
            elif company_size==5 and company[klucz_2]["Position"] == 'Kierownik':
                earnings = random.randint(100000, 110000)
                earnings = round(earnings, -1)
            elif company_size==6 and company[klucz_2]["Position"] == 'Kierownik':
                earnings = random.randint(105000, 115000)
                earnings = round(earnings, -1)

            if company_size==1 and company[klucz_2]["Position"] != 'Kierownik':
                earnings = random.randint(50000, 65000)
                earnings=round(earnings, -1)
            elif company_size==2 and company[klucz_2]["Position"] != 'Kierownik':
                earnings = random.randint(60000, 70000)
                earnings = round(earnings, -1)
            elif company_size==3 and company[klucz_2]["Position"] != 'Kierownik':
                earnings = random.randint(70000, 80000)
                earnings = round(earnings, -1)
            elif company_size==4 and company[klucz_2]["Position"] != 'Kierownik':
                earnings = random.randint(85000, 98000)
                earnings = round(earnings, -1)
            elif company_size==5 and company[klucz_2]["Position"] != 'Kierownik':
                earnings = random.randint(95000, 103000)
                earnings = round(earnings, -1)
            elif company_size==6 and company[klucz_2]["Position"] != 'Kierownik':
                earnings = random.randint(100000, 107000)
                earnings = round(earnings, -1)
            company[klucz_2]["Annual earnings"] = str(earnings) + " zł"
            company[klucz_2]["Monthly earnings"] = str(int(earnings / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)


        else:
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            company[klucz_2]["Position"] = 'Regular employee'
            if len(used_departaments1)==0:
                used_departaments1 = wykorzystane_dzialy.copy()
            company[klucz_2]["Department"] = used_departaments1.pop()
            if company_size<=3:
                earnings = random.randint(40000, 60000)
                earnings=round(earnings, -1)
            elif company_size>3:
                earnings = random.randint(55000, 85000)
                earnings = round(earnings, -1)
            company[klucz_2]["Annual earnings"] = str(earnings) + " zł"
            company[klucz_2]["Monthly earnings"] = str(int(earnings / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
    return company

def print_employers(company):
    for k,v in company.items():
        print(k,v)


def to_json(company):
    with open("Employees.json", "w", encoding='utf-8') as outfile:
        json.dump(company, outfile, indent=2, ensure_ascii=False)
    print("Data loaded to Employees.json file.")


number_of_employees=500
company_name= "Google"
company = employers(number_of_employees, company_name)
company = company_structure(company, company_name)
print_employers(company)
to_json(company)


