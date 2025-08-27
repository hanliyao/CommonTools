from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=binary_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://xueqiu.com/S/SH688401?md5__1038=eqUhGK4fxRx0xYw405DIOrxLi0Qv%3DoDk0eD")

current_price = driver.find_element(By.CLASS_NAME,'stock-current')

table = driver.find_element(By.CLASS_NAME, "quote-info")

rows = table.find_elements(By.TAG_NAME, "tr")

print(f'current price : {current_price.text}')

for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    column_data = [col.text for col in columns]
    print(column_data)

driver.refresh()

driver.quit()
