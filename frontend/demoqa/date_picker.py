import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://demoqa.com/date-picker')
driver.maximize_window()

now_date = datetime.date.today()
print(f'Today date: {now_date}')

plus_10_days_date = now_date + datetime.timedelta(days=10)
print(f'Today date extended by 10 days: {plus_10_days_date}')

date_format = plus_10_days_date.strftime('%m.%d.%Y').replace('.', '/')
print(f'New date format for input: {date_format}')

input_calendar = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
v = input_calendar.text
print(v)
input_calendar.send_keys(Keys.BACKSPACE)    # clear input. there's no opportunity to solve it with .clear()
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
input_calendar.send_keys(Keys.BACKSPACE)
print('Date input field is empty')

input_calendar.send_keys(date_format)
time.sleep(5)

value_calendar = input_calendar.get_attribute('value')
print(value_calendar)
assert value_calendar == date_format
print('Success! Date entered correctly')
time.sleep(5)
