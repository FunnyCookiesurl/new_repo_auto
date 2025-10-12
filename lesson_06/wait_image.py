from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 40, 0.1)
waiter.until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

cont = driver.find_element(By.ID, "image-container")
images = cont.find_elements(By.TAG_NAME, "img")
third_image = images[2]
src = third_image.get_attribute("src")
print(src)

driver.quit()
