# Program zapytania SQL pozwala nam wyświetlić wybrane informacj o sezonie 2018/2019 w lalidze.

Wymagania: Python 3, pandas module, pandasql module<br>

Na początek wczytane zostają dane z pliku laliga.csv.<br>

Funkcja sql_df() jest używana w funkcji queries() i pobiera treść każdego zapytania drukując nam przy tym jego rezultat.<br>
<br>
Zapytań łącznie jest 11 i każde jest opisane.
Niektóre zapytania pobierają od użytkownika informację jak np. jaką drużynę chce wyświetlić.
Aby ułatwić korzystanie z programu, gdy od użytkownika wymagane jest podanie pozycji albo drużyny,
są one wyświetlane i wystarczy je skopiować bez cudzysłowia.
<br><br>
Głównym trzonem programu jest funkcja queries(), która wyświetla jakie zapytania możemy wykonać.
Są one ponumerowane i wystarczy wpisać nr. zapytania i kliknąć enter.
Po każdym zapytaniu program czeka na wciśnięcie entera aby kontynuować.
Czasami niestety enter przenosi wiersz do nowej linijki a potem ponowny enter kończy program.
Aby temu zapobiec, jeśli program przeniesie nas do nowego wiersza, należy wcisnąć backspace i dopiero enter.
Aby zakończyć działanie programu wpisujemy end albo dowolny string przy wyborze zapytania.

