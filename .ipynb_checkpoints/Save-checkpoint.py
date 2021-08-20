#!/usr/bin/env python
# coding: utf-8
import os
import wget

class Save:
    
    def __init__(self, images, word):
        self.path = os.getcwd()
        self.obj = images
        self.searchword = word

    def makedir(self):
        self.foldername = self.searchword + "s"
        self.path = os.path.join(self.path, 'images')
        os.chdir(self.path)
        os.mkdir(self.foldername)
        
    def download_image(self):
        counter = 0
        for image in self.obj:
            save_as = os.path.join(self.path, self.foldername+str(counter)+'.jpg') 
            wget.download(image, save_as)
            counter+=1