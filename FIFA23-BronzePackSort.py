import time
import ipapi
import warnings
import re

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

def autobuy(browser):
        
        possibleItems = {
           #players
            "large player item rare ut-item-loaded": "400",
            "large player item common ut-item-loaded": "400",

            "small player item rare ut-item-loaded": "400",
            "small player item common ut-item-loaded": "400",

            "large player item ut-item-loading rare": "400",
            "large player item ut-item-loading common": "400",

            "small player item ut-item-loading rare": "400",
            "small player item ut-item-loading common": "400",
        }

        

        possibleBGs = ["https://www.ea.com/ea-sports-fc/ultimate-team/web-app/content/24B23FDE-7835-41C2-87A2-F453DFDB2E82/2024/fut/items/images/backgrounds/itemBGs/large/cards_bg_e_0_1_1.png"]

        #transfers
        time.sleep(2)
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/nav/button[3]'))).click() #transfers
        time.sleep(2)
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[3]'))).click() #transfer list



        counter = 0
        while (1):
            try:
                wait_for_button_xpath(browser, 5, "/html/body/main/section/section/div[2]/div/div/div/section[1]/header/button[1]").click()
                time.sleep(5)
            except:
                print("No Items Sold")

            try:
                wait_for_button_xpath(browser, 5, "/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button[1]").click()
                wait_for_button_xpath(browser, 5, "/html/body/div[4]/section/div/div/button[2]").click()
                time.sleep(5)
            except:
                print("No Relist")
            try:
                selected_item = wait_for_button_xpath(browser, 10, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[1]/div/div[2]/div/div/div[1]/div")
                class_name = selected_item.get_attribute('class')
                style = selected_item.get_attribute('style')

                if class_name in possibleItems:
                    price = possibleItems[class_name]

                    # matches = re.findall(r'"([^"]+)"', style)
                    # if not matches[0] in possibleBGs:
                    #     print("bg not found")
                    #     break

                    wait_for_button_xpath(browser, 5, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[1]/button").click()


                    sp = browser.find_element("xpath", "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")
                    sp.click()
                    sp.send_keys(Keys.CONTROL, 'a')
                    sp.send_keys(Keys.BACKSPACE)
                    sp.send_keys(str(int(price)-50))

                    bn = browser.find_element("xpath", "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
                    bn.click()
                    bn.send_keys(Keys.CONTROL, 'a')
                    bn.send_keys(Keys.BACKSPACE)
                    bn.send_keys(price)

                    browser.find_element("xpath", "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/button").click()
                    
                    time.sleep(3)
            
                else:
                    print("class name not found")
                    print(class_name)
                    break
            except Exception as e:
                time.sleep(3)

                try:
                    wait_for_button_xpath(browser, 5, "/html/body/main/section/section/div[2]/div/div/div/section[1]/header/button[1]").click()
                    time.sleep(5)
                except:
                    print("No Items Sold")

                try:
                    wait_for_button_xpath(browser, 5, "/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button[1]").click()
                    wait_for_button_xpath(browser, 5, "/html/body/div[4]/section/div/div/button[2]").click()
                    time.sleep(5)
                except:
                    print("No Relist")

                print(e)
                if counter == 1:
                    break
                else:
                    counter += 1
            
main()
