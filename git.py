from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import  time
import os
import webbrowser
import getpass


reponameinput = input('Enter your repo name: ')

username = "  " # ENTER YOU NAME HERE
password = "  " #  ENTER YOUR PASSWORD

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/")
signin = driver.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > a.HeaderMenu-link.no-underline.mr-3')
signin.click()
username = driver.find_element_by_css_selector('#login_field')
username.send_keys(username)
password = driver.find_element_by_css_selector('#password')
password.send_keys(password)
submit = driver.find_element_by_css_selector('#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block')
submit.click()
newrepo = driver.find_element_by_css_selector('#repos-container > h2 > a')
newrepo.click()

readme = driver.find_element_by_css_selector('#repository_auto_init')
readme.click()

writerepo = driver.find_element_by_css_selector('#repository_name')
writerepo.send_keys(reponameinput)


try:
    element = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#new_repository > div.js-with-permission-fields > button"))
    )
    element.click()
except:
    element.quit()


code = driver.find_element_by_css_selector('#js-repo-pjax-container > div.container-xl.clearfix.new-discussion-timeline.px-3.px-md-4.px-lg-5 > div > div.gutter-condensed.gutter-lg.d-flex.flex-column.flex-md-row > div.flex-shrink-0.col-12.col-md-9.mb-4.mb-md-0 > div.file-navigation.mb-3.d-flex.flex-items-start > span > get-repo > details > summary')
code.click()

copycode = driver.find_element_by_css_selector('#js-repo-pjax-container > div.container-xl.clearfix.new-discussion-timeline.px-3.px-md-4.px-lg-5 > div > div.gutter-condensed.gutter-lg.d-flex.flex-column.flex-md-row > div.flex-shrink-0.col-12.col-md-9.mb-4.mb-md-0 > div.file-navigation.mb-3.d-flex.flex-items-start > span > get-repo > details > div > div > div:nth-child(1) > div > div.ssh-clone-options > div > div > clipboard-copy')
copycode.click()

copyorginalcode = pyperclip.paste()
print(copyorginalcode)

path = "V:/Projects/" # TODO: ENTER YOUR PATH HER LIKE THIS 

os.chdir(path)
os.getcwd()
os.system('git clone '+copyorginalcode)
print('done cloning')

pathtwo = path + reponameinput
os.chdir(pathtwo)
os.getcwd()
os.system('git init')
os.system('git add .')

os.system('code .')# this will open vs code this is where i usally work so it is your choice you can open any editor 






