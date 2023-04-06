from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# step 1
driver = webdriver.ChromiumEdge()
driver.get("https://testsheepnz.github.io/BasicCalculator.html")
print("step1 done")

# step 3
elem = driver.find_element(By.ID, "selectBuild")
select = Select(elem)
select.select_by_visible_text("Prototype")
assert "Prototype" in select.first_selected_option.text
print("step3 done")

# step 4
elem = driver.find_element(By.ID, "number1Field")
# elem.location_once_scrolled_into_view
elem.send_keys("2")
elem.send_keys(Keys.RETURN)
assert "2" in elem.get_attribute('value')
print("step4 done")

# step 5
elem = driver.find_element(By.ID, "number2Field")
elem.send_keys("3")
elem.send_keys(Keys.RETURN)
assert "3" in elem.get_attribute('value')
print("step5 done")

# step 6
elem = driver.find_element(By.ID, "selectOperationDropdown")
select = Select(elem)
select.select_by_visible_text('Subtract')
assert "Subtract" in select.first_selected_option.text
print("step6 done")

# step 7
elem = driver.find_element(By.ID, "calculateButton")
elem.click()
print("step7 done")

# step 8
elem = driver.find_element(By.ID, "numberAnswerField")
assert "-1" in elem.get_attribute('value')
driver.close()
print("step8 done")


