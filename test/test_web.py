from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



import time


driver = webdriver.Chrome()
driver.get("")


username = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
username.send_keys("qa")

password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
password.send_keys('123')

login = driver.find_element("xpath", '/html/body/app-root/layout/empty-layout/div/div/auth-sign-in/div/div[1]/div/form/button')
login.click()

time.sleep(10)

# admin = driver.find_element(By.CLASS_NAME("module"))
admin = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/div/div[2]/landing-home/div/div/div/ul/li/div/div/span')))

admin.click()

time.sleep(10)

driver.switch_to.window(driver.window_handles[1])

stakeholder_management = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/fuse-vertical-navigation/div/div[2]/fuse-vertical-navigation-collapsable-item/div[1]/div/div/div/span')))
ActionChains(driver).move_to_element(stakeholder_management).click(stakeholder_management).perform()

time.sleep(10)

stakeholder_information = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/fuse-vertical-navigation/div/div[2]/fuse-vertical-navigation-collapsable-item/div[2]/fuse-vertical-navigation-basic-item[2]/div/a/div/div')))
# stakeholder_information.click()


ActionChains(driver).move_to_element(stakeholder_information).click(stakeholder_information).perform()

create_button = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/div/div[2]/mat-sidenav-container/mat-sidenav-content/app-stakeholders/div/app-table-wrapper/div/app-stl-table/div[2]/div/div[1]/div[2]/button[2]')))
create_button.click()

time.sleep(10)

stakeholder_name = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/div/div[2]/mat-sidenav-container/mat-sidenav/div/app-stl-form/app-stakeholder-form/div/form/div[2]/mat-form-field[1]/div/div[1]')))
ActionChains(driver).move_to_element(stakeholder_name).click().send_keys("person1").perform()

gender_dropdown = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/div/div[2]/mat-sidenav-container/mat-sidenav/div/app-stl-form/app-stakeholder-form/div/form/div[2]/stl-single-select-dropdown[1]/mat-form-field/div')))
ActionChains(driver).move_to_element(gender_dropdown).click(gender_dropdown).perform()


gender_female = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/mat-option[3]')))
# time.sleep(10)
ActionChains(driver).move_to_element(gender_female).click(gender_female).perform()

country_dropdown = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/div/div[2]/mat-sidenav-container/mat-sidenav/div/app-stl-form/app-stakeholder-form/div/form/div[2]/stl-single-select-dropdown[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]')))
ActionChains(driver).move_to_element(country_dropdown).click(country_dropdown).perform()

sierra_leone = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/mat-option[2]/div')))
ActionChains(driver).move_to_element(sierra_leone).click(sierra_leone).perform()

driver.implicitly_wait(5)

geo_location = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/layout/classy-layout/div/div[2]/mat-sidenav-container/mat-sidenav/div/app-stl-form/app-stakeholder-form/div/form/div[2]/app-dropdown-tree/div/mat-form-field/div/div[1]/div/mat-select/div')))
ActionChains(driver).move_to_element(geo_location).click(geo_location).perform()



driver.quit()