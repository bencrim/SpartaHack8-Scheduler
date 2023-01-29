from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/bryan/Desktop/Spartahack/chromedriver_mac64/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://reg.msu.edu/")
location = driver.find_element("id","q")
location.send_keys("Computer Science")
location.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gs-title"))
    )
    
except:
    print("failure")
    driver.quit()
location = driver.find_element("class name", "gs-title")
location.click()
try:
    location = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='MainContent_divOrigID']//li[3]"))
    )
    
except:
    print("failure")
    driver.quit()
location = driver.find_element("xpath", "//div[@id='MainContent_divOrigID']//li[3]")
unfiltered = location.text
split = unfiltered.split("\n")
classes = []
for line in split:
    if line[0].isupper() and line[-1].isnumeric():
        classes.append(line)
class_codes = []
class_titles = []




for c in classes:
    i = 0
    for v in c:
        if v.isnumeric():
            break
        i += 1

    code = c[0:i+3].strip()
    title = c[i+3:].strip()
    class_codes.append(code)
    class_titles.append(title)
print(class_codes)
print(class_titles)
driver.quit()




