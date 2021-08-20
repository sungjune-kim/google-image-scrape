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
    
    def activate(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        
        search = driver.find_element_by_name("q")
        search.send_keys(self.searchword)
        search.send_keys(Keys.RETURN)
        
        try:
            driver.execute_script("window.scrollTo(0,8000)")
            images = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[class='rg_i Q4LuWd']")))
            images = [image.get_attribute('src') for image in images]    
            print(f"scraped {len(images)} images")
            
        finally:
            driver.quit()
        
        return images