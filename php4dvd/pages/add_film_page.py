from internal_page import InternalPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class AddFilmPage(InternalPage):

    @property
    def name_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def duration_field(self):
        return self.driver.find_element_by_name("duration")

    @property
    def rating_field(self):
        return self.driver.find_element_by_name("rating")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("submit")

#    @property
#    def is_this_page(self):
#        return self.is_element_present(By.CSS_SELECTOR, "div.addmovie > h2")

    @property
    def button_del_film(self):
        return self.driver.find_element_by_xpath("/html/body/div/div/div/section/nav/ul/li[4]/div/div/a/img")

