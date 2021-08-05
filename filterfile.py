# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:04:48 2021
/****************************************************************************************************************************
File         : filterfile.py
Author       : Michael Alvarez
Version      : [Spyder: Python 3.8]
Date         : 2021-08-02
****************************************************************************************************************************/
"""

def filterFile():
    file_name = input("Type the name of the file to be filtered : ")
    replace_this = input("Type what should be replaced : ")
    replace_with = input("Type the replacement : ")
    
    # with open _ as _ ensures the file is closed after use, avoiding memory leaks..
    with open(file_name+".txt", "r") as tag_file:
        lines = tag_file.readlines()
        
        for line in lines:
            print("{}".format(line.replace(replace_this,replace_with)))
filterFile()
