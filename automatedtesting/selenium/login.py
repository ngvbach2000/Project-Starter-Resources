# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome("C:\Tools\chromedriver\chromedriver.exe")
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element("id",'user-name').send_keys(user)
    driver.find_element("id",'password').send_keys(password)
    driver.find_element("id",'login-button').click()
    print ('Login successfully')

    print ('Choose all items')
    items = driver.find_elements("class name",'btn_small, btn_inventory')
    for item in items:
        item.click()
        print ('Click')
    
    print ('Go to cart')
    driver.find_element("class name",'shopping_cart_link').click()
    removes = driver.find_elements("class name", "btn_small, cart_button")
    for remove in removes:
        remove.click()
        print ('Remove')

    print ('Done')

login('standard_user', 'secret_sauce')

