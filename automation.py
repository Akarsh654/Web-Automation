# Author: Akrash Sharma

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# get the webdriver and website
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://github.com")

# find, return then click the web element called "Sign in
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username = ""  # type your github username in the empty string
password = ""  # type your github password in the empty string

# locate the login and password web elements
username_box = browser.find_element_by_id("login_field")
password_box = browser.find_element_by_id("password")

# simulate the user typing in the name and password in a textbox
username_box.send_keys(username)
password_box.send_keys(password)
password_box.submit()

# assert that the username is in github
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert username in link_label

# close the browser window
browser.quit()
