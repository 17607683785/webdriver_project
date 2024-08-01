from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 配置 WebDriver
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',  # 修改为你的WebDriver地址
    options=options
)

# 打开一个网页
driver.get("http://www.example.com")

# 保持浏览器打开
input("Press Enter to close the browser...")

# 关闭浏览器
driver.quit()

