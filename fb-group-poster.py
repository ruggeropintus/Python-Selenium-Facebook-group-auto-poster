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

# groupsLinkList = ["https://www.facebook.com/groups/44856655328/",
#                   "https://www.facebook.com/groups/kyivdancefestival/",
#                   "https://www.facebook.com/groups/144534108969160/",
#                   "https://www.facebook.com/groups/347114762374764/",
#                   "https://www.facebook.com/groups/1944377502498919/",
#                   "https://www.facebook.com/groups/132116430756891/",
#                   "https://www.facebook.com/groups/salserosMX/",
#                   "https://www.facebook.com/groups/DegeneracionSalsera/",
#                   "https://www.facebook.com/groups/salserospuertorico/",
#                   "https://www.facebook.com/groups/670549102968519/",
#                   "https://www.facebook.com/groups/704670606349104/",
#                   "https://www.facebook.com/groups/858604684276195/",
#                   "https://www.facebook.com/groups/176010239153184/",
#                   "https://www.facebook.com/groups/losgavilanessalseros/",
#                   "https://www.facebook.com/groups/rcastro",
#                   "https://www.facebook.com/groups/NORTHFLORIDASALCHATA/",
#                   "https://www.facebook.com/groups/820834947979865/",
#                   "https://www.facebook.com/groups/336963856330426/",
#                   "https://www.facebook.com/groups/217944685079429/",
#                   "https://www.facebook.com/groups/703998189624866/",
#                   "https://www.facebook.com/groups/SalserosMDP/",
#                   "https://www.facebook.com/groups/170173676659488/",
#                   "https://www.facebook.com/groups/200148068106666/",
#                   "https://www.facebook.com/groups/2324543681136804/"]

# groupsLinkList = ["https://www.facebook.com/groups/235527887015908/",
#                   "https://www.facebook.com/groups/1621444401514331/",
#                   "https://www.facebook.com/groups/576558082831600/",
#                   "https://www.facebook.com/groups/1454760514752946/",
#                   "https://www.facebook.com/groups/279905095365564/",
#                   "https://www.facebook.com/groups/328666513812147/",
#                   "https://www.facebook.com/groups/491367065099718/",
#                   "https://www.facebook.com/groups/salseridellabassaumidaromagna/",
#                   "https://www.facebook.com/groups/914437455422505/",
#                   "https://www.facebook.com/groups/1994946097311042/",
#                   "https://www.facebook.com/groups/brisbanesalsa/",
#                   "https://www.facebook.com/groups/296134790596411/",
#                   "https://www.facebook.com/groups/591007764276181/",
#                   "https://www.facebook.com/groups/BachataRemix/",
#                   "https://www.facebook.com/groups/1648382815414149/",
#                   "https://www.facebook.com/groups/283917041957185/",
#                   "https://www.facebook.com/groups/924741904353744/",
#                   "https://www.facebook.com/groups/phoenixbachata/",
#                   "https://www.facebook.com/groups/193942994102543/",
#                   "https://www.facebook.com/groups/472784476744580/",
#                   "https://www.facebook.com/groups/salserosybachaterosdesantiagodechile/",
#                   "https://www.facebook.com/groups/CaliSalsa/",
#                   "https://www.facebook.com/groups/487581634703255/",
#                   "https://www.facebook.com/groups/814253035334304/"]


# groupsLinkList = ["https://www.facebook.com/groups/117502368342838/",
#                   "https://www.facebook.com/groups/2077931098903786/",
#                   "https://www.facebook.com/groups/bachatadanceacademy/",
#                   "facebook.com/groups/163041610457990/",
#                   "https://www.facebook.com/groups/290755017666726/",
#                   "https://www.facebook.com/groups/SydneyBachata/",
#                   "https://www.facebook.com/groups/438329236209409/",
#                   "https://www.facebook.com/groups/176145122510771/",
#                   "https://www.facebook.com/groups/123246504498945/"]

# groupsLinkList = ["https://www.facebook.com/groups/120276918610382/",
#                   "https://www.facebook.com/groups/ExodehardcoreSharing/",
#                   "https://www.facebook.com/groups/876308409439219/",
#                   "https://www.facebook.com/groups/593906064787633/",
#                   "https://www.facebook.com/groups/TheAnnihilationProject/",
#                   "https://www.facebook.com/groups/2140010692951821/"]


