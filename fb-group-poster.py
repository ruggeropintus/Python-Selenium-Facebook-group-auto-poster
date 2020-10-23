from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

chromeDriverPath = "/home/ruggero/dev/git/Python-Selenium-Facebook-group-auto-poster/chromedriver"
facebookWebsite = "https://www.facebook.com"

emailElementID = "email"
passElementID = "pass"
loginElementID = "royal_login_button"
createPostID = "Create Post"


def main():
    # Insert here credentials and groups

    message = ["Ciao Mondo 1", "Hello World 2", "Salu Le Monde"]

    # "Checkout an amazing selenium script for posting automaticaaly on Facebook groups! https://github.com/ethanXWL/Python-Selenium-Facebook-group-poster"

    # Set up paths of images to post
    # images_list = ['C:/Users/OEM/Pictures/sample1.jpg',
    #                'C:/Users/OEM/Pictures/sample2.jpg']
    imagesList = []

    driver = initializeChromeDriver()

    facebookLogin(driver, account, password)

    postInGroups(driver, groupsLinkList, message, imagesList)

    driver.close()


def initializeChromeDriver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chromeDriverPath, chrome_options=chrome_options)
    return driver


def facebookLogin(driver, account, password):
    driver.get(facebookWebsite)
    acceptAll(driver)
    login(driver, account, password)


def acceptAll(driver):
    acceptAllElement = driver.find_element(
        By.XPATH, '//*[@data-testid="cookie-policy-banner-accept"]')
    acceptAllElement.click()


def login(driver, account, password):
    emailElement = driver.find_element(
        By.XPATH, '//*[@id="' + emailElementID + '"]')
    emailElement.send_keys(account)

    passElement = driver.find_element(
        By.XPATH, '//*[@id="' + passElementID + '"]')
    passElement.send_keys(password)

    loginElement = driver.find_element(
        By.XPATH, '//*[@data-testid="' + loginElementID + '"]')
    loginElement.click()

    time.sleep(5)


def postInGroups(driver, groupsLinkList, message, imagesList):
    for num, group in enumerate(groupsLinkList):

        print("Posting message in group: ", group)
        time.sleep(10)
        driver.get(group)
        time.sleep(10)

        driver.find_element(
            By.XPATH, '//*[@aria-label="' + createPostID + '"]').click()
        time.sleep(10)

        # postBox = driver.find_element_by_css_selector(
        # "[method='POST']")
        # postBox = driver.find_element_by_xpath(
        #     "//*[@aria-describedby='placeholder']/div/div/div/span")
        postBox = driver.find_element_by_xpath(
            "//*[contains(@aria-describedby,'placeholder')]/div/div/div/span")
        time.sleep(10)

        # attr = postBox.get_attribute("data-offset-key")

        postBox.send_keys(message[num])
        time.sleep(10)

        postButton = driver.find_element_by_xpath(
            "//*[text() = 'Post']")
        postButton.click()
        time.sleep(10)


#
#     time.sleep(5)
#     try:
#         driver.find_element(
#             By.XPATH, '//*[@aria-label="Create Post"]').click()
#         post_box = driver.find_element_by_css_selector(
#             "[name='xhpc_message_text']")
#     except:
#         post_box = driver.find_element_by_css_selector(
#             "[name='xhpc_message_text']")
#     post_box.send_keys(message)
#     time.sleep(1)
#     for photo in images_list:
#         photo_element = driver.find_element(
#             By.XPATH, '//input[@type="file"]')
#         photo_element.send_keys(photo)
#         time.sleep(1)
#     time.sleep(6)
#     post_button = driver.find_element_by_xpath(
#         "//*[@data-testid='react-composer-post-button']")
#     clickable = False
#     while not clickable:
#         cursor = post_button.find_element_by_tag_name(
#             'span').value_of_css_property("cursor")
#         if cursor == "pointer":
#             clickable = True
#         break
#     post_button.click()


if __name__ == '__main__':
    main()
