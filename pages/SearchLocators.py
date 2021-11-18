from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_FIELD = (By.ID, 'text')
    POPUP = (By.CSS_SELECTOR, 'div.mini-suggest__popup.mini-suggest__popup_svg_yes')
    IS_IN_TOP5 = (By.XPATH, '//b[text()="tensor.ru"]')

