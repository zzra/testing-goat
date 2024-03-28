from selenium import webdriver
from selenium.webdriver.firefox.service import Service
path = "/snap/bin/geckodriver"

browser = webdriver.Firefox(service=Service(executable_path=path))
browser.get("http://127.0.0.1:8000")

assert "Congratulations!" in browser.title
print("OK")