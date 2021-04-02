from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("orteil.dashnet.org/cookieclicker")

actions = ActionChains(driver)
