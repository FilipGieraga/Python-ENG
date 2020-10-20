# Filmweb Scraper:

Requirements: Python 3, selenium, xlsxwriter

## Documentation:
This program allows you to scrape the biggest polish website with movies and output it to excel spreadsheet.
You can also pass some parameters to functions and change the final output.
There are two functions which are scrape() and excel_file().
Scrape takes two parametrs that have default values. First is number of pages and second is url.
Website is dynamic and it needs scrolling to load. The amount of scrolls needed really depends on
your computer performance and internet speed. For me 150(which is default) to scroll 500 movies was even more than enough.
Default URL takes you to Top Ranking containing 500 movies of different kind, but you can change the filters if you want
to be more specific. There are 3 filters:
Genre(like comedy, or thriller)
Year
Country where the movie was made
If you want to scrape filtered data you need to go to the website directly, set the filters and paste given url to the function, because
default url is for top 500.
Please note that this program opens the chrome browser without any extentions and once it does,
you need to close the pop ups that show so it can start automatically scrolling.
Example below scrapes best horrors of 2020 and needs only 15 scrolls to finish.<br><br>

container = scraper(url="https://www.filmweb.pl/ranking/film/Horror/12/2020",no_of_pagedowns=15)<br><br>

Once the scraping is done, function returns dictionary of records and pass it to excel_file().
Here you can only specify the name of the file. It also takes dictionary "container" and this can't be changed.
The output is excel file that looks like this:<br>
![alt tag](https://github.com/FilipGieraga/Python-ENG/blob/master/19.%20Filmweb_Scraper/scraper.PNG)

## IMPORTANT
Since it's Selenium you need to have chromedriver.exe on your computer and specify the path to it in variable path.<br>
It doesn't need installation.
You can find and download this here: https://chromedriver.chromium.org/

