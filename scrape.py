import time
import random
import os
import requests
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import csv
from dotenv import load_dotenv

load_dotenv()
url = "https://www.indieonthemove.com/venues?q=seattle&sort_by=relevance&sort_order=descending"
testUrl = "https://indieonthemove.com/venues/renaissance-seattle-hotel-seattle-washington"
email = os.getenv('EMAIL')
pw = os.getenv('PW')
pages = []
driver = webdriver.Chrome(ChromeDriverManager().install())
results = {}

def main():
    login()
    getSites()
    getEmail()
    writeFile()




def login():
    driver.get(url)
    login_page = driver.find_element_by_xpath('//*[@id="navTop"]/div/div[2]/div/a[1]')
    login_page.click()
    username = driver.find_element_by_xpath('//*[@id="email"]')
    username.send_keys(email)
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(pw)
    submit = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div/div/div[2]/form/div[4]/button')
    submit.click()


def getSites():
    # Get list of urls for all venues
    # table = driver.find_element_by_css_selector('tbody.bg-white tr h6.mb-0 a').get_attribute('href')
    for num in range(1,6):
        url2 = f"https://www.indieonthemove.com/venues?page={num}&q=seattle&sort_by=relevance&sort_order=descending"
        driver.get(url2)
        table = driver.find_element_by_css_selector('tbody.bg-white')
        elements = table.find_elements_by_css_selector('a')
        for row in elements:
            col = row.get_attribute('href')
            pages.append(col)
            # print("yolo ",col )


def getEmail():
    # go thru all urls
    for site in pages:
        driver.get(site)
        siteName = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[1]/div[1]/div[1]/h4').text
        booking = driver.find_element_by_css_selector('ul.mb-0').text
        booking = booking.replace(',', ' ')
        booking = booking.replace('\n', ' ')
        try:
            email = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[1]/div[2]/div/ul/li[2]').text
            results[siteName] = {'email': email, 'bookingNotes':booking }
            print(siteName ,email, booking)
        except (NoSuchElementException, StaleElementReferenceException):
            results[siteName] = {'email': 'N/A', 'bookingNotes':booking }


def writeFile():
    print('Writing to Excel File ...')
    with open('promoter.csv', 'w') as f:
        for key in results.keys():
            f.write(f"{key}, {results[key]['email']}, {results[key]['bookingNotes']}\n")

if __name__ == "__main__":
    main()