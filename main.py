# import selenium modules, classes and methods
# You will need the webdriver class to use hte method for your specified webdriver....in my case I am using chrome driver
# Also have time installed to mimic page loading wait-time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

#add faacebook email and password, If you already have account you can skip line 22-39.These line help you login using your facebook account...It is the easiest way i found so far to login.
FACEBOOK_EMAIL = ''
FACEBOOK_PASSWORD = ''
#add chrom driver path oon your device
chrome_driver_path = ''
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
#This automates the button clicks to log in
sleep(3)
login_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_btn.click()

sleep(3)
facebook_login_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login_btn.click()

sleep(3)
#Another window pops-up so we need to move to the next window usind 'window_handles' method.
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

#automate email and password input and press enter
email.send_keys(FACEBOOK_EMAIL)
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)
#switch back to tinder window
driver.switch_to.window(tinder_window)

#wait a few seconds to login and configure location, notification and cookies
sleep(6)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Although it does not check if the people are your type, but it aouto likes every profile that comes your way hahaha
for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
        #You will get this exception whn you get a match.The like button becomes hidden
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        #You wll get tis exception when the screen is loading
        except NoSuchElementException:
            sleep(2)

driver.quit()