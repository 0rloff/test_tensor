from .BaseClass import BasePage
from .SearchLocators import SearchLocators
from selenium.webdriver.common.keys import Keys


class Search(BasePage):

    # Проверка наличия поля поиска
    def is_search_field_here(self):
        assert self.is_element_present(*SearchLocators.SEARCH_FIELD), 'Строка поиска не найдена'

    # Ввод запроса
    def enter_word(self, word):
        search_panel = self.browser.find_element(*SearchLocators.SEARCH_FIELD)
        search_panel.click()
        search_panel.send_keys(word)

    # Проверка появления попапа с подсказкой
    def suggest_popup(self):
        assert self.is_element_present(*SearchLocators.POPUP), 'Попап с подсказками не появляется'

    # Жмем Enter
    def press_enter(self):
        self.press_key = self.browser.find_element(*SearchLocators.SEARCH_FIELD)
        self.press_key.send_keys(Keys.ENTER)

    # Проверка наличия нужного сайта в топ 5 выдачи
    def search_result(self):
        self.search_result = self.browser.find_elements(*SearchLocators.IS_IN_TOP5)
        self.test_result = ''
        for i in self.search_result[:5]:
            if 'tensor.ru' in i.text:
                self.test_result = i.text
                break
        assert 'tensor.ru' in self.test_result, 'Сайта "tensor.ru" нет в выдаче'

