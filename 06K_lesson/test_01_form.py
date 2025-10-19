from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = EdgeService(
    r'D:\SkyPro\Python Auto\repository_clone\edgedriver\msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "first-name"))
)

input_field = driver.find_element(By.NAME, 'first-name')
input_field.send_keys("Иван")
input_field = driver.find_element(By.NAME, 'last-name')
input_field.send_keys("Петров")
input_field = driver.find_element(By.NAME, 'address')
input_field.send_keys("Ленина, 55-3")
input_field = driver.find_element(By.NAME, 'e-mail')
input_field.send_keys("test@skypro.com")
input_field = driver.find_element(By.NAME, 'phone')
input_field.send_keys("+7985899998787")
input_field = driver.find_element(By.NAME, 'zip-code')
input_field.send_keys("")
input_field = driver.find_element(By.NAME, 'city')
input_field.send_keys("Москва")
input_field = driver.find_element(By.NAME, 'country')
input_field.send_keys("Россия")
input_field = driver.find_element(By.NAME, 'job-position')
input_field.send_keys("QA")
input_field = driver.find_element(By.NAME, 'company')
input_field.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

zip_code = driver.find_element(By.ID, "zip-code")
assert "alert-danger" in zip_code.get_attribute("class")

first_name = driver.find_element(By.ID, "first-name")
assert "alert-success" in first_name.get_attribute("class")

last_name = driver.find_element(By.ID, "last-name")
assert "alert-success" in last_name.get_attribute("class")

address = driver.find_element(By.ID, "address")
assert "alert-success" in address.get_attribute("class")

e_mail = driver.find_element(By.ID, "e-mail")
assert "alert-success" in e_mail.get_attribute("class")

phone = driver.find_element(By.ID, "phone")
assert "alert-success" in phone.get_attribute("class")

city = driver.find_element(By.ID, "city")
assert "alert-success" in city.get_attribute("class")

country = driver.find_element(By.ID, "country")
assert "alert-success" in country.get_attribute("class")

job_position = driver.find_element(By.ID, "job-position")
assert "alert-success" in job_position.get_attribute("class")

company = driver.find_element(By.ID, "company")
assert "alert-success" in company.get_attribute("class")

driver.quit()
