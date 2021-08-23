#!/usr/bin/env python
# coding: utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ConfigLoader import config_driver, config_save

class ImageScraper:
    def __init__(self, searchword):
        self.PATH = config_driver['PATH']
        self.URL = config_driver['URL']
        self. searchword = searchword
        self.image_list = []
    
    def activate(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        
        search = driver.find_element_by_name("q")
        search.send_keys(self.searchword)
        search.send_keys(Keys.RETURN)
        
        try:
            main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"islrc")))
            items = main.find_elements_by_class_name("bRMDJf islir")
            imgs = [item.get_attribute('src') for item in items]
            
        finally:
            driver.quit()
        
        return imgs