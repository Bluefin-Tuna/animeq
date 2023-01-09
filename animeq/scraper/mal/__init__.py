from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from animeq.scraper.mal.data_processing import *
from animeq.scraper.mal.scrapers import *
from animeq.scraper import create_driver

def scrape_url_mal(ex, url, driver: webdriver = None) -> List[list]:
    
    NUM_MAL_ANIME = 22300
    ANIME_PER_SITE = 50
    SITE = "https://myanimelist.net/topanime.php"
    
    for i in range(0, NUM_MAL_ANIME, ANIME_PER_SITE):
        p = []
        try:
            driver.get(f"{SITE}?limit={i}")
            animes = driver.find_elements(By.CLASS_NAME, "ranking-list")
            p = []
            for j, a in enumerate(animes):
                _ = a.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/table/tbody/tr[{j+2}]/td[2]/div/div[2]/h3/a')
                url.append(_.get_attribute("href"))
                p.append(_.get_attribute("href"))
        except KeyboardInterrupt as e:
            return ex, url
        except Exception as err:
            if(len(p) < 45):
                ex.append(i)
            return ex, url
  
    return ex, url

def scrape_page_mal(URL: str, driver: webdriver = None):
    
    driver.get(URL)
    out = {}
    
    name = scrape_name(driver)
    summary = scrape_summary(driver)
    information = scrape_information(driver)
    reviews = scrape_reviews(driver)
    relations = scrape_relations(driver)
    statistics = scrape_statistics(driver)

    return statistics, information, summary, reviews, relations

scrape_url = scrape_url_mal
scrape_page = scrape_page_mal

statistics, information, summary, reviews, relations = scrape_page_mal(URL = "https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood", driver = create_driver())
print(statistics)
print("\n")
print(information)
print("\n")
print(summary)
print("\n")
print(reviews)
print("\n")
print(relations)

import re
print(re.search(r"[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+", "9090 (scored by - users)"))