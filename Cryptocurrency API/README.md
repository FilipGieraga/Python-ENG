# Program pozwala na stworzenie swojego własnego kryptoportfolio w excelu posiadającego aktualne ceny wraz z procenotwymi zmianami i wykresem kołowym

Wymagania: Python 3, requests module, requests.exceptions, json, xlsxwriter

# Program:
1. prosi użytkownika o wpisanie pełnych nazw kryptowalut np. bitcoin, xrp, cardano . Po każdej pojedynczej wpisanej kryptowalucie proszę dać enter.
2. wpisując end zatrzymujemy pętlę
3. jeśli coś pójdzie nie tak program nas o tym powiadomi
4. jeżeli wszystko jest okej, program prosi nas o podanie konkretnej ilości
posiadanej waluty jako liczby całkowitej(np. 5) albo dziesiętnej(np. 0.4)
5. na podstawie wprowadzonych danych tworzy plik CryptoPortfolio.xlsx
6. zapisuje plik w ścieżce programu
7. nasz excel posiada 6 kolumn "Name", "Short Name","Quantity","Price($)","Value($)","1H Change","24H Change","7D Change"
8. liczy nam również wartość całkowitą portfela na podstawie podanych ilości posiadanych kryptowalut
9. tworzy wykres kołowy ilustrujący wartość posiadanych kryptowalut

## Dane są zaciągane ze strony coinmarketcap.com za pomocą mojego prywatnego api klucza

