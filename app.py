from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 配置 WebDriver
driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

# 打开一个网页
driver.get("http://www.example.com")

# 保持浏览器打开
input("Press Enter to close the browser...")

# 关闭浏览器
driver.quit()
