from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://www.google.com")
#
# # Use a different locator for the search box, such as the name attribute
# googleSearchBox = driver.find_element(By.ID, "APjFqb")
#
# googleSearchBox.send_keys("Automation")
# # driver.find_element(By.NAME, "btnK").click()
# googleSearchBox.send_keys(Keys.RETURN)

driver.get("https://cbms.cnsbd.com/login")



driver.find_element(By.NAME, "username").send_keys("tarif")
driver.find_element(By.NAME, "password").send_keys("123")
driver.find_element(By.NAME, "submit").click()
driver.find_element(By.XPATH, "(//A)[6]").click()
# driver.find_element(By.LINK_TEXT, "Effort Tracking Info").click()

driver.get("https://cbms.cnsbd.com/effortTracking/effortTrackingInfo/effortTrackingTasks")

element = driver.find_element(By.ID,"select2-drop-mask")

# drp = Select(element)
# drp.select_by_visible_text("BISDP-G4")




# driver.find_element(By.XPATH, "//button[@class='agree-btn']").click()



time.sleep(120)

# Close the browser window when done
driver.quit()
