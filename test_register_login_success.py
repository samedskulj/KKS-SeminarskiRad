from conftest import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login_success(set_up):
    try:
        input_email = wait.until(EC.element_to_be_clickable((By.ID, "session_key")))
        input_password = wait.until(EC.element_to_be_clickable((By.ID, "session_password")))
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Sign in")]')))
        input_email.send_keys("kontrolakvalitete@outlook.com")
        input_password.send_keys("ptfunze2022")
        sign_in_button.click()
        wait.until(EC.invisibility_of_element((By.ID, "session_key")))
        wait.until(EC.invisibility_of_element((By.ID, "session_password")))
        loggedin = True
    except:
        loggedin = False
    assert loggedin