from .BaseClass import BasePage
from .ImagesLocators import PicturesLocators


class Pictures(BasePage):

    # Проверка наличия ссылки на Яндекс.Картинки
    def is_pic_button_here(self):
        assert self.is_element_present(*PicturesLocators.PICTURES_BUTTON), 'Ссылка "Картинки" не найдена'

    # Переход в Яндекс.Картинки и проверка загрузки страницы
    def open_pictures_search_page(self):
        self.pic_button = self.browser.find_element(*PicturesLocators.PICTURES_BUTTON)
        self.pic_button.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert 'https://yandex.ru/images/' in self.browser.current_url, 'Загружена неверная страница'

    # Переход в первую категорию популярных запросов и проверка соответствия выдачи
    def select_first_category(self):
        self.first_cat = self.browser.find_element(*PicturesLocators.FIRST_CATEGORY)
        self.first_cat_text = self.first_cat.get_attribute("data-grid-text")
        self.first_cat.click()
        assert self.first_cat_text in self.browser.find_element(*PicturesLocators.FIRST_CAT_RESULT).get_attribute('value'), \
            'Выдача поиска не соответствует запросу по первой категории'

    # Открытие первого изображения
    def select_first_picture(self):
        self.image = self.browser.find_element(*PicturesLocators.FIRST_IMAGE_ICON)
        self.image.click()

    # Переход к следующему изображению
    def switch_image(self):
        self.next_button = self.browser.find_element(*PicturesLocators.NEXT_BUTTON)
        self.prev_button = self.browser.find_element(*PicturesLocators.PREV_BUTTON)
        self.start_image_url = self.browser.find_element(*PicturesLocators.IMAGE_ORIGIN).get_attribute('src')
        self.next_button.click()
        self.next_image_url = self.browser.find_element(*PicturesLocators.IMAGE_ORIGIN).get_attribute('src')
        self.prev_button.click()
        self.prev_image_url = self.browser.find_element(*PicturesLocators.IMAGE_ORIGIN).get_attribute('src')
        assert self.start_image_url != self.next_image_url and self.start_image_url == self.prev_image_url, 'Ошибка перехода'

