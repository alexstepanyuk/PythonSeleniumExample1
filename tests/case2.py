from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# step 1
driver = webdriver.Chrome()
driver.get("https://testsheepnz.github.io/BasicCalculator.html")

# step 3
elem = driver.find_element(By.ID, "selectBuild")
select = Select(elem)
select.select_by_visible_text("Prototype")
assert "Prototype" in select.first_selected_option.text

# step 4
elem = driver.find_element(By.ID, "number1Field")
# elem.location_once_scrolled_into_view
elem.send_keys("gs")
elem.send_keys(Keys.RETURN)
assert "gs" in elem.get_attribute('value')

# step 5
elem = driver.find_element(By.ID, "number2Field")
elem.send_keys("bu")
elem.send_keys(Keys.RETURN)
assert "bu" in elem.get_attribute('value')

# step 6
elem = driver.find_element(By.ID, "selectOperationDropdown")
select = Select(elem)
select.select_by_visible_text('Concatenate')
assert "Concatenate" in select.first_selected_option.text

# step 7
elem = driver.find_element(By.ID, "calculateButton")
elem.click()

# step 8
elem = driver.find_element(By.ID, "numberAnswerField")
assert "gsbu" in elem.get_attribute('value')
driver.close()
