from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from tabulate import tabulate
import time
import sys
import os

today = datetime.today()
now = datetime.now()
options = Options()
# options.headless = True
current_time = now.strftime("%H:%M:%S")
driver = webdriver.Chrome(options=options)
url = 'https://www.wealthsimple.com/en-ca/'
googlesheeturl = 'https://docs.google.com/spreadsheets/d/12DBEu_hWAquzwGcX_K3sUWU45TLrEQw278S_r_tRxng/edit#gid=0'
driver.get(url)

# z is row start with 3
# issuer is 2
issuer = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[z]/td[i]/strong[1]"
# amount is 5
amount = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[z]/td[j]/strong[1]"
filterClick = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[5]/div[2]/input[1]"
filterCompany = "//body/div[@id='container']/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]"
filterFillingType = "//body/div[@id='container']/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/div[2]/select[1]"
filterAmount = "//body/div[@id='container']/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]"
transactionRow = "//tr[contains(@class, 'filing-row recent buy-sell')]"
symbols = "//*[@class='bought']/ancestor::tr//a[@data-field='symbol']"
transactionType = "//*[@class='bought']/ancestor::tr//td[4]"
volume = "//*[@class='bought']/following-sibling::strong[1]"
shares = "//*[@class='bought']/following-sibling::strong[2]"
bought = "//*[@class='bought']"
sold = "//*[@class='sold']"

driver.find_element_by_xpath(filterFillingType).send_keys("All")
driver.find_element_by_xpath(filterAmount).send_keys("5000")
driver.find_element_by_xpath(filterClick).click()
boughtGroups = driver.find_elements_by_xpath(bought)
soldGroups = driver.find_elements_by_xpath(sold)
symbolsGroups = driver.find_elements_by_xpath(symbols)
transactionGroups = driver.find_elements_by_xpath(transactionType)
volumeGroups = driver.find_elements_by_xpath(volume)
sharesGroups = driver.find_elements_by_xpath(shares)
rows = driver.find_elements_by_xpath("//table/tbody/tr")
dateToday = today.strftime("%Y-%m-%d")

# print("\n[boughtGroups] Total of " + str(len(boughtGroups)) +
#       " companies bought their shares \n")
# print("[soldGroups] Total of " + str(len(soldGroups)) +
#       " companies sold their shares \n")
# print("[rows] Total of " + str(len(rows)) +
#       " companies bought/sold their shares \n\n")

def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

data = []
for x in range(len(boughtGroups)):
    data.append(symbolsGroups[x].text)
    # data.append(transactionGroups[x].text)
    data.append(boughtGroups[x].text)
    data.append(sharesGroups[x].text)

chunkData = list(chunk_list(data, 3))
# print("\n\nToday's date is " + dateToday + '\n')

chunkDataTable = tabulate(chunkData, headers=[
    'Symbol',  'Amount', 'Share Price'], tablefmt="html")

# chunkDataTable = tabulate(chunkData, headers=[
#     'Symbol', 'Amount', 'Share Price'])

# print(chunkDataTable)

# ############## Text File ##############
# extension = ".txt"
# save_path = "C:/Users/chung/Desktop/InsiderTrading"
# filename = dateToday + " Insider Buy" + extension
# completefileName = os.path.join(save_path, filename)
# f = open(completefileName, 'w', encoding='utf8')
# f.write("Last updated " + current_time)
# f.write("\n\n\n")
# f.write(chunkDataTable)
# f.close()
# ############## Text File ##############

# print(tabulate(chunkData, headers=[
# 'Symbol', 'Amount', 'Share Price']))

driver.quit()
