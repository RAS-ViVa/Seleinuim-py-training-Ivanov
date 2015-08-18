from internal_page import InternalPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class InfFilmPage(InternalPage):

    @property
    def button_del_film(self):
        return self.driver.find_element_by_xpath("/html/body/div/div/div/section/nav/ul/li[4]/div/div/a/img")