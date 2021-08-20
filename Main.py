#!/usr/bin/env python
# coding: utf-8

from scraper import ImageScraper

if __name__ == '__main__':
    searchword = input("Search Word : ")
    num_image = int(input("How many images do you want to scrape? : "))
    
    scraper = ImageScraper(searchword)
    scraper.activate(num_image)