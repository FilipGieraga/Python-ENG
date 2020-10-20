import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlsxwriter

path = "C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(path)


def scraper(no_of_pagedowns=150, url="https://www.filmweb.pl/ranking/film"):
    browser.get(url)
    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.35)
        no_of_pagedowns -= 1

    movies_pl = browser.find_elements_by_class_name("rankingType__title")
    movies_eng = browser.find_elements_by_class_name("rankingType__originalTitle")
    ratings = browser.find_elements_by_class_name("rankingType__rate--value")
    number_of_ratings = browser.find_elements_by_class_name("rankingType__rate--count")

    container = {}
    i = 1
    for movie_pl, movie_eng, rate, number in zip(movies_pl, movies_eng, ratings, number_of_ratings):
        number = number.text
        if "oceny" in number:
            number = number.rstrip(" oceny")
        else:
            number = number.rstrip(" ocen")
        movie_pl = movie_pl.text
        movie_eng = movie_eng.text
        rate = rate.text
        container.update(
            {i: {"Movie PL": movie_pl, "Movie ANG": movie_eng, "Rating": rate, "Number of ratings": number}})
        i += 1
    browser.quit()
    return container


def excel_file(cotainer, file_name="Top_Movies_500"):
    workbook = xlsxwriter.Workbook(f'{file_name}.xlsx')
    worksheet = workbook.add_worksheet(name="Movies")
    cell_format = workbook.add_format({'bold': True})
    worksheet.freeze_panes(1, 0)
    headers = ["Movie PL Title", "Movie Eng Title", "Rating", "Number of Ratings"]
    row = 0
    col = 0
    for cell in headers:
        worksheet.write(row, col, cell, cell_format)
        col += 1

    row = 1
    col = 0

    for key, value in container.items():
        worksheet.write(row, col, value["Movie PL"])
        worksheet.write(row, col + 1, value["Movie ANG"])
        row += 1

    row = 1
    col = 2

    for key, value in container.items():
        number = value["Rating"].replace(",", ".")
        number = float(number)
        worksheet.write(row, col, number)
        worksheet.write(row, col + 1, value["Number of ratings"])
        row += 1

    worksheet.conditional_format('C2:C' + str(row) + '', {'type': 'data_bar', 'bar_color': '#F0CC10'})

    worksheet.set_column('A:A', 59.9)
    worksheet.set_column('B:B', 63.9)
    worksheet.set_column('C:C', 16.56)
    worksheet.set_column('D:D', 16)

    workbook.close()

container = scraper()

excel_file(container)


# container = scraper(url="https://www.filmweb.pl/ranking/film/Horror/12/2020",no_of_pagedowns=15)
#
# excel_file(container,file_name="Horrors_2020")