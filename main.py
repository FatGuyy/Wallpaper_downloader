from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

os.environ['PATH'] += r'.\chromedriver.chromedriver.exe'
        #chrome_options = Options()
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        #driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

list = ['Anime', 'God', 'Hills', 'trees', ]


def button_click(xpath):
    button = driver.find_element(by=By.XPATH, value=xpath)
    button.click()


try:
    driver.get('https://unsplash.com')
except:
    print("Can't find website")
#Searching the title in search bar
driver.implicitly_wait(3)
search_bar =  driver.find_element(by=By.XPATH,value = '/html/body/div/div/header/nav/div[2]/form/div[1]/input' )
search_bar.send_keys(list[0])
search_bar.send_keys(Keys.RETURN)

#Hoverover the images and click the download button


#Remaining of the things with device and where it stores (the path of the directory to where it is sent)



time.sleep(5)
driver.close()