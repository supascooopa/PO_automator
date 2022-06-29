from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from time import sleep
import os
from datetime import datetime
import openpyxl

# ----- utilities ----- #
service = Service("geckodriver.exe")
driver = webdriver.Firefox(service=service)
url = "http://5.104.0.77/web?#action=373&model=purchase.order&view_type=list&cids=&menu_id=241"
driver.get(url)
today_date = datetime.now().strftime("%d-%m-%Y")


# ----- login in ----- #
login = driver.find_element(By.ID, "login")
login.send_keys("mnalptekin")
password = driver.find_element(By.ID, "password")
password.send_keys(os.environ.get("PASSWORD"))
driver.find_element(By.CLASS_NAME, "btn-primary").click()
sleep(10)
# ----- creating PO ----- #
driver.find_element(By.CLASS_NAME, "o_list_button_add").click()
sleep(2)
driver.find_element(By.LINK_TEXT, "Bir Ürün Ekle").click()
# ----- reading from excel file ----- #
wb = openpyxl.load_workbook("")
# ----- entering products ----- #
product_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/div/input")
test_name = "Iphone 13 128"
product_input.send_keys(test_name)
sleep(3)
if driver.find_element(By.ID, "ui-id-10").is_displayed():
    auto_fill_list = driver.find_element(By.ID, "ui-id-10")
    items = auto_fill_list.find_elements(By.TAG_NAME, "li")
    if len(items) == 2:
        try:
            with open(f"olmayan ürünler {today_date}", "a") as file:
                file.write(test_name)
        except FileNotFoundError:
            with open(f"olmayan ürünler {today_date}", "w") as file:
                file.write(test_name)
    else:
        sleep(7)
        product_input.send_keys(Keys.ENTER)
sleep(3)
quantity = driver.find_element(By.NAME, "product_qty").send_keys(" ")
price = driver.find_element(By.NAME, "price_unit").send_keys(" ")




