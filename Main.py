from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

urls = []
remove_urls = []

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
s = Service("./chromedriver")
driver = webdriver.Chrome(options=options, service=s)

driver.get("https://www.google.com/")
driver.find_element(By.ID, "L2AGLb").click()
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("What is Selenium")
search_bar.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class = "g"]')))

remove_results = driver.find_elements(By.XPATH, "//div[@class='v7W49e']//div[@class='ULSxyf']//div[@class='AuVD cUnQKe']//div[@class='yuRUbf']/a")
for result_rm in remove_results:
    remove_urls.append(result_rm.get_attribute("href"))

results = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']/a")
for result in results:
    urls.append(result.get_attribute("href"))

# newList = urls-remove_urls

list_difference = []
for element in urls:
    if element not in remove_urls:
        list_difference.append(element)


print(list_difference)

driver.close()