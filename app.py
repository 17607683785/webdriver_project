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

    selenium_hub_host = os.environ.get('SELENIUM_HUB_HOST')
    selenium_hub_port = os.environ.get('SELENIUM_HUB_PORT')

    if not selenium_hub_host or not selenium_hub_port:
        return "'SELENIUM_HUB_HOST' or 'SELENIUM_HUB_PORT' environment variable is not set", 500

    try:
        driver = webdriver.Remote(
            command_executor=f'http://{selenium_hub_host}:{selenium_hub_port}/wd/hub',
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
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
