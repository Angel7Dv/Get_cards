# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


web = "https://www.adamchoi.co.uk/teamgoals/detailed"

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(web)
