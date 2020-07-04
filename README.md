# Automatyzacja z Selenium

Automatyzacja przypadku testowego przy pomocy Selenium Webdriver.
Projekt zaliczeniowy


1. sprawdzamy wersje pip3

   ```
   $ pip3 --version
   ```
2. przypadku braku tej wersi nalezy ja zainstalowac

  ```
  $ sudo apt install python3-pip
  ```
3. Instalacja Selenium

  ```
  $ pip3 install selenium
  ```

4. Instalacja sterownika przegladarki niezbednego do wspolpracy z selenium.
w tym przypadku chromedriver, poniewaz korzystamy z przegladarki Chrome
  ```
  https://sites.google.com/a/chromium.org/chromedriver/downloads
  ```
5. po pobraniu archiwum rozpakowujemy je
  ```
  $ unzip chromedriver_linux64.zip
  ```
6. nastepnie przenosimy do katalogu /usr/local/bin

  ```
  $ mv gchromedriver /usr/local/bin
  ```
7. przechodzimy do naszych przypadkow testowych (tam, gdzie je stworzylismy)

  ```
  $ cd Documents
  ```
8. uruchamiamy przypadki testowego

  ```
  $ python3 test_case1.py
  $ python3 test_case2.py
  ```
