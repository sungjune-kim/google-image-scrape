#!/usr/bin/env python
# coding: utf-8

from scraper import ImageScraper
from Save import Save

if __name__ == '__main__':
    searchword = input("Search Word : ")
    
    save_instance = Save(searchword)
    path, foldername = save_instance.makedir()
    
    scraper = ImageScraper(path, foldername, searchword)
    scraper.activate()

