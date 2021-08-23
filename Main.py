#!/usr/bin/env python
# coding: utf-8

from scraper import ImageScraper
from Save import Save

if __name__ == '__main__':
    searchword = input("Search Word : ")
    
    
    scraper = ImageScraper(searchword)
    images = scraper.activate()

#    saver = Save(images,searchword)
#    saver.makedir()
#    saver.download_image()