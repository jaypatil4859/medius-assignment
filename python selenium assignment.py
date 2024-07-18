from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://forms.gle/WT68aV5UnPajeoSc8")

name = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
contact_number = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
email_id = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
address = driver.find_element(By.CLASS_NAME, "KHxj8b.tL9Q4c")
pincode = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
dob = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input")
gender = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input")
verification_code  = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input")

name.send_keys("Jay Patil")
contact_number.send_keys("7715843577")
email_id.send_keys("ijaypatil04@gmail.com")
address.send_keys("Trimurti Sadan, near Mahadev temple, Mohili gaon, Ambivali east")
pincode.send_keys("421102")
dob.send_keys("04-11-2000")
gender.send_keys("Male")
verification_code.send_keys("GNFPYC")

submit = driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac").click()

screen_capture = driver.get_screenshot_as_file("confirmation_page.png")

driver.quit()