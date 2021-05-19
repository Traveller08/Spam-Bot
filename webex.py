from os import wait
from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

browser= webdriver.Chrome()

browser.maximize_window()
browser.get(" https://iiitlucknow.webex.com/meet/niharika")
btn=browser.find_element_by_id("smartJoinButton")
btn.click()
time.sleep(15)
pyautogui.moveTo(1082,440)
pyautogui.click()
pyautogui.write("Ankit kumar")
pyautogui.press('tab')
pyautogui.write("lit2020034@iitl.ac.in")
pyautogui.press('enter')
time.sleep(15)


pyautogui.moveTo(806,849)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(1053,848)
pyautogui.click()

# pyautogui.moveTo(860,835)
# pyautogui.click()
# time.sleep(3)
# pyautogui.moveTo(1053,848)
# pyautogui.click()

# pyautogui.moveTo(860,835)
# pyautogui.click()
# time.sleep(3)
# pyautogui.moveTo(1053,848)
# pyautogui.click()



