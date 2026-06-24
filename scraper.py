from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

cities = ["Denver", "London", "Tokyo", "Sydney", "Cairo", "Moscow", "Mumbai", "Toronto", "Paris", "Berlin"]
results = []

try:
    for city in cities:
        driver.get(f"https://wttr.in/{city}?format=%l:+%C+%t+%h+%w")
        sleep(2)
        data = driver.find_element(By.CSS_SELECTOR, 'body').text
        print(data)
        results.append({'raw_data': data, 'city': city})
        sleep(1)  # be polite, pause between requests

    with open('raw_weather_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['city', 'raw_data'])
        writer.writeheader()
        writer.writerows(results)

    print("Saved to raw_weather_data.csv")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()