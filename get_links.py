# coding=utf-8
"""
@review: Fabio Curi
Date: 21.11.2018

Script that gathers links from Registro Central and Coordinadora Catalana de Fundacions.
"""

import os
import time
from selenium import webdriver

if '__main__' == __name__:

    cwd = os.getcwd()

    print('Gathering links from Registro Central...')

    num_pages = 162

    # Initialize search
    driver = webdriver.Chrome()
    driver.get("http://fundosbuscador.mjusticia.gob.es/fundosbuscador/cargaBuscador.action?lang=es_es")
    time.sleep(5)
    element = driver.find_element_by_xpath("//input[@value='Buscar'][not(@id='buscadorPortalBoton')]")
    element.click()
    time.sleep(5)

    links = []

    # Go page by page fetching the links
    for i in range(num_pages+1):
        if i == 0:
            continue
        if i > 0:
            print("Loading page " + str(i))
            page = "http://fundosbuscador.mjusticia.gob.es/fundosbuscador/actualizarResultadoBusqueda.action?paginacion.index=" + str(i) + "&lang=es_es"
            driver.get(page)
            time.sleep(2)
            for row in driver.find_elements_by_css_selector("td.columna_01"):
                cell = row.find_element_by_tag_name("a")
                links.append(cell.get_attribute("href"))
            time.sleep(1)

    driver.close()

    uniqueLinksSet = set(links)
    print("Number of links:")
    print(len(uniqueLinksSet))

    with open(cwd + '/RegistroCentralLinks.txt', 'w') as myfile:
    	myfile.write('\n'.join(uniqueLinksSet))

    print('Links from Registro Central gathered!')
    print('Gathering links from Coordinadora Catalana de Fundacions...')

    num_pages = 59

    # Initialize search
    driver = webdriver.Chrome()
    driver.get("http://www.ccfundacions.cat/fundacions")
    time.sleep(5)

    links = []

    # Go page by page fetching the links
    for i in range(num_pages+1):
        print("Loading page " + str(i))
        if i==0:
            page = "http://www.ccfundacions.cat/fundacions"
            driver.get(page)
            time.sleep(2)
        else:
            page = "http://www.ccfundacions.cat/fundacions?page=" + str(i)
            driver.get(page)
            time.sleep(2)

        for row in driver.find_elements_by_css_selector("div.member"):
            cell = row.find_element_by_tag_name("a")
            links.append(cell.get_attribute("href"))
        for row in driver.find_elements_by_css_selector("span.field-content"):
            cell = row.find_element_by_tag_name("a")
            links.append(cell.get_attribute("href"))

        time.sleep(1)

    driver.close()

    uniqueLinksSet = set(links)
    print("Number of links:")
    print(len(uniqueLinksSet))

    with open(cwd + '/CoordinadoraCatalanaLinks.txt', 'w') as myfile:
        myfile.write('\n'.join(uniqueLinksSet))

    print('Links from Coordinadora Catalana de Fundacions gathered!')
