# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random


from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By
import unittest, time, re, random


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_link_text("Log out")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "loginform"))

    @property
    def add_film_link(self):
        return self.driver.find_element_by_xpath("//*[@id='content']/section/nav/ul/li[1]/div/div/a")# !!!!
#        return self.driver.find_element_by_css_selector("nav a[href='./?go=add']")

    @property
    def is_films_collection(self):
        return self.driver.find_elements_by_class_name("movie_cover")

    @property
    def remove_film_link(self):
        return self.driver.find_element_by_class_name("movie_cover")

    @property
    def search_field(self):
        return self.driver.find_element_by_xpath("//*[@id='q']")

    @property
    def name_first_Film(self):
        return self.driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[3]/a[1]/div/div[1]/div")

    @property
    def film_name1(self):
        return self.driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[3]/a[1]/div/div[1]/div")

#    @property
#    def current1_url(self):
#        return self.base_url