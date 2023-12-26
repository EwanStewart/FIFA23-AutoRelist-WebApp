


import time
import ipapi
import warnings
import re
import msvcrt

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PC_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'

warnings.filterwarnings("ignore")



def browserSetup(headless_mode: bool = False, user_agent: str = PC_USER_AGENT) -> WebDriver:
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("user-agent=" + user_agent)
    #Insert profile path to Chrome User Data
    options.add_argument("--user-data-dir=C:/Users/ewans/AppData/Local/Google/Chrome/User Data/")
    options.add_argument("--profile-directory=Default")

    options.add_argument('log-level=3')
       
    chrome_browser_obj = webdriver.Chrome(options=options)
    return chrome_browser_obj

def click_button(browser, time, selector):
    element = WebDriverWait(browser, time).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, selector))
    ).click()
    

def wait_for_button(browser, time, selector):
    element = WebDriverWait(browser, time).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )
    return element

def wait_for_button_xpath(browser, time, XPATH):
    element = WebDriverWait(browser, time).until(ec.presence_of_element_located((By.XPATH, XPATH)))
    return element

def main():
    browser = browserSetup(False, PC_USER_AGENT)
    browser.get('https://www.ea.com/fifa/ultimate-team/web-app/')
    
    try:
        click_button(browser, 10, "#Login > div > div > button.btn-standard.call-to-action")
    except:
        pass

    autobuy(browser)

def wait_for_q_key():
    while True:
        key = msvcrt.getch()
        if key == 'q':
            return

def autobuy(browser):
        
        m = {
            "large manager staff item common ut-item-loaded",
            "large manager staff item rare ut-item-loaded",

            "small manager staff item common ut-item-loaded",
            "small manager staff item rare ut-item-loaded",
        }        

        player = {
            #players
            "large player item rare ut-item-loaded",
            "large player item common ut-item-loaded",

            "small player item rare ut-item-loaded",
            "small player item common ut-item-loaded",

            #managers

            "large player item ut-item-loading rare",
            "large player item ut-item-loading common",

            "small player item ut-item-loading rare",
            "small player item ut-item-loading common",

            #managers
            "large manager staff item ut-item-loading common",
            "large manager staff item ut-item-loading rare",

            "small manager staff item ut-item-loading common",
            "small manager staff item ut-item-loading rare"
        }

        bk = {
            "large badge item rare",
            "large badge item common",

            "small badge item rare",
            "small badge item common",

            #kits
            "large kit item rare",
            "large kit item common",

            "small kit item rare",
            "small kit item common"
        }

        #transfers

        

        while (1):
            WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/nav/button[4]'))).click() #store
            WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[3]'))).click() # packs
            WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Classic Packs']"))).click()
            WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div[3]/div[1]/div[3]/button'))).click() #bronze
            WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[4]/section/div/div/button[1]'))).click() #confirm
            counter = 0
            time.sleep(5)

            while (1):
                try:
                    selected_item = wait_for_button_xpath(browser, 2, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[1]/div/div[2]/div/div/div[1]/div")
                except:
                    try:
                        selected_item = wait_for_button_xpath(browser, 2, "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[1]/div/div/div")
                    except:
                        break
                        
                                    
                class_name = selected_item.get_attribute('class')
                time.sleep(0.5)
                if class_name in player:
                    print("player")
                    #WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[9]'))).click() #compare
                    #WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]'))).click() #transfer list
                    try:
                        selected_item = wait_for_button_xpath(browser, 10, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[1]/div/div[2]/div/div/div[1]/div")

                        wait_for_button_xpath(browser, 5, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[1]/button").click()

                        sp = browser.find_element("xpath", "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")
                        sp.click()
                        sp.send_keys(Keys.CONTROL, 'a')
                        sp.send_keys(Keys.BACKSPACE)
                        sp.send_keys(str(int(400)-50))

                        bn = browser.find_element("xpath", "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
                        bn.click()
                        bn.send_keys(Keys.CONTROL, 'a')
                        bn.send_keys(Keys.BACKSPACE)
                        bn.send_keys(400)

                        browser.find_element("xpath", "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/button").click()
                        
                        time.sleep(1)
                    
                    except Exception as e:
                        WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]'))).click()
                        time.sleep(2)
                    
                elif class_name in m:
                   time.sleep(0.5)
                   WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]'))).click()
                   time.sleep(0.5)

                                                              
                elif class_name == "large misc item common":
                    print("coins")
                    WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]'))).click() #redeem    
                elif class_name == "quicksell large misc item rare":
                    WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]'))).click()
                else:
                    print("quicksell " + class_name)
                    WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[10]'))).click() #quicksell
                    time.sleep(0.25)
                    WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[4]/section/div/div/button[1]'))).click() #yes
                    time.sleep(1)
                    
                    

            
main()
