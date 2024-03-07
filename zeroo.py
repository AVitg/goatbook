import sys
print(sys.version)


from selenium import webdriver
browser=webdriver.Chrome()
print(browser.title)

