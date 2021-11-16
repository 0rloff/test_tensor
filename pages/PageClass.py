from .BaseClass import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Search(BasePage):

    # Проверка наличия поля поиска
    def is_search_field_here(self):
        self.field = self.browser.find_elements(By.ID, 'text')
        assert len(self.field) > 0, 'Строка поиска не найдена'

    # Ввод запроса
    def enter_word(self, word):
        search_panel = self.browser.find_element(By.ID, 'text')
        search_panel.click()
        search_panel.send_keys(word)

    # Проверка появления попапа с подсказкой
    def suggest_popup(self):
        self.popup = self.browser.find_elements(By.CSS_SELECTOR, 'div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')
        assert len(self.popup) > 0, 'Попап с подсказками не появляется'

    # Жмем Enter
    def press_enter(self):
        self.press_key = self.browser.find_element(By.ID, 'text')
        self.press_key.send_keys(Keys.ENTER)

    # Проверка наличия нужного сайта в топ 5 выдачи
    def search_result(self):
        self.n = 5
        self.result = ''
        for i in range(self.n):
            result = self.browser.find_element(By.XPATH, f'//li[@data-cid="{i}"]')
            if 'tensor.ru' in (result.get_attribute('innerHTML')):
                break
        assert 'tensor.ru' in result.get_attribute('innerHTML'), 'Сайта "tensor.ru" нет в выдаче'

