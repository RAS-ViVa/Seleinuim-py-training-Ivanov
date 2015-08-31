from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from php4dvd.pages.add_film_page import AddFilmPage
from php4dvd.pages.info_film_page import InfoFilmPage
from php4dvd.pages.inf_film_page import InfFilmPage
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#import Selenium2Library
import time

from selenium import webdriver



class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.add_film_page = AddFilmPage(driver, base_url)
        self.inf_film_page = InfFilmPage(driver, base_url)
        self.info_film_page = InfoFilmPage(driver, base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        element.tag_name == "nav"
        self.logout()

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def is_logged_in(self):
        return self.login_page.is_this_page

    def is_not_logged_in(self):
        return self.internal_page.is_this_page

    def add_new_film(self,film):
        self.internal_page.add_film_link.click()
        afp = self.add_film_page
        afp.is_this_page
        afp.name_field.clear()
        afp.name_field.send_keys(film.name)
        afp.year_field.clear()
        afp.year_field.send_keys(film.year)
        afp.duration_field.clear()
        afp.duration_field.send_keys(film.duration)
        afp.rating_field.clear()
        afp.rating_field.send_keys(film.rating)
        afp.submit_button.click()

        for i in range(60):
            try:
                if self.info_film_page.button_del_film: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        self.info_film_page.home_button.click()
 #       self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^[\s\S]*$")
        for i in range(60):
            try:
                if self.internal_page.name_first_Film: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")




#        for i in range(900):
#            i=i+1
#        else: pass# self.fail("time out")

        #self.fail("time out")

#        self.info_film_page.home_button.click()
#        for i in range(2000):
#            i=i+1
#        else: pass #self.fail("time out")


    def remove_film(self):
        self.internal_page.remove_film_link.click()
        rf = self.inf_film_page
        rf.is_this_page
#        rf.is_this_page
        rf.button_del_film.click()
        self.wait.until(alert_is_present()).accept()
        for i in range(60):
            try:
                if self.login_page.is_this_page: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")



#    def name_first_film(self):
#        return self.internal_page.find_element_by_xpath("/html/body/div[1]/div/div/section/div[3]/a[1]/div/div[1]/div")

    def sum_films_collection(self):
        return len(self.internal_page.is_films_collection)

    def clear_search_field (self):
        self.internal_page.search_field.clear()
        self.internal_page.search_field.send_keys('')
        self.internal_page.search_field.send_keys(Keys.ENTER)
        for i in range(1000):
            t=i+1
        else: pass


    def command_Enter(self):
        self.find_element_by_id("q").send_keys(Keys.ENTER)
        for i in range(1000):
            t=i+1
        else: pass


    def search_film(self, wich_FilmSearch):
        print (self.current_url)
        self.internal_page.search_field.clear()
        self.internal_page.search_field.send_keys(wich_FilmSearch)
        self.internal_page.search_field.send_keys(Keys.ENTER)

        print (self.current_url)

        for i in range(60):
            try:
                if str(self.current_url).find('/search/') > 0:break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        print (self.current_url)


#    @property
    def film_name(self):
        return self.internal_page.film_name1.get_attribute("title")

    def current2_url(self):
        return self
