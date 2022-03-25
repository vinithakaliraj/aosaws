from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import aosaws_locators as locators
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

s = Service(executable_path='C:/python/chromedriver.exe')
driver = webdriver.Chrome(options=options)
def set_up():
    print(f'Launch {locators.aos_home_page_url} ')
    print('--------------------~*~---------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.aos_home_page_url)
    sleep(2)
    if driver.current_url == locators.aos_home_page_url and driver.title == locators.aos_home_page_title:
        print(f'Yey! {locators.aos_url} Launched Successfully')
        print(f'{locators.aos_url} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.aos_url}  did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')



def create_new_user():
    print('--------------Create New User--------------')
    sleep(1)
    driver.get(locators.aos_home_page_url)
    driver.find_element(By.ID, 'menuUserSVGPath').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(2)
    for key, value in (locators.account_dict.items()):
        driver.find_element(By.XPATH, f'//input[@name="{key}"]').send_keys(value)
        sleep(0.25)
    for key, value in (locators.personal_dict.items()):
        driver.find_element(By.XPATH, f'//input[@name="{key}"]').send_keys(value)
        sleep(0.25)
    driver.find_element(By.NAME, 'countryListboxRegisterPage').click()
    sleep(0.25)
    driver.find_element(By.XPATH, f'//option[@label="Canada"]').click()
    for key, value in (locators.address_dict.items()):
        driver.find_element(By.XPATH, f'//input[@name="{key}"]').send_keys(value)
        sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    driver.find_element(By.ID, 'menuUserLink')
    displayed_username = driver.find_element(By.CSS_SELECTOR,
                                             'span[data-ng-show="userCookie.response"]'
                                             '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')

    if locators.username == displayed_username:
        print('New user is created and new username is displayed in the top menu!')
        print(f'New user username: {locators.username}, new username displayed in the top menu: {displayed_username}')


def log_out():
    print('----------Log Out--------------')
    driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/span').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    print('The user is log out!')


def tear_down():
    if driver is not None:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

def log_in():
    print(f'````````````````Log-in````````````````')
    sleep(1)
    driver.get(locators.aos_home_page_url)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/login-modal/div/div/div[3]/sec-form/sec-view[1]/div/input').send_keys(locators.username)
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/login-modal/div/div/div[3]/sec-form/sec-view[2]/div/input').send_keys(locators.password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()

def check_new_user_can_login():
    if driver.title == locators.aos_home_page_title and driver.current_url == locators.aos_home_page_url:
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.username}")]').is_displayed():
            print(f' ---- User with full name: {locators.username} is displayed. ----')



def contactus():
    print(f'checking for the contact us in the homepage')
    print(f'******************```contact us to displayed`````************************')
    driver.get(locators.aos_home_page_url)
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/header/nav/ul/li[5]/a').click()
    sleep(2)
    print(f'contact us is clickable and displayed')
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[1]/div/sec-view[1]/div/select').send_keys('Laptops')
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[1]/div/sec-view[2]/div/select').send_keys('HP Pavilion 15z Laptop')
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[1]/div/sec-view[3]/div/input').send_keys('hapytest@gmail.com')
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[2]/div/sec-view/div/textarea').send_keys('hi hello')
    sleep(2)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(2)
    driver.find_element(By.XPATH,'//*[@id="registerSuccessCover"]/div/a').click()
    sleep(2)

def main_logo():
    print(f'checking for the main logo in the homepage')
    driver.get(locators.aos_home_page_url)
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[1]').click()
    sleep(2)
    if driver.current_url == locators.aos_home_page_url and driver.title == locators.aos_home_page_title:
        print(f'Yey! {locators.aos_url} Launched Successfully')
        print(f'{locators.aos_url} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.aos_url}  did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')

def top_menu_clickable():
    print(f'Checking for the top menu buttons are clickable')
    print(f'###########top menu##############')
    driver.get(locators.aos_home_page_url)
    sleep(2)
    driver.find_element(By.XPATH,'/html/body/header/nav/ul/li[8]/a').click()
    sleep(2)
    print(f'our products is clickable and displayed')
    driver.find_element(By.XPATH,'/html/body/header/nav/ul/li[7]/a').click()
    sleep(2)
    print(f'special offers is clickable and displayed')
    driver.find_element(By.XPATH,'/html/body/header/nav/ul/li[6]/a').click()
    sleep(2)
    print(f'Popular items is clickable and displayed')
    driver.find_element(By.XPATH,'/html/body/header/nav/ul/li[5]/a').click()
    sleep(2)
    print(f'contact us is clickable and displayed')
    sleep(2)

