import random
import csv
import json
import pandas as pd
from matplotlib import pyplot as plt
import pdfkit

w = "dolnośląskie kujawsko-pomorskie lubelskie lubuskie łódzkie małopolskie mazowieckie opolskie podkarpackie podlaskie pomorskie śląskie\
    świętokrzyskie warmińsko-mazurskie wielkopolskie zachodniopomorskie"

w = w.split()

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

imiona_męskie = imiona_męskie.replace('\n', ' ')
imiona_męskie = imiona_męskie.split(", ")

imiona_żeńskie = """Ada, Adela, Adelajda, Adrianna, Agata, Agnieszka, Aldona, Aleksandra, Alicja, Alina, Amanda, Amelia, Anastazja,
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

imiona_żeńskie = imiona_żeńskie.replace('\n', ' ')
imiona_żeńskie = imiona_żeńskie.split(", ")

nazwiska = """
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

nazwiska = nazwiska.split()


def choice():
    d1 = input("Do you want to create participants.csv file?(y/n)\n")
    if d1 == "y":
        csv_file()
    else:
        pass
    d2 = input("Do you want to create participants.json file?(y/n)\n")
    if d2 == "y":
        json_file()
    else:
        pass


def csv_file():
    id1 = 100000
    with open("participants.csv", "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['Name', 'Surname', 'Age', 'Gender', 'Voivodeship', 'ID'])
        for i in range(200):
            gender = random.choice(["M", "W"])
            if gender == "M":
                name = random.choice(imiona_męskie)
            else:
                name = random.choice(imiona_żeńskie)
            surname = random.choice(nazwiska)
            if gender == "W":
                list_nazwisko = list(surname)
                if list_nazwisko[-1] == "i":
                    list_nazwisko[-1] = "a"
                    surname = ''.join(list_nazwisko)
            age = random.randint(18, 80)
            voivodeship = random.choice(w)
            id = id1
            csv_writer.writerow([name, surname, age, gender, voivodeship, id])
            i += 1
            id1 += random.randint(1, 4)


def json_file():
    with open("participants.csv", "r") as new_file:
        csv_reader = csv.reader(new_file, delimiter=",", quotechar='"')
        next(csv_reader)
        d = dict()
        x1 = 0  # id2
        x2 = 0  # height
        x3 = 0  # weight
        for line in csv_reader:
            if line:
                id2 = line[5]
                gender1 = line[3]
                x1 = id2
                if gender1 == "M":
                    weight = random.randint(58, 140)
                    height = random.randint(168, 192)
                    x2 = height
                    x3 = weight
                elif gender1 == "W":
                    weight = random.randint(42, 110)
                    height = random.randint(156, 178)
                    x2 = height
                    x3 = weight
                d.update({x1: {"height": x2, "weight": x3}})

    def set_default(d):
        if isinstance(d, set):
            return list(d)
        raise TypeError

    with open("participants.json", "w") as outfile:
        json.dump(d, outfile, default=set_default, indent=2)


def BMI():
    df2 = pd.read_json("participants.json")
    df2 = df2.T
    df2["BMI"] = df2.weight / ((df2.height / 100) ** 2)
    df2["Comment"] = ''
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    df2.loc[df2.BMI<18.5, 'Comment'] = "Underweight"
    df2.loc[df2.BMI.between(18.5, 24.999), 'Comment'] = "Correct weight"
    df2.loc[df2.BMI.between(25, 29.999), 'Comment'] = "Overweight"
    df2.loc[df2.BMI.between(30,60), 'Comment'] = "Clinical obesity"
    df1 = pd.read_csv("participants.csv", engine='python')
    df2["Gender"] = df1["Gender"].values
    df2["Voivodeship"] = df1["Voivodeship"].values
    df2["Age"] = df1["Age"].values
    print("\n")
    print(df2)
    df2_m = df2.loc[df2["Gender"].str.contains("M")]
    df2_w = df2.loc[df2["Gender"].str.contains("W")]
    plt.style.use('fivethirtyeight')
    return df2, df2_m, df2_w


def histograms(df2, df2_m, df2_w):
    # #Histogram for men
    BMI_m = plt.hist(df2_m.BMI, edgecolor="black")
    plt.legend()
    plt.title('BMI Histogram For Men')
    plt.xlabel("BMI")
    plt.ylabel("Number of people")
    plt.tight_layout()
    plt.savefig("Histogram1.png")
    plt.show()

    # Histogram for women
    BMI_w = plt.hist(df2_w.BMI, edgecolor="black")
    plt.legend()
    plt.title('BMI Histogram For Women')
    plt.xlabel("BMI")
    plt.ylabel("Number of people")
    plt.tight_layout()
    plt.savefig("Histogram2.png")
    plt.show()

    df2_m1 = df2.loc[(df2["Gender"].str.contains("M")) & (df2["Age"].between(18, 35))]
    df2_w1 = df2.loc[(df2["Gender"].str.contains("W")) & (df2["Age"].between(18, 35))]
    BMI_mw1 = plt.hist(df2_w1.BMI, edgecolor="blue", bins=5, color="red", alpha=0.5, label="Women")
    BMI_mw1 = plt.hist(df2_m1.BMI, edgecolor="red", bins=5, color="blue", alpha=0.5, label="Men")
    plt.legend(loc='upper right')
    plt.title('BMI histogram for m & w aged 18-35')
    plt.xlabel("BMI")
    plt.ylabel("Number of people")
    plt.tight_layout()
    plt.savefig("Histogram3.png")
    plt.show()

    df2_m2 = df2.loc[(df2["Gender"].str.contains("M")) & (df2["Age"].between(46, 65))]
    df2_w2 = df2.loc[(df2["Gender"].str.contains("W")) & (df2["Age"].between(46, 65))]
    BMI_mk2 = plt.hist(df2_w2.BMI, edgecolor="blue", bins=5, color="red", alpha=0.5, label="Women")
    BMI_mk2 = plt.hist(df2_m2.BMI, edgecolor="red", bins=5, color="blue", alpha=0.5, label="Men")
    plt.legend(loc='upper right')
    plt.title('BMI histogram for m & w aged 46-65')
    plt.xlabel("BMI")
    plt.ylabel("Number of people")
    plt.tight_layout()
    plt.savefig("Histogram4.png")
    plt.show()

    df2_m3 = df2.loc[(df2["Gender"].str.contains("M")) & (df2["Age"].between(66, 80))]
    df2_w3 = df2.loc[(df2["Gender"].str.contains("W")) & (df2["Age"].between(46, 80))]
    BMI_mk3 = plt.hist(df2_w3.BMI, edgecolor="blue", bins=5, color="red", alpha=0.5, label="Women")
    BMI_mk3 = plt.hist(df2_m3.BMI, edgecolor="red", bins=5, color="blue", alpha=0.5, label="Men")
    plt.legend(loc='upper right')
    plt.title('BMI histogram for m & w aged 66-80')
    plt.xlabel("BMI")
    plt.ylabel("liczba osób")
    plt.tight_layout()
    plt.savefig("Histogram5.png")
    plt.show()

    # Group average by voivodeship

    w_m = df2_m.groupby("Voivodeship")["BMI"].mean()
    w_w = df2_w.groupby("Voivodeship")["BMI"].mean()
    # print(f"Avg for men in particular voivodeship:\n{w_m}\n\n")
    # print(f"Avg for women in particular voivodeship:\n{w_w}")

    w_m.plot(kind='bar', title="Men", x='BMI', y='Voivodeship')
    plt.subplots_adjust(bottom=0.44)
    plt.savefig("Histogram6.png")
    plt.show()

    w_w.plot(kind='bar', title="Women", x='BMI', y='Voivodeship')
    plt.subplots_adjust(bottom=0.44)
    plt.savefig("Histogram7.png")
    plt.show()

    print("\n\n")
    s1 = (f"The highest BMI in the group of men is: {df2_m.BMI.max()}")
    s2 = (f"The highest BMI in the group of women is: {df2_w.BMI.max()}")
    s3 = (f"The average BMI in the group of men is: {df2_m.BMI.mean()}")
    s4 = (f"The average BMI in the group of women is: {df2_w.BMI.mean()}")
    s5 = (f"The lowest BMI in the group of men is: {df2_m.BMI.min()}")
    s6 = (f"The lowest BMI in the group of women is: {df2_w.BMI.min()}")
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print("\n\n")


def html_to_pdf(df2):
    try:
        print("Creating a summary in pdf..")
        html = df2.to_html("Summary.html")
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        pdfkit.from_file("Summary.html", "Summary.pdf", configuration=config, options=options)
    except:
        print("Something went wrong... Install program wkhtmltopdf "
              "and check if the path_wkhtmltopdf variable leads to it")


choice()
df2, df2_m, df2_w = BMI()
histograms(df2, df2_m, df2_w)
html_to_pdf(df2)
