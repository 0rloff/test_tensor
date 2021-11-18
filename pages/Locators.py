from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_FIELD = (By.ID, 'text')
    POPUP = (By.CSS_SELECTOR, 'div.mini-suggest__popup.mini-suggest__popup_svg_yes')
    IS_IN_TOP5 = (By.XPATH, '//b[text()="tensor.ru"]')


class PicturesLocators:
    PICTURES_BUTTON = (By.CSS_SELECTOR, '[data-id = images]')
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0')
    FIRST_CAT_RESULT = (By.CSS_SELECTOR, 'input.input__control')
    FIRST_IMAGE_ICON = (By.CSS_SELECTOR, '.serp-item_pos_0')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next i.CircleButton-Icon')
    PREV_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev i.CircleButton-Icon')
    IMAGE_ORIGIN = (By.CSS_SELECTOR, 'img.MMImage-Origin')
