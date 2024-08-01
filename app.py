from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def index():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Remote(
        command_executor='http://100.20.92.101:4444/wd/hub',  # 修改为你的WebDriver地址
        options=options
    )

    driver.get("http://www.example.com")
    title = driver.title
    driver.quit()
    return f"Page title is {title}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
