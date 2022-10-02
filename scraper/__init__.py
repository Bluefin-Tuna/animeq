import requests
from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome("/home/tanush/Programming/Projects/animeq/scraper/chromedriver", options = options)

def scrape_anime_names(source_all: str = "https://animixplay.to/list", driver: webdriver = driver) -> List[list]:
    driver.get(source_all)
    bw = driver.find_element(By.ID, "alphabetical")
    buttons = bw.find_elements(By.TAG_NAME, "button")
    out = []
    for b in buttons:
        time.sleep(0.5)
        b.click()
        _list = driver.find_element(By.ID, "listplace")
        _wrapper = _list.find_elements(By.CLASS_NAME, "allitem")
        for i, w in enumerate(_wrapper):
            _ = w.text.split("\n")
            _.append(w.find_element(By.TAG_NAME, "a").get_attribute("href"))
            out.append(_)
    return out

def save_anime_names(filename: str = "./data/anime.csv", inp: list = None) -> None:
    try:
        with open(filename, "w+") as f:
            f.write("Name,Source,URL\n")
            for _ in inp:
                f.write(f"{_[0]},{_[1]},{_[2]}\n")
    except Exception as e:
        print(e)
            
    # for i in _list:
    #     print(i)
    # soup = BeautifulSoup(page.content, parser)
    # print(soup.prettify())

def scrape_manga_names():
    try:
        pass
    except:
        pass

# def cross_reference():

# def scrape_anime(name):



# def scrape_manga(name):

out = scrape_anime_names()
save_anime_names(inp = out)