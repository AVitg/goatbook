from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

FFoptions=Options()

FFoptionsll.add_argument("--headless")

FFservice=Service(executable_path="/snap/bin/geckodriver")


browser = webdriver.Firefox(options=FFoptions,service=FFservice)
browser.get("http://localhost:8000")

assert "Congratulations!" in browser.title
print("OK")


## clean up git commit, if you added wrong files
#git rm -r --cached superlists/__pycache__
#