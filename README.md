Automatyzacja przypadku testowego przy pomocy Selenium Webdriver.
Projekt zaliczeniowy


#sprawdzamy wersje pip3
$ pip3 --version
#w przypadku braku tej wersi nalezy ja zainstalowac
$ sudo apt install python3-pip

#Instalacja Selenium
$ pip3 install selenium

#Instalacja sterownika przegladarki niezbednego do wspolpracy z selenium.
w tym przypadku chromedriver, poniewaz korzystamy z przegladarki Chrome
https://sites.google.com/a/chromium.org/chromedriver/downloads

#po pobraniu archiwum rozpakowujemy je
$ unzip chromedriver_linux64.zip

#nastepnie przenosimy do katalogu /usr/local/bin
$ mv gchromedriver /usr/local/bin

#przechodzimy do naszych przypadkow testowych (tam, gdzie je stworzylismy)
$ cd Documents

#uruchamiamy przypadki testowego
$ python3 test_case1.py
$ python3 test_case2.py
