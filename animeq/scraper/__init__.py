from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def create_driver(dir: str = "/home/tanush/Programming/Projects/animeq/animeq/scraper/chromedriver") -> webdriver:

    options = Options()
    options.add_argument("--headless")

    return webdriver.Chrome(dir, options = options)