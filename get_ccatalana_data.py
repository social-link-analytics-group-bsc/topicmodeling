# coding=utf-8
"""
@author: Fabio Curi
Date: 21.11.2018

Scrapes links from Coordinadora Catalana de Fundacions.
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

    with open(cwd + '/CoordinadoraCatalanaLinks.txt') as f:
        foundationsLinks = f.readlines()

    # Initialize search
    driver = webdriver.Chrome()
    for foundationIdx, link in enumerate(foundationsLinks):
        if foundationIdx > -1:  # Set this condition because webdriver has a limit of scrapping data !
            driver.get(link)
            time.sleep(5)
            dataText = []
            try:
                for idx, row in enumerate(driver.find_elements_by_css_selector("tr")):
                    if idx == 0:
                        continue
                    else:
                        if idx == 1:
                            dataText.append(row.find_element_by_css_selector("td.label").text)
                            dataText.append('\n' + (row.find_element_by_css_selector("td.value").text))
                        else:
                            dataText.append('\n' + (row.find_element_by_css_selector("td.label").text))
                            dataText.append('\n' + (row.find_element_by_css_selector("td.value").text))

                outputFileName = cwd + "/CoordCatalanaFund/" + str(foundationIdx)
                outputFile = open(outputFileName, 'w+')
                for string in dataText:
                    outputFile.write(string)
                outputFile.close()
                print('Foundation ' + str(foundationIdx) + ' from Coordinadora Catalana de Fundacions scrapped!')

            except:
                print('Error loading foundation ' + str(foundationIdx))
    driver.close()