# groupsLinkList = ["https://www.facebook.com/groups/1657928417808333/",
#                   "https://www.facebook.com/groups/111463475532259/",
#                   "https://www.facebook.com/groups/15359527623/",
#                   "https://www.facebook.com/groups/1450122935247497/",
#                   "https://www.facebook.com/groups/UKCSalsaSoc/",
#                   "https://www.facebook.com/groups/CambridgeCubanSalsa/",
#                   "https://www.facebook.com/groups/312987445412767/",
#                   "https://www.facebook.com/groups/viennasalsaevents/",
#                   "https://www.facebook.com/groups/1073439109364813/",
#                   "https://www.facebook.com/groups/FollowLeandro/",
#                   "https://www.facebook.com/groups/salsabachatakizombavideos/",
#                   "https://www.facebook.com/groups/397975036935975/",
#                   "https://www.facebook.com/groups/LeedsSalsa/",
#                   "https://www.facebook.com/groups/869664896782753/"]

groupsLinkList = ["https://www.facebook.com/groups/1980640592165531/",
                  "https://www.facebook.com/groups/233907926802227/",
                  "https://www.facebook.com/groups/106803783508170/",
                  "https://www.facebook.com/groups/djsallover/",
                  "https://www.facebook.com/groups/108947492513974/",
                  "https://www.facebook.com/groups/111756225565727/",
                  "https://www.facebook.com/groups/176323882527718/",
                  "https://www.facebook.com/groups/1922629534667190/",
                  "https://www.facebook.com/groups/ambient.downtempo.electronica/",
                  "https://www.facebook.com/groups/257776851910360/"]


def main():
    # Insert here credentials and groups

    message = ['"Baila!!! Pa olvidar las penas"\n'
               'https://www.mixcloud.com/ruggero-pintus/salsa-bachata-kizomba-semba-party-mix-vol-5/\n'
               'Salsa Bachata Kizomba Semba Party Mix Vol 5\n'
               '^ ^ ^ click on the link above to listen ^ ^ ^\n'
               '\n'
               'The mix features tracks from Gilberto Santa Rosa, Alexander Abreu, Calema, N\'klabe, Rafaelito y su Tumbao, Mago de Sousa, Dj Khalid, Dj T - Wave, Dani J, Toby Love, Loony Johnson, Soraia Ramos, Punidor, Havana D\' Primera, Zoe Wees, Tito Rojas, Andy Montañez, Mr.Don\n'
               '\n'
               'Follow me on:\n'
               'Facebook https://www.facebook.com/djr2official/\n'
               'Instagram https://www.instagram.com/djr2music\n'
               'Twitter https://twitter.com/DjR2_artu\n'
               'Spotify https://open.spotify.com/user/21kesygo356dgcay2xmimzlaq\n'
               '\n'
               '#stayhome #quarantine #stayathome #gilbertosantarosa #AlexanderAbreu #Calema #Nklabe #rafaelitoysutumbao #magodesousa #djkhalid #djtwave #danij #tobylove #loonyjohnson #SoraiaRamos #Punidor #havanadeprimera #ZoeWees #TitoRojas #andymontañez #MrDon\n'
               '\n'
               'https://www.facebook.com/djr2official/posts/462189485173535 ']

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

        print("Posting message in group: ", group,
              " (", num + 1, "/", len(groupsLinkList), ")")
        try:
            driver.get(group)
        except:
            continue

        time.sleep(20)

        try:
            aaa = driver.find_element_by_xpath(
                '//*[ @ id = "mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span')
        except:
            continue

        time.sleep(5)

        try:
            aaa.click()
        except:
            continue

        time.sleep(20)

        try:
            postBox = driver.find_element_by_xpath(
                "//*[contains(@aria-describedby,'placeholder')]/div/div/div/span")
        except:
            continue

        time.sleep(5)

        try:
            postBox.send_keys(message[0])
        except:
            continue

        time.sleep(30)

        try:
            postButton = driver.find_element_by_xpath("//*[text() = 'Post']")
        except:
            continue

        time.sleep(5)

        try:
            postButton.click()
        except:
            continue
        time.sleep(1115)


if __name__ == '__main__':
    main()
