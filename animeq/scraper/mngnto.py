from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def scrape_manga_names(driver: webdriver = None) -> List[list]:
    
    assert isinstance(driver, webdriver), "Driver should be defined as a webdriver."
    
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
