from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait
import pytest


def test_event_modal_open(signin_func):
    #ID se dinamički mjenja zbog Embera pa je zbog toga aria-label jedini validan elemenat pored class
    event_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Create an event"]')))
    event_button.click()
    event_modal_heading = wait.until(EC.presence_of_element_located((By.ID, "-header")))
    assert event_modal_heading.text == "Create an event"

def test_search_messages_error(signin_func):
    search_input = wait.until(EC.presence_of_element_located((By.ID, "msg-overlay-list-bubble-search__search-typeahead-input")))
    search_input.click()
    search_input.send_keys("test")
    error_message = wait.until(EC.presence_of_element_located((By.XPATH, '//p[contains(., "We didn’t find anything with “test”")]')))
    assert error_message.text == "We didn’t find anything with “test”"

def test_news_article_open(signin_func):
    news_article_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Write an article on LinkedIn"]')))
    news_article_button.click()
    wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, '[aria-label="Write an article on LinkedIn"]')))
    try:
        text_to_write = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-placeholder="Write here. Add images or a video for visual impact."]')))
        found = True
    except:
        found = False
    assert found
