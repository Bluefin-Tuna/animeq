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

def scrape_manga_names(driver: webdriver = driver) -> List[list]:
    out = []
    for _ in range(1379):
        driver.get(f"https://manganato.com/genre-all/{_+1}?type=topview")
        url = driver.find_elements(By.CSS_SELECTOR, ".panel-content-genres .content-genres-item .genres-item-name")
        info = driver.find_elements(By.CSS_SELECTOR, ".panel-content-genres .content-genres-item .genres-item-view-time")
        if(len(url) != len(info)):
            print("Missalignment Found.")
        for i in range(min(len(url), len(info))):
            out.append([
                url[i].text, 
                info[i].find_element(By.CLASS_NAME, "genres-item-view").text,
                info[i].find_element(By.CLASS_NAME, "genres-item-time").text,
                info[i].find_element(By.CLASS_NAME, "genres-item-author").text,
                url[i].get_attribute("href"),
            ])
        if(_%10 == 0):
            save_manga_names(inp = out)
    return out

def save_manga_names(filename: str = "./data/manga.csv", inp: list = None) -> None:
    try:
        with open(filename, "w+") as f:
            f.write("Name|View Count|Last Updated|Author|URL\n")
            for _ in inp:
                f.write(f"{_[0]}|{_[1]}|{_[2]}|{_[3]}|{_[4]}\n")
    except Exception as e:
        print(e)

out = scrape_manga_names()
save_manga_names(inp = out)