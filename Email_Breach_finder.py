from cgitb import html
from multiprocessing.connection import wait
from playwright.sync_api import sync_playwright 
import time


with sync_playwright() as p:
    # headless=False, slow_mo=100
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://snusbase.com/login')
    page.locator("xpath=/html/body/div/form/div[1]/input").fill('Your Username Goes Here') #<--input your username here
    page.locator("xpath=/html/body/div/form/div[2]/input").fill('Your Password Goes Here') #<--input your password here
    assert page.locator('#remember_me').is_checked() is True
    page.locator("button.login-button").click()
    page.is_visible('xpath=/html/body/div[3]/div[1]/p[2]/a')
    page.locator('xpath=//*[@id="header"]/a[2]').dispatch_event('click')
    
    
    f = open("gmail.txt", "r")
    for line in f:
        x=line
        page.locator('id=searchbar').fill(x)
        page.locator('xpath=//*[@id="searchform"]/input[3]').dispatch_event('click')
        time.sleep(3)
        html_1 = page.inner_html('#result_count')

        y=html_1.strip()
        z=int(y)
        
        if  z > 0:
            with open (f'breach.txt', 'a') as f:
                f.write(f'Breach Found: {z} : For Gmail: {x} \n' )
            print('Breach Found For: ', x)
        else:
            print('No Breach Found')
    f.close()      
