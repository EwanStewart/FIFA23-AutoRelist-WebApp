import time
import ipapi
import warnings

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

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
    element = WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, XPATH)))
    return element

def relist(browser):
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/nav/button[3]'))).click()
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[3]'))).click()
        time.sleep(2)
        try:
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button'))).click()
            time.sleep(1)
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[4]/section/div/div/button[2]'))).click()
        except Exception as e:
            print(e)
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div/section[1]/header/button'))).click()
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button'))).click()
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[4]/section/div/div/button[2]'))).click()
        time.sleep(5)


def main():
    browser = browserSetup(False, PC_USER_AGENT)
    browser.get('https://www.ea.com/fifa/ultimate-team/web-app/')
    
    try:
        click_button(browser, 10, "#Login > div > div > button.btn-standard.call-to-action")
    except:
        pass

    try:
        relist(browser)
    except:
        try:
            relist(browser)
        except:
            browser.quit()
            
main()

import subprocess

filepath="C:/Users/ewans/Desktop/sleep.bat"
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()