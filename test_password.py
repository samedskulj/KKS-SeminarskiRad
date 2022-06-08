from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait


def test_show_password_hidden(set_up):
    input_password = wait.until(EC.element_to_be_clickable((By.ID, 'session_password')))
    show_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sign-in-form__password-visibility-toggle-button")))
    input_password.send_keys("test")
    show_button.click()
    assert show_button.text == "Hide"
    assert input_password.get_attribute("type") == "text"
