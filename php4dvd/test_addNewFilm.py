# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class  AddNewFilm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
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

#   добавления нового фильма
        driver.find_element_by_xpath("//*[@id='content']/section/nav/ul/li[1]/div/div/a").click() # клик на
        # кнопку "Add movie"
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.addmovie > h2"): break # дожидаемся доступа к полям
                # для заполнениея информации о новом фильме
            except: pass
            time.sleep(1)
        else: self.fail("time out")

#   заполнение информации о новом фильме
        driver.find_element_by_xpath("//*[@id='imdbsearch']").clear()
        driver.find_element_by_xpath("//*[@id='imdbsearch']").send_keys("My")
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[2]/td[2]/input").clear()
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[2]/td[2]/input").send_keys("1 My favorite film")
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[4]/td[2]/input").clear()
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[4]/td[2]/input").send_keys("2013")
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[3]/td[2]/textarea").clear()
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[3]/td[2]/textarea").send_keys(u"описание фильма")
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[5]/td[2]/input").clear()
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[5]/td[2]/input").send_keys("1000")
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[6]/td[2]/input").clear()
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[6]/td[2]/input").send_keys("1000")
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_id("seen_no").click()
        driver.find_element_by_id("submit").click() # click по кнопке "Save"

        for i in range(60):
            try:
                if self.is_element_present(By.ID, "movie"): break # ожидаем появления элемента на основной странице
            except: pass
            time.sleep(1)
        else: self.fail("time out")

# logout выхода из приложения

        driver.find_element_by_xpath("//*[@id='wrapper']/header/div/nav/ul/li[last()]/a").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^[\s\S]*$")
        for i in range(60):
            try:
                if self.is_element_present(By.NAME, "submit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")


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