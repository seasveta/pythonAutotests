from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""Testing of an online store prototype. Order creation script."""


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
username = 'standard_user'
password = 'secret_sauce'

"""Authorization screen"""

user_input = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_input.send_keys(username)
print('Input username')

password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys(password)
print('Input password')

login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
login_button.click()
print('Click login button')


"""Info product 1. Sauce Labs Bike Light"""

product_1 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]')
value_product_1 = product_1.text
print(f'Name of product 1: {value_product_1}')

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(f'Price of product 1: {value_price_product_1}')

select_product_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
select_product_1.click()
print('Product 1 added to cart')


"""Info product 2. Sauce Labs Fleece Jacket"""

product_2 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
value_product_2 = product_2.text
print(f'Name of product 2: {value_product_2}')

price_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text
print(f'Price of product 2: {value_price_product_2}')

strip_price_1 = value_price_product_1[1:]
strip_price_2 = value_price_product_2[1:]
total_price = round((float(strip_price_1) + float(strip_price_2)), 2)
print(f'Total price: {total_price}')

select_product_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
select_product_2.click()
print('Product 2 added to cart')

cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
cart.click()
print('Cart opened')


"""Match products info in the cart."""

cart_product_1 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
cart_value_product_1 = cart_product_1.text
print(f'Name of product 1: {cart_value_product_1}')
assert value_product_1 == cart_value_product_1
print('Product 1 names match')

cart_price_product_1 = driver.find_element(By.XPATH,
                                           '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
cart_value_price_product_1 = cart_price_product_1.text
print(f'Price of product 1: {cart_value_price_product_1}')
assert value_price_product_1 == cart_value_price_product_1
print('Product 1 prices match')

cart_product_2 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
cart_value_product_2 = cart_product_2.text
print(f'Name of product 2: {cart_value_product_2}')
assert value_product_2 == cart_value_product_2
print('Product 2 prices match')

cart_price_product_2 = driver.find_element(By.XPATH,
                                           '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
cart_value_price_product_2 = cart_price_product_2.text
print(f'Price of product 1: {cart_value_price_product_2}')
assert value_price_product_2 == cart_value_price_product_2
print('Product 2 prices match')

checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout_button.click()
print('Open order form')


"""Order form. Match products info"""

first_name = 'Svet'
last_name = 'Volk'
postal_code = '1111'

input_first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
input_first_name.send_keys(first_name)
print('Input first name')

input_last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
input_last_name.send_keys(last_name)
print('Input last name')

input_postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
input_postal_code.send_keys(postal_code)
print('Input postal code')

continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
continue_button.click()
print('Order overview opened')


"""Order overview screen. Match products info"""

order_product_1 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
value_order_product_1 = order_product_1.text
print(f'Name of product 1: {value_order_product_1}')
assert value_product_1 == value_order_product_1
print('Product 1 names match')

price_order_product_1 = driver.find_element(By.XPATH,
                                            '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_order_product_1 = price_order_product_1.text
print(f'Price of product 1: {value_price_order_product_1}')
assert value_price_product_1 == value_price_order_product_1
print('Product 1 prices match')

order_product_2 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
value_order_product_2 = order_product_2.text
print(f'Name of product 2: {value_order_product_2}')
assert value_product_2 == value_order_product_2
print('Product 2 names match')

price_order_product_2 = driver.find_element(By.XPATH,
                                            '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_price_order_product_2 = price_order_product_2.text
print(f'Price of product 2: {value_price_order_product_2}')
assert value_price_product_2 == value_price_order_product_2
print('Product 2 prices match')

order_total_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_order_total_price = order_total_price.text

strip_order_total_price = value_order_total_price[13:]
print(f'Total price in order: {strip_order_total_price}')

assert total_price == float(strip_order_total_price)
print('Total price match')

finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
finish_button.click()
print('Finish order button click')


"""Created order screen"""

created_order = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
print('Order successfully created')

driver.close()
