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


groupsLinkList = ["https://www.facebook.com/groups/2140010692951821/",
                  "https://www.facebook.com/groups/TheAnnihilationProject/",
                  "https://www.facebook.com/groups/593906064787633/",
                  "https://www.facebook.com/groups/876308409439219/",
                  "https://www.facebook.com/groups/120276918610382/",
                  "https://www.facebook.com/groups/869664896782753/",
                  "https://www.facebook.com/groups/233907926802227/",
                  "https://www.facebook.com/groups/djsallover/",
                  "https://www.facebook.com/groups/108947492513974/",
                  "https://www.facebook.com/groups/176323882527718/",
                  "https://www.facebook.com/groups/1922629534667190/",
                  "https://www.facebook.com/groups/ambient.downtempo.electronica/",
                  "https://www.facebook.com/groups/257776851910360/",
                  "https://www.facebook.com/groups/183644435504146/",
                  "https://www.facebook.com/groups/559936830787046/",
                  "https://www.facebook.com/groups/trackmixeventshare/",
                  "https://www.facebook.com/groups/shareyourmusicwithfriends/",
                  "https://www.facebook.com/groups/359414134260746/",
                  "https://www.facebook.com/groups/929968170391687/",
                  "https://www.facebook.com/groups/1027818457589063/",
                  "https://www.facebook.com/groups/Promoteshareyourmusic/",
                  "https://www.facebook.com/groups/225845574908476/",
                  "https://www.facebook.com/groups/929610450791590/",
                  "https://www.facebook.com/groups/listentofreemusic/"]

DEBUG = False


def main():
    # Insert here credentials and groups

    message = ['Some music from the last months\' charts\n'
               'https://www.mixcloud.com/ruggero-pintus/salsa-bachata-kizomba-semba-party-mix-vol-6/\n'
               'Salsa Bachata Kizomba Semba Party Mix Vol 6\n'
               '^ ^ ^ click on the link above to listen ^ ^ ^\n'
               '\n'
               'The mix features tracks from Havana D´ Primera & Alexander Abreu, La Excelencia, Camilo & El Alfa, KHEA, Natti Natasha, Prince Royce, Lenny Santos, C4 pedro, Maya Cool, Daddy Yankee, Marc Anthony, Calle Vapor, Jeyro, Grupo Extra, Josslyn, Rui Orlando, and Anderson Mário.\n'
               '\n'
               'Follow me on:\n'
               'Facebook https://www.facebook.com/djr2official/\n'
               'Instagram https://www.instagram.com/djr2music\n'
               'Twitter https://twitter.com/DjR2_artu\n'
               'Spotify https://open.spotify.com/user/21kesygo356dgcay2xmimzlaq\n'
               '\n'
               '#havanadeprimera #AlexanderAbreu #LaExcelencia #Camilo #elalfaeljefe #khea #nattinatasha #princeroyce #lennysantos #C4Pedro #mayacool #daddyyankee #MarcAnthony #CalleVapor #Jeyro #GrupoExtra #josslyn #RuiOrlando #AndersonMario\n'
               '\n'
               'https://www.facebook.com/djr2official/posts/631703791555436 ']

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
    time.sleep(2)
    acceptAllElement = driver.find_element(
        By.XPATH, '//*[@data-testid="cookie-policy-dialog-manage-button"]')
    acceptAllElement.click()
    time.sleep(2)
    acceptCookies = driver.find_element(
        By.XPATH, '//*[@data-testid="cookie-policy-manage-dialog-accept-button"]')
    acceptCookies.click()


def login(driver, account, password):
    emailElement = driver.find_element(
        By.XPATH, '//*[@id="' + emailElementID + '"]')
    emailElement.send_keys(account)
    time.sleep(2)

    passElement = driver.find_element(
        By.XPATH, '//*[@id="' + passElementID + '"]')
    passElement.send_keys(password)
    time.sleep(2)

    loginElement = driver.find_element(
        By.XPATH, '//*[@data-testid="' + loginElementID + '"]')
    loginElement.click()

    time.sleep(20) if not DEBUG else time.sleep(5)


def postInGroups(driver, groupsLinkList, message, imagesList):
    for num, group in enumerate(groupsLinkList):

        print("Posting message in group: ", group,
              " (", num + 1, "/", len(groupsLinkList), ")")
        try:
            driver.get(group)
        except:
            print("----- FAILED!!!! -----")
            continue

        time.sleep(20) if not DEBUG else time.sleep(5)

        print("aaa - find")
        try:
            aaa = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span')
            # aaa = driver.find_element_by_xpath(
            #     '//*[ @ id = "mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span')

        except:
            print("----- FAILED!!!! -----")
            continue

        time.sleep(5)

        print("aaa - click")
        try:
            aaa.click()
        except:
            print("----- FAILED!!!! -----")
            continue

        time.sleep(20) if not DEBUG else time.sleep(5)

        print("postBox - find")
        try:
            postBox = driver.find_element_by_xpath(
                "//*[contains(@aria-describedby,'placeholder')]/div/div/div/span")
        except:
            print("----- FAILED!!!! -----")
            continue

        time.sleep(5)

        print("postBox - send message")
        try:
            postBox.send_keys(message[0])
        except:
            print("----- FAILED!!!! -----")
            continue

        time.sleep(30) if not DEBUG else time.sleep(5)

        print("postButton - find")
        try:
            postButton = driver.find_element_by_xpath("//*[text() = 'Post']")
        except:
            print("----- FAILED!!!! -----")
            continue

        time.sleep(5)

        print("postButton - click")
        try:
            postButton.click()
        except:
            print("----- FAILED!!!! -----")
            continue
        time.sleep(1115)


if __name__ == '__main__':
    main()
