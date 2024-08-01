from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

app = Flask(__name__)

@app.route('/')
def index():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Remote(
            command_executor=f'http://{os.environ["SELENIUM_HUB_HOST"]}:{os.environ["SELENIUM_HUB_PORT"]}/wd/hub',
            options=options,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        driver.get("http://www.example.com")
        title = driver.title
        driver.quit()
        return f"Page title is {title}"
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
