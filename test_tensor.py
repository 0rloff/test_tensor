from pages.PageClass import Search
import time


def test_yandex_search(browser):
    link = 'https://yandex.ru/'
    yandex_page = Search(browser, link)
    yandex_page.open_site()
    yandex_page.is_search_field_here()
    yandex_page.enter_word("тензор")
    yandex_page.suggest_popup()
    time.sleep(2)
    yandex_page.press_enter()
    time.sleep(5)

#    elements = yandex_page.check_navigation_bar()
#    assert "Картинки" and "Видео" in elements
