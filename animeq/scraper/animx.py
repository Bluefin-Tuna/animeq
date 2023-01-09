from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def scrape_anime_names(source_all: str = "https://animixplay.to/list", driver: webdriver = None) -> List[list]:

    assert isinstance(driver, webdriver), "Driver should be defined as a webdriver."

    driver.get(source_all)
    bw = driver.find_element(By.ID, "alphabetical")
    buttons = bw.find_elements(By.TAG_NAME, "button")
    out = []
    for b in buttons:
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