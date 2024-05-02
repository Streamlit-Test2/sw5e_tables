from selenium import webdriver
import time

# Setup Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have the chromedriver that matches your Chrome version

# URL of the page
url = 'https://sw5e.com/rules/phb/species'
driver.get(url)

# Let the page load, necessary if the page has lots of JavaScript
time.sleep(10)  # You can adjust the wait time as necessary

# Get raw page source
html = driver.page_source

# Save the raw HTML to a file
with open('page_source.html', 'w', encoding='utf-8') as file:
    file.write(html)

# Clean up: close the browser
driver.quit()