def checking_homepage_texts():
    print(f'checking for the texts in the homepage')
    print(f'******************```texts to displayed`````************************')
    driver.get(locators.aos_home_page_url)
    driver.find_element(By.ID, 'speakersTxt').click()
    sleep(2)
    print(f' The speaker shopping page is displayed')
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[2]/nav/a[1]').click()
    sleep(2)
    driver.find_element(By.ID, 'tabletsTxt').click()
    sleep(2)
    print(f' The Tablet shopping page is displayed')
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[2]/nav/a[1]').click()
    sleep(2)
    driver.find_element(By.ID, 'laptopsTxt').click()
    sleep(2)
    print(f' The Laptop shopping page is displayed')
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[2]/nav/a[1]').click()
    sleep(2)
    driver.find_element(By.ID, 'miceTxt').click()
    sleep(2)
    print(f' The Mice shopping page is displayed')
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[2]/nav/a[1]').click()
    sleep(2)
    driver.find_element(By.ID, 'headphonesTxt').click()
    sleep(2)
    print(f' The Headphone shopping page is displayed')
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[2]/nav/a[1]').click()
    sleep(2)

def delete_user():
    print(f' deleting the created user')
    print(f'******************```deleting the user`````************************')
    driver.get(locators.aos_home_page_url)
    log_in()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/span').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[1]/div/div[1]/label').click()
    sleep(2)
    if driver.title == locators.aos_home_page_title and driver.current_url == locators.aos_home_page_url:
        if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]/div[1]/div/div[1]/label(.,"{locators.username}")]').is_displayed():
            print(f' ---- User with full name: {locators.username} is displayed. ----')
            driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[6]/button/div').click()
            sleep(2)
        else:
            print(f' ~~~~~~~~~~The username is different so login with correct user~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def add_item_shoppingcart():
    print(f'adding items in the shopping cart')
    print(f'******************```shopping items`````************************')
    driver.get(locators.aos_home_page_url)
    log_in()
    driver.find_element(By.ID, 'speakersTxt').click()
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul/li[1]/p[1]/a').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="productProperties"]/div[4]/button').click()
    sleep(2)
    print(f' the speaker is added to the shopping cart through selecting the product')
    driver.find_element(By.XPATH, '/html/body/div[3]/nav/a[1]').click()
    sleep(2)
    driver.find_element(By.ID, 'details_21').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="productProperties"]/div[4]/button').click()
    sleep(2)
    print(f'the speaker is added to the shopping cart through view details')
    sleep(2)
    print(f'checking out the products in the shopping cart')
    print(f'******************```check out`````************************')
    driver.find_element(By.XPATH, '//*[@id="menuCart"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="checkOutButton"]').click()
    sleep(2)
    driver.find_element(By.ID, 'next_btn').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="paymentMethod"]/div/div[2]/sec-form/sec-view[1]/div/input').send_keys('safepayuser')
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="paymentMethod"]/div/div[2]/sec-form/sec-view[2]/div/input').send_keys('Pass1')
    sleep(2)
    driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/h2').is_displayed()
    assert driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/h2').is_displayed()
    sleep(2)
    driver.find_element(By.ID, 'trackingNumberLabel').is_displayed()
    assert driver.find_element(By.ID, 'trackingNumberLabel').is_displayed()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/p').is_displayed()
    assert driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/p').is_displayed()
    sleep(2)


def view_orders():
    print(f' displaying items in the shopping cart')
    print(f'******************```order number`````************************')
    driver.get(locators.aos_home_page_url)
    log_in()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/span').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div/table/tbody/tr[2]/td[1]/label').is_displayed()
    assert driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div/table/tbody/tr[2]/td[1]/label').is_displayed()

# set_up()
# main_logo()
# checking_homepage_texts()
# top_menu_clickable()
# contactus()
# create_new_user()
# add_item_shoppingcart()
# view_orders()
# check_new_user_can_login()
# log_out()
# delete_user()
# log_in()
# tear_down()