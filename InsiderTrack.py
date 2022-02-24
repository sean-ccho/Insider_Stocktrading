from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from tabulate import tabulate
import time
import sys
import os


class personalInsiderTracker:

    def tracker():
        today = datetime.today()
        now = datetime.now()
        options = Options()
        # options.headless = True
        current_time = now.strftime("%H:%M:%S")
        driver = webdriver.Chrome(options=options)
        url = 'https://ceo.ca/api/sedi/?symbol=&amount=&transaction=&insider='
        googlesheeturl = 'https://docs.google.com/spreadsheets/d/12DBEu_hWAquzwGcX_K3sUWU45TLrEQw278S_r_tRxng/edit#gid=0'
        driver.get(url)
        dateToday = today.strftime("%Y-%m-%d")
        print(dateToday)
        filterClick = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[5]/div[2]/input[1]"
        FilterbyCompany = "//*[@id='sedi-filter']/div[1]/div[2]/input[1]"
        # companyTransactionDate = "//strong[contains(text(),'2021-09-07')]"
        scompanyTransactionDate = "//strong[contains(text(),'" + \
            dateToday + "')]"

        # print(companyTransactionDate)
        print(scompanyTransactionDate)

        driver.find_element_by_xpath(FilterbyCompany).send_keys("NBM")
        driver.find_element_by_xpath(filterClick).click()

        try:
            if driver.find_element_by_xpath(scompanyTransactionDate):
                s = "NBM Insider Purchased Shares!!"
                print(s)
        except:
            s = "No NBM Insider transaction"
            print(s)

        driver.quit()
        return s
