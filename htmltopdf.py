import os
from selenium import webdriver
import json


actual_dir = os.path.dirname(__file__)
download_dir = "pdf"
download_dir2 = os.path.join(actual_dir, download_dir)


chrome_options = webdriver.ChromeOptions()
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
prefs = {
    "printing.print_preview_sticky_settings.appState": json.dumps(settings),
    "savefile.default_directory": download_dir2
}
chrome_options.add_experimental_option('prefs', prefs)

chrome_options.add_argument('--kiosk-printing')
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER_PATH)
driver.get("https://google.com")
driver.execute_script('window.print();')
driver.quit()