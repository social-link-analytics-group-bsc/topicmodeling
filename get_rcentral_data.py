# coding=utf-8
"""
@author: Fabio Curi
Date: 21.11.2018

Scrapes links from Registro Central.
"""

import os
import sys
import time
from selenium import webdriver

if '__main__' == __name__:

    cwd = os.getcwd()
    reload(sys)
    sys.setdefaultencoding('utf8')
    foundationsLinks = []

    with open(cwd + '/RegistroCentralLinks.txt') as f:
        foundationsLinks = f.readlines()

    # Initialize search
    driver = webdriver.Chrome()
    for foundationIdx, link in enumerate(foundationsLinks):
        if foundationIdx > -1: # Set this condition because webdriver has a limit of scrapping data !
            driver.get(link)
            time.sleep(5)
            outputData = []
            try:
                for idx, row in enumerate(driver.find_elements_by_css_selector("ul")):
                    if idx > 19:
                        break
                    if idx > 12:
                        if idx == 13:
                            outputData.append("Nombre fundación:\n")
                            outputData.append(driver.find_elements_by_css_selector("h3")[1].text)
                            outputData.append("\n")
                        if idx == 14:
                            outputData.append("Fines:\n")
                        if idx == 15:
                            outputData.append("Actividades:\n")
                        if idx == 16:
                            outputData.append("Fundadores:\n")
                        if idx == 17:
                            outputData.append("Patronos:\n")
                        if idx == 18:
                            outputData.append("Directivos:\n")
                        if idx == 19:
                            outputData.append("Órganos:\n")
                        for item in row.find_elements_by_css_selector("li"):
                            outputData.append(item.text + "\n")
                outputFileName = cwd + '/RegistroCentral/' + str(foundationIdx)
                outputFile = open(outputFileName,'w+')
                for string in outputData:
                    outputFile.write(string)
                outputFile.close()
                print('Foundation ' + str(foundationIdx) + ' from Registro Central scrapped!')
            except:
                print('Error loading foundation ' + str(foundationIdx))

    driver.close()
