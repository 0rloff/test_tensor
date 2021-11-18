from pages.SearchClass import Search
from pages.ImagesClass import Pictures


def test_yandex_search(browser):
    link = 'https://yandex.ru/'
    yandex_page = Search(browser, link)
    yandex_page.open_site()
    yandex_page.is_search_field_here()
    yandex_page.enter_word("тензор")
    yandex_page.suggest_popup()
    yandex_page.press_enter()


def test_yandex_pictures(browser):
    link = 'https://yandex.ru/'
    yandex_page = Pictures(browser, link)
    yandex_page.open_site()
    yandex_page.is_pic_button_here()
    yandex_page.open_pictures_search_page()
    yandex_page.select_first_category()
    yandex_page.select_first_picture()
    yandex_page.switch_image()