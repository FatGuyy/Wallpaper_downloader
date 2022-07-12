from sqlite3 import paramstyle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

os.environ['PATH'] += r'.\chromedriver.chromedriver.exe'
driver = webdriver.Chrome()

options = webdriver.ChromeOptions() 
params = {'behaviour': 'allow',"download.default_directory" : os.getcwd()}

#options.add_experimental_option("prefs",prefs)
action = ActionChains(driver)

list = ['Anime', 'God', 'Hills', 'trees']

def button_click(xpath):
    button = driver.find_element(by=By.XPATH, value=xpath)
    button.click()

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)

try:
    driver.get('https://unsplash.com')
except:
    print("Can't find website")

#Searching the title in search bar
driver.implicitly_wait(3)
search_bar =  driver.find_element(by=By.XPATH,value = '/html/body/div/div/header/nav/div[2]/form/div[1]/input' )
search_bar.send_keys(list[0])
search_bar.send_keys(Keys.RETURN)

#/html/body/div/div/div[2]/div[4]/div[1]/div/div/div/div[1] - xpath for first coloumn
#Hoverover the images and click the download button
image_display = driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div[4]/div[1]/div/div/div/div[1]/figure[1]')
action.move_to_element(image_display).perform()
download_button = driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div[4]/div[1]/div/div/div/div[1]/figure[1]/div/div[1]/div/div/div/div/div[2]/div[2]/div[2]/a')
    #download_button.click()
action.move_to_element(download_button).click().perform()

driver.implicitly_wait(5)
#Remaining of the things with device and where it stores (the path of the directory to where it is sent)



time.sleep(10)
driver.close()