import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome(executable_path='C:/Users/Антон/PycharmProjects/test_tensor/chromedriver.exe')
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
