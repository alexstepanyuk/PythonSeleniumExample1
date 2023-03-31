from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# step1
driver = webdriver.Chrome()
driver.get("https://testsheepnz.github.io/random-number.html")

# step2
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# step3
select = Select(driver.find_element(By.ID, 'buildNumber'))
select.select_by_visible_text("Demo")

# step4
button_element = driver.find_element(By.ID, 'rollDiceButton')
button_element.click()
driver.implicitly_wait(10)

# step5
element = driver.find_element(By.ID, "numberGuess")
element.send_keys("string")

# step6
button_element = driver.find_element(By.ID, 'submitButton')
button_element.click()

# step7
element = driver.find_element(By.XPATH, '//*[@id="feedbackLabel"]/font/b/i')
print(element.text)
driver.close()