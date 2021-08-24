#!/usr/bin/env python
# coding: utf-8
import os
import wget

class Save:
    def __init__(self, word):
        self.path = os.getcwd()
        self.searchword = word
        
    def makedir(self):
        self.foldername = self.searchword + "s"
        self.path = os.path.join(self.path, 'images')
        os.chdir(self.path)
        os.mkdir(self.foldername)
        
        return self.path, self.foldername
        