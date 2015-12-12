from selenium.webdriver import ActionChains
from base_component import BaseComponent



class FiltersScroller(BaseComponent):

    selectors = {
        'self': 'frame__content',
        'has_site': "//label[@class='checkbox' and @title='Есть сайт']",
        'has_photo': "//label[@class='checkbox' and @title='Есть фото']",
        'has_card': "//label[@class='checkbox' and @title='Расчет по картам']",
        'work_all_time': "//label[@class='radiogroup__label'][2]",
        'work_select_time': "//label[@class='radiogroup__label'][3]",
        'Пн': "//div[@class='radiogroup _week']/label[1]",
        'Вт': "//div[@class='radiogroup _week']/label[2]",
        'Ср': "//div[@class='radiogroup _week']/label[3]",
        'Чт': "//div[@class='radiogroup _week']/label[4]",
        'Пт': "//div[@class='radiogroup _week']/label[5]",
        'Сб': "//div[@class='radiogroup _week']/label[6]",
        'Вс': "//div[@class='radiogroup _week']/label[7]",
        'filter_time': 'filters__raderRunner',
        'filters__time_In': 'filters__raderRunnerIn',


    }

    def slide_move(self, hour):

        """
         :param hour:  час, на который нужно передвинуть слайдер\n"
         :return: значение в px, на которое нужно сдвинуть слайдер\n"
         340 - ширина слайдера\n"
        """
        
        position = self.driver.find_element_by_class_name(self.selectors['filter_time']).get_attribute('style')
        length = len(position)
        position = float(position[6:length - 2])
        return 340 * (hour / 24 - position / 100)

    def check_filter(self, tip):
        filter_name = self.driver.find_element_by_xpath(self.selectors[tip])
        if not filter_name.is_selected():
            filter_name.click()

    def select_day(self, day):
        self.driver.find_element_by_xpath(self.selectors[day]).click()

    def select_hour(self, hour):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element_by_class_name(self.selectors['filters__time_In']),
                                       self.slide_move(hour), 0).perform()