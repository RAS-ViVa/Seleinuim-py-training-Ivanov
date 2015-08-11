# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random

class Search_Film(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Search_Film(self):
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

#   очищаем поле фильтра для поиска фильмов
        text_Search = ''
        driver.find_element_by_xpath("//*[@id='q']").clear()
        driver.find_element_by_xpath("//*[@id='q']").send_keys(text_Search)
        driver.find_element_by_id("q").send_keys(Keys.ENTER)

#   ожидаем обновления информации с очищенным фильтром
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div[1]/div/div/section/div[3]/a[1]/div/div[1]/div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")#ожидаем обновления информации с очищенным фильтром

#   запоминаем общее количество фильмов в коллекции
        allFilms = []
        allFilms = driver.find_elements_by_class_name("movie_cover")
        sumAllFilms = len(allFilms)

#   находим и запоминаем имя первого фильма в списке
        name_Film = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[3]/a[1]/div/div[1]/div")

#   находим фильм по полному названию
        text_Search = name_Film.get_attribute('title')
        driver.find_element_by_xpath("//*[@id='q']").clear()
        driver.find_element_by_xpath("//*[@id='q']").send_keys(text_Search)
        driver.find_element_by_id("q").send_keys(Keys.ENTER)

#   ожидаем переход на страницу с результатами поиска
        for i in range(60):
            try:
                if str(driver.current_url).find('/search/') > 0:break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

#   проверяем, что что-то найдено, если нет тест завершается с ошибкой
        control=driver.find_element_by_class_name("movie_cover")

#   подсчитываем общее кол-во фильмов в базе с искомым названием (возможно, что в базе один и тот же
#   фильм повторяется несколько раз)
        searchFilms = []
        searchFilms = driver.find_elements_by_class_name("movie_cover")
        sumSearchFilms = len(searchFilms)

#   проверяем, что общее кол-во найденных фильмов меньше общего кол-ва фильмов в коллекции
        if sumAllFilms == sumSearchFilms: exit([1])

#   очищаем поле фильтра для поиска фильмов
        text_Search = ''
        driver.find_element_by_xpath("//*[@id='q']").clear()
        driver.find_element_by_xpath("//*[@id='q']").send_keys(text_Search)
        driver.find_element_by_id("q").send_keys(Keys.ENTER)


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
