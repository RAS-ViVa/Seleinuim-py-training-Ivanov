# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_removeFilm(self):
#   вход с правами admin
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_xpath("//form[@id='loginform']//tr/td[2]/input").clear()
        driver.find_element_by_xpath("//form[@id='loginform']//tr/td[2]/input").send_keys("admin")
        driver.find_element_by_xpath("//form[@id='loginform']//tr[2]/td[2]/input").clear()
        driver.find_element_by_xpath("//form[@id='loginform']//tr[2]/td[2]/input").send_keys("admin")
        driver.find_element_by_xpath("//form[@id='loginform']//tr[3]/td[2]/input").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "results"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

# очищаем поле фильтра для поиска фильмов
        text_Search = '' #name_Film.get_attribute('title')
        driver.find_element_by_xpath("//*[@id='q']").clear()
        driver.find_element_by_xpath("//*[@id='q']").send_keys(text_Search)
        driver.find_element_by_id("q").send_keys(Keys.ENTER)

# запоминаем общее количество фильмов в коллекции
        print(driver.find_elements_by_class_name("movie_cover"))
        allFilms = []
        allFilms = driver.find_elements_by_class_name("movie_cover")
        sumFilms = len(allFilms)
#        print(sumFilms)

# удаляем первый в списке фильм
        driver.find_element_by_class_name("movie_cover").click()
        driver.find_element_by_xpath("/html/body/div/div/div/section/nav/ul/li[4]/div/div/a/img").click()
        self.assertTrue(self.is_alert_present())
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "results"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

# определяем что общее кол-во фильмов коллекции после удаления умешьшилось на 1
        allFilmsNew = driver.find_elements_by_class_name("movie_cover")
        sumFilmsNew = len(allFilmsNew)
#        print(sumFilmsNew)
#        print(sumFilms - sumFilmsNew)
        r = sumFilms - sumFilmsNew - 1
        r = 0


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
