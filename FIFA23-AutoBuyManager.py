import time
import ipapi
import warnings

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PC_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'

warnings.filterwarnings("ignore")

def getCCodeLangAndOffset() -> tuple:
    try:
        nfo = ipapi.location()
        lang = nfo['languages'].split(',')[0]
        geo = nfo['country']
        tz = str(round(int(nfo['utc_offset']) / 100 * 60))
        return(lang, geo, tz)
    except:
        getCCodeLangAndOffset()

LANG, GEO, TZ = getCCodeLangAndOffset()

def browserSetup(headless_mode: bool = False, user_agent: str = PC_USER_AGENT) -> WebDriver:
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("user-agent=" + user_agent)
    options.add_argument('lang=' + LANG.split("-")[0])

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

def main():
    browser = browserSetup(False, PC_USER_AGENT)
    browser.get('https://www.ea.com/fifa/ultimate-team/web-app/')
    
    try:
        click_button(browser, 10, "#Login > div > div > button.btn-standard.call-to-action")
    except:
        pass

    autobuy(browser)

def autobuy(browser):
        orignal_mbn_price = 1500
        mbn_price = orignal_mbn_price
        increment_mbn_price = 100
        times_without_success = 0
        increment_mbn = False

        increment_mbn_count = 0
        decrement_mbn_count = 0


        #transfers
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/nav/button[3]'))).click()
        #search the transfer market
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]'))).click()
        #managers
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[1]/div/button[2]'))).click()
    
        #nation select start
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/div/div'))).click()

        #England
        WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/div/ul/li[4]'))).click()
        #nation select end


        #league select start
        #WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[5]/div/div'))).click()

        #EPL
        #WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[5]/div/ul/li[2]'))).click()
        #league select end

        while (1):
            #start max buy now
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')))
            mbn = browser.find_element("xpath", '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')
            mbn.click()
            mbn.send_keys(Keys.CONTROL, 'a')
            mbn.send_keys(Keys.BACKSPACE)
            mbn.send_keys(mbn_price)
            #end max buy now

            #search
            WebDriverWait(browser, 60).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]'))).click()

            #start buy now
            try:
                WebDriverWait(browser, 1).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]'))).click()
                WebDriverWait(browser, 1).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[4]/section/div/div/button[1]'))).click()
                WebDriverWait(browser, 2).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]'))).click()
                browser.quit()
                time.sleep(10)
                main()
            except:
                WebDriverWait(browser, 1).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[1]/button[1]'))).click()
                times_without_success += 1

            #end buy now

            if not (increment_mbn):
                mbn_price += increment_mbn_price
                increment_mbn_count+=1
            else:
                mbn_price -= increment_mbn_price
                decrement_mbn_count+=1

            if (increment_mbn_count == 2):
                increment_mbn = True
                increment_mbn_count = 0
                mbn_price = orignal_mbn_price
            elif (decrement_mbn_count == 3):
                increment_mbn = False
                decrement_mbn_count = 0
                mbn_price = orignal_mbn_price


            if (times_without_success == 25):
                browser.quit()
                time.sleep(250)
                break

            time.sleep(1)

        main()
  


            
main()
