from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
driver = None


def go_to_home():
    home_btn = driver.find_element_by_css_selector('a[aria-label="Home"]')
    home_btn.click()


def login(url):
    driver.get(url)
    email_field = driver.find_element_by_id("email")
    password_field = driver.find_element_by_id("pass")
    login_btn = driver.find_element_by_css_selector(
        'button[data-testid="royal_login_button"]')

    email = "rovekoy922@94jo.com"
    password = getpass("Enter password: ")
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_btn.click()


def initiate_browser():
    driver = webdriver.Chrome(chrome_options=option)
    return driver


def main():
    global driver
    driver = initiate_browser()
    login("https://facebook.com")
    go_to_home()
    driver.quit()


if __name__ == "__main__":
    main()
