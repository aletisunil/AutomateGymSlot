from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import environ


def Booking():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    #browser=webdriver.Chrome("/Users/sunilaleti/Documents/chromedriver") #Enter Location of Chrome driver
    browser.maximize_window()
    try:
        browser.get("https://reclink.uta.edu/booking/5dcc386e-4bd5-4474-80ec-a47472d3963a")
        sleep(2)
        browser.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button').click()
        browser.find_element_by_xpath('//*[@id="i0116"]').send_keys(environ[.get"Email"])
        browser.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        sleep(2)
        browser.find_element_by_xpath('//*[@id="i0118"]').send_keys(environ.get["Password"])
        sleep(2)
        browser.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input').click()
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        browser.find_element_by_xpath('//*[@id="divBookingSlots"]/div/div[1]/div/button').click()
        print("Booked Successfully")

    except:
        print("Booking Failed")

    finally:
        browser.quit()

if __name__ == '__main__':
    Booking()