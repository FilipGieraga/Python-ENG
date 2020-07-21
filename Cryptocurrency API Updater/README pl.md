# Rozszerzenie programu Cryptocurrency API, które pozwala odpalając skrypt zaktualizować ceny w pliku CryptoPortfolio.xlsx

Requirements: Python 3, os module, pandas module, json module, requests module, requests.exceptions module, xlwings module

# Program:
1. szuka pliku CryptoPortfolio.xlsx i sprawdza czy takowy istnieje w ścieżce w której znajduje się program
2. sprawdza kolumnę nazwa, żeby znaleźć monety jakie posiadamy w naszym portfelu
3. aktualizuje wartości takie jak cena i procentowe zmiany
4. na podstawie tych zmian zmieniają się również wartości takie jak total, value oraz wygląd wykresu


# Ważne:
Program pozwala nam nanieść zmiany w pliku excel i dopiero po tym odpalić skrypt.
Załóżmy że do naszego portfela chcemy dodać nową monetę i zmienić ilość istniejącej już monety.<br>
Aby zmienić ilość monety wystarczy w odpowiadającej ilości komórce zmienić liczbę.<br>
Aby dodać nową monetę proces polega na rozszerzeniu formuł w naszym pliku, musimy przesunąć Total i odpowiadającą mu wartość w dół o jeden w tym wypadku.
W ten sposób tworzy nam się nowy pusty rząd, w którym musimy wypełnić trzy komórki Name, Short name i ilość.<br>
Musimy zaktualizować formuły dla nowo powstałej monety poprzez:<br>
przeciągnięcie formuły values o jedną w dół<br>
przeciągnięcie formuły total dla naszej sumy o jedną w dół<br>
kliknięcię na wykres kołowy oraz przęciagnięcie go o jedną komórkę w dół dla short name i value<br>
użycie malarza formatów dla procentowych zmian<br>

## The data is pulled from coinmarketcap.com using my private api key

