from internal_page import InternalPage
from php4dvd.pages.blocks.user_form import UserForm
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class InfoFilmPage(InternalPage):

    def __init__(self, driver, base_url):
        super(InfoFilmPage, self).__init__(driver, base_url)
        self.user_form = UserForm(self.driver, self.base_url)

    @property
    def button_del_film(self):
        return self.driver.find_element_by_xpath("/html/body/div/div/div/section/nav/ul/li[4]/div/div/a/img")

    @property
    def home_button(self):
        return self.driver.find_element_by_link_text("Home")