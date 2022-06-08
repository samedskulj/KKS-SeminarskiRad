import time

import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
#Bluetooth fix - warning i error
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 })
#Path i driver je moguće i lokalno podesiti
s = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
wait = WebDriverWait(driver, timeout=60)
#Const varijabla - lakše napraviti promjenu ubuduće na drugu web aplikaciju
LINKEDIN = "https://www.linkedin.com"

@pytest.fixture
def signin_func():
    global driver
    global wait
    driver.get(LINKEDIN)
    driver.maximize_window()
    #Provjera ako je korisnik već ulogovan da nema potrebe za tim procesom opet - Selenium User Agent problem sa Linkedin-om - quick fix
    if driver.current_url != "https://www.linkedin.com/feed/":
        input_email = wait.until(EC.element_to_be_clickable((By.ID, "session_key")))
        input_password = wait.until(EC.element_to_be_clickable((By.ID, "session_password")))
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Sign in")]')))
        #testni profil
        input_email.send_keys("kontrolakvalitete@outlook.com")
        input_password.send_keys("ptfunze2022")
        sign_in_button.click()
        wait.until(EC.invisibility_of_element((By.ID, "session_key")))
        wait.until(EC.invisibility_of_element((By.ID, "session_password")))
        yield driver
    else:
        yield driver

@pytest.fixture
def set_up():
    global driver
    driver.maximize_window()
    driver.get(LINKEDIN)
    return driver
