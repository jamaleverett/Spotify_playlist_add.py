from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get("https://open.spotify.com/browse/featured")

element = WebDriverWait (browser, 10).until(
EC.visibility_of_element_located((By.XPATH, "//li[2]/div/a/div/span"))) 
element.click()
WebDriverWait (browser, 20).until(
EC.visibility_of_element_located((By.XPATH, "//input[@class='SearchInputBox_input']"))).send_keys("songs")

browser.find_elements_by_xpath("//*[text()='Log in']").click()

WebDriverWait(browser, 20).until(
EC.visibility_of_element_located((By.XPATH,"//input[@id='login-username']"))).send_keys("")

WebDriverWait(browser, 20).until(
EC.visibility_of_element_located((By.XPATH,"//input[@id='login-password']"))).send_keys("")

WebDriverWait(browser, 10).until(
EC.visibility_of_element_located((By.XPATH, "//button[@id='login-button']"))).click()

items = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='react-contextmenu-wrapper']/div/div/a")))
print(len(items))

for song in items:
    print (song.text)
    actionChains = ActionChains(browser)

    ActionChains.context_click(song).perform()
    element =WebDriverWait(browser, 10).until( 
        EC.visibility_of_element_located((By.XPATH, "//*[text()='Add to Playlist']")))
    element.click()

    element12 = WebDriverWait(browser, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//button[@class='btn asideButton-button btn-green btn-small']")))
    actionChains.move_to_element(element12).click().perform()
    actionChains.context_click(song).perform()
    element00=WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@class='inputBox-input']"))).send_keys("testPlayList")
    
    element11 = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='button-group button-group--horizontal']//div[2]/button")))
    actionChains.move_to_element(element11).click().perform()

    elem=WebDriverWait(browser, 20).until(
         EC.visibility_of_element_located((By.XPATH, "//div[@class='TrackListHeader__entity-name']//span")))
    print (elem.text)
    break




   
   
