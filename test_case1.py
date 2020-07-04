import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

true_name = "Natalia"
true_surname = "Zalucka"
true_phone_number = "730784030"
true_email = "natalia.zalucka4@gmail.com"
true_password = "projektWSB1"

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def testRegistration(self):
        driver = self.driver
        # 1. Kliknij "Zaloguj się"
        zaloguj_btn = WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        # 2. Kliknij "Rejestracja"
        rejestracja_btn = WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]')))
        rejestracja_btn.click()
        # 3. Wprowadź imię
        name_field = WebDriverWait(driver, 60)\
        .until(EC.presence_of_element_located((By.NAME, 'firstName')))
        name_field.send_keys("Natalia")
        # 4. Wprowadź nazwisko
        surname_field=driver.find_element_by_name('lastName')
        surname_field.send_keys("Zalucka")
        # 5. Wybierz płeć
        gender=driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]') # Kobieta
        gender.click()
        # 6. Wpisz kod kraju
        country_code=driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        country_code.click()
        country_code_input=driver.find_element_by_name('phone-number-country-code')
        country_code_input.send_keys("+48")
        country_code_input.send_keys(Keys.RETURN)
        # 7. Wpisz prawidlowy numer telefonu
        phone=driver.find_element_by_name('phoneNumberValidDigits')
        phone.send_keys("730784030")
        # 8. Wpisz e-mail
        email=driver.find_element_by_name('email')
        email.send_keys('natalia.zalucka4@gmail.com')
        # 9. Wpisz hasło
        password=driver.find_element_by_css_selector('input[data-test="booking-register-password"]')
        password.send_keys('projektWSB1')
        # 10. Wybierz kraj
        country=driver.find_element_by_name('country-select')
        country.click()
        country.send_keys("Polska")
        country.send_keys(Keys.RETURN)
        # 11. Zaakceptuj politykę prywatności
        pp=driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        pp.click()
        # 12. Kliknij Zarejestruj się
        driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]').click()

        sleep(25)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=1)
