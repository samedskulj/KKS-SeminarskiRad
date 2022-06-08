from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait


def test_show_no_items_page(signin_func):
    my_items_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"My items")]')))
    my_items_link.click()
    wait.until(EC.invisibility_of_element((By.XPATH, '//a[contains(.,"My items")]')))
    try:
        no_items = wait.until(EC.presence_of_element_located((By.XPATH, '//h3[contains(.,"No saved items yet")]')))
        found = True
    except:
        found = False

    assert found


def test_save_items_and_show(signin_func):
    jobs_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Jobs")]')))
    jobs_link.click()
    single_job = wait.until(EC.presence_of_element_located((By.XPATH, "//button[starts-with(@aria-label, 'Save job')]")))
    single_job.click()
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Save")]')))
    save_button.click()
    home_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Home")]')))
    home_link.click()
    my_items_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"My items")]')))
    my_items_link.click()
    try:
        all_saved_jobs = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(., "Saved")]')))
        found = True
    except:
        found = False

    assert found


def test_search_items(signin_func):
    search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Search"]')))
    search_input.click()
    search_input.send_keys("Samed Škulj")
    search_input.send_keys(Keys.ENTER)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(., "Samed Škulj")]')))
        found = True
    except:
        found = False

    assert found
