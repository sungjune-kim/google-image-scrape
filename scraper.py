#!/usr/bin/env python
# coding: utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ConfigLoader import config_driver, config_save
import os
import urllib.request

class ImageScraper:
    def __init__(self, path, foldername, searchword):
        self.PATH = config_driver['PATH']
        self.URL = config_driver['URL']
        self.searchword = searchword
        self.dir = path
        self.foldername = foldername
    
    def activate(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        
        search = driver.find_element_by_name("q")
        search.send_keys(self.searchword)
        search.send_keys(Keys.RETURN)
        
        try:
            time.sleep(2)
            #main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"islrc")))
            #items = main.find_elements_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
            #imgs = [item.get_attribute('src') for item in items]
            
            links=[] 
            images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd") 
            for image in images:
                if image.get_attribute('src')!=None:
                    links.append(image.get_attribute('src'))

            #counter = 0
            #for image in links:
            #    save_path = os.path.join(self.dir, self.foldername+str(counter)+'.jpg')
            #    wget.download(image, save_path)
            #    counter += 1
            #print(f"Downloaded {counter} images")
            self.dir = self.dir + '/' + self.foldername
            
            for k,i in enumerate(links):
                url = i 
                start = time.time()
                urllib.request.urlretrieve(url, self.dir+'/'+self.searchword+"_"+str(k)+".jpg")
                print(str(k+1)+'/'+str(len(links))+' '+self.searchword+' Downloading....... Download time : '+str(time.time() - start)[:5]+' sec') 
                print(self.searchword+' ---Download Complete---')

            
        finally:
            driver.quit()