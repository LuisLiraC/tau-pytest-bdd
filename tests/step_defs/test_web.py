import pytest

from pytest_bdd import scenarios, when, then, parsers
# from pytest_bdd import given
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
# GOOGLE_HOME = 'https://google.com'

# Scenarios
scenarios('../features/web.feature')

# Fixtures
# @pytest.fixture
# def browser():
#     b = webdriver.Chrome()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()


# # Given Steps
# @given('the Google home page is displayed')
# def gooogle_home(browser):
#     browser.get(GOOGLE_HOME)


# When steps
@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase: "{text}"'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)

# Then Steps


@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//*[@id='rso']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0


@then(parsers.parse('results are shown for "{phrase}"'))
def search_result(browser, phrase):
    links_div = browser.find_element_by_id('rso')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
