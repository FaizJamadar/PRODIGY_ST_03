import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#Tc_01 Login with valid credentials (standard_user)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)
if "inventory" in driver.current_url:
    print("TC_01 passed- standard_user logged in succesfully")
else:
    print("TC_01 failed- standard_user login failed")
    driver.quit()
    time.sleep(1)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# TC_01 - Login with valid credentials (standard_user)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if "inventory" in driver.current_url:
    print("TC_01 PASSED - standard_user logged in successfully")
else:
    print("TC_01 FAILED - login did not work")

driver.quit()
time.sleep(1)

# TC_02 - Login with locked_out_user (should show error)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
if "locked out" in error.lower():
    print("TC_02 PASSED - locked_out_user was blocked:", error)
else:
    print("TC_02 FAILED - expected error but got:", error)

driver.quit()
time.sleep(1)

# TC_03 - Login with wrong password
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrongpassword123")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
if error:
    print("TC_03 PASSED - wrong password rejected:", error)
else:
    print("TC_03 FAILED - wrong password was accepted")

driver.quit()
time.sleep(1)

# TC_04 - Login with wrong username
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("random_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
if error:
    print("TC_04 PASSED - wrong username rejected:", error)
else:
    print("TC_04 FAILED - wrong username was accepted")

driver.quit()
time.sleep(1)

# TC_05 - Login with empty username
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
if "username" in error.lower():
    print("TC_05 PASSED - empty username caught:", error)
else:
    print("TC_05 FAILED")

driver.quit()
time.sleep(1)

# TC_06 - Login with empty password
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
if "password" in error.lower():
    print("TC_06 PASSED - empty password caught:", error)
else:
    print("TC_06 FAILED")

driver.quit()
time.sleep(1)

# TC_07 - Both fields empty
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
if error:
    print("TC_07 PASSED - both fields empty caught:", error)
else:
    print("TC_07 FAILED")

driver.quit()
time.sleep(1)

# TC_08 - Login with problem_user
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("problem_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if "inventory" in driver.current_url:
    print("TC_08 PASSED - problem_user logged in")
else:
    print("TC_08 FAILED")

driver.quit()
time.sleep(1)

# TC_09 - Login with performance_glitch_user (takes longer to load)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(6)

if "inventory" in driver.current_url:
    print("TC_09 PASSED - performance_glitch_user logged in (slow)")
else:
    print("TC_09 FAILED")

driver.quit()
time.sleep(1)

# TC_10 - Wrong username and wrong password both
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("fakeuser")
driver.find_element(By.ID, "password").send_keys("fakepass")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
if error:
    print("TC_10 PASSED - fake credentials rejected:", error)
else:
    print("TC_10 FAILED")

driver.quit()

print("\nDone - all test cases executed")
