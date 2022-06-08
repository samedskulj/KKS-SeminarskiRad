from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait




def test_login_error(set_up):
    input_email = wait.until(EC.element_to_be_clickable((By.ID, "session_key")))
    input_password = wait.until(EC.element_to_be_clickable((By.ID, "session_password")))
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Sign in")]')))
    input_email.send_keys("test")
    input_password.send_keys("test2")
    sign_in_button.click()
    error_message = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "alert-content")))
    assert error_message.text == "Please enter a valid email address or mobile number."

def test_register_error(set_up):
    join_now_button = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(.,"Join now")]')))
    join_now_button.click()
    wait.until(EC.invisibility_of_element((By.XPATH, '//a[contains(.,"Join now")]')))
    join_form_submit = wait.until(EC.element_to_be_clickable((By.ID, "join-form-submit")))
    join_form_submit.click()

    try:
        email_register_error = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"Please enter your email address")]')))
        password_register_error = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//p[contains(.,"Please enter your password")]')))
        found = True
    except:
        found = False

    assert found


