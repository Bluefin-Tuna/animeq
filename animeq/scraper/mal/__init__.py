from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from animeq.scraper.mal.data_processing import *
from animeq.scraper.mal.scrapers import *
from animeq.scraper import create_driver

def scrape_url_mal(ex, url, driver: webdriver = None) -> List[list]:
    
    # assert isinstance(driver, webdriver), "Driver should be defined as a webdriver."

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

def scrape_page_mal(URL: str, driver: webdriver = None) -> dict:
    
    # assert isinstance(driver, webdriver), "Driver should be defined as a webdriver."
    
    driver.get(URL)

    return scrape_name(driver), scrape_summary(driver), scrape_information(driver), scrape_reviews(driver), scrape_relations(driver), scrape_statistics(driver)

def scrape_pages_mal(driver: webdriver = None, file: str = "animeq/data/anime.csv"):

    # assert isinstance(driver, webdriver), "Driver should be defined as a webdriver."

    of = open("mal.tsv", "w")
    f = open(file, 'r')
    for l in f.readlines():
        l = l.split(",")
        NAME = ",".join(l[0: len(l) - 2])
        URL = l[-1]
        try:
            name, summary, info, rev, rel, stat = scrape_page_mal(URL, driver)
            of.write(f"{NAME}\t{URL}\t{name}\t{summary}\t{info}\t{rev}\t{rel}\t{stat}\n")
        except Exception as e:
            print(e)

# scrape_url = scrape_url_mal
# scrape_page = scrape_page_mal

# scrape_pages_mal(driver= create_driver())

scraper = create_driver()
e = scraper.find_element(By.XPATH, "/html/body/div/div/main/div/div/div[4]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/article").text
print(e)