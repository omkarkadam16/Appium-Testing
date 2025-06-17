# test_calc.py

from appium import webdriver
import time
from desired_caps import desired_caps

# Connect to Appium Server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Wait for app to launch
time.sleep(2)

# 2 + 3 =
driver.find_element("id", "com.android.calculator2:id/digit_2").click()
driver.find_element("id", "com.android.calculator2:id/op_add").click()
driver.find_element("id", "com.android.calculator2:id/digit_3").click()
driver.find_element("id", "com.android.calculator2:id/eq").click()

# Get and print result
result = driver.find_element("id", "com.android.calculator2:id/result").text
print("Result: ", result)

# End the session
driver.quit()
