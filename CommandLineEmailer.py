#! python3
# CommandLineEmailer.py - takes the email adress and text string from command line then sends email of that string to that email adress.

## Write a program that takes email address and string of text on the command line

import sys
if len(sys.argv) > 2:
    testEmail = sys.argv[1]
    testString = ' '.join(sys.argv[2:])
else:
    print('Moving On for right now.')

#print(testEmail,testString)

## Using Selenium logs in to your email account 

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://mail.yandex.com.tr/?noretpath=1')
time.sleep(3)
firstElement = browser.find_element_by_css_selector('.button2_theme_mail-white')
firstElement.click()
time.sleep(3)
emailElem = browser.find_element_by_name('login')
emailElem.send_keys('erimserdnmez@yandex.com')
emailElem.submit()
time.sleep(3)
passwordElem = browser.find_element_by_name('passwd')
passwordElem.send_keys('92aF35Gdr10e8'), passwordElem.submit()
time.sleep(3)
try:
    skipElement = browser.find_element_by_css_selector('.Button2_view_pseudo')
    skipElement.click()
except Exception:
    time.sleep(3)
    nextElement = browser.find_element_by_css_selector('.mail-ComposeButton')
    nextElement.click()
    time.sleep(3)
    recieverElem = browser.find_element_by_css_selector('.ComposeRecipients-ToField > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
    recieverElem.send_keys(testEmail)
    
    topicElement = browser.find_element_by_css_selector('.composeTextField')
    topicElement.click()
    topicElement.send_keys('Test')
    bodyElement = browser.find_element_by_css_selector('.cke_wysiwyg_div')
    bodyElement.click()
    bodyElement.send_keys(testString)
    time.sleep(3)
    sendElement = browser.find_element_by_css_selector('.ComposeControlPanel-SendButton > button:nth-child(1)')
    sendElement.click()

