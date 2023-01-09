from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By

def identity(i):
    return i

def scrape_name(driver: webdriver, func = identity) -> str:
    
    name = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/div/h1").text
    name = func(name)
    
    return name

def scrape_information(driver: webdriver, func = identity) -> List[tuple]:

    info = [tuple(driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[{i}]").text.split(":")) for i in range(11, 25)]
    info = func(info)

    return info

def scrape_summary(driver: webdriver, func = identity):

    summary = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/p").text
    summary = func(summary)

    return summary

def scrape_statistics(driver: webdriver, func = identity):

    statistics = [tuple(driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[{i}]").text.split(":")) for i in range(25, 30)]
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/div[2]/ul/li[5]/a").click()
    statistics = statistics + [tuple(driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/div[{i}]").text.split(":")) for i in range(4, 9)]

    return statistics

def scrape_reviews(driver: webdriver, func = identity):

    _review_tag = driver.find_elements(By.CSS_SELECTOR, ".review-element .thumbbody .body .tags .tag.btn-label")
    _review_pop = driver.find_elements(By.CSS_SELECTOR, ".review-element .thumbbody .body .bottom-navi .icon-reaction")
    _review_tag = [rt.get_attribute("data-id") for rt in _review_tag]
    _review_pop = [rp.text for rp in _review_pop]
    
    reviews = list(zip(_review_tag, _review_pop))
    reviews = func(reviews)

    return reviews

def scrape_relations(driver: webdriver, func = identity):

    relations = []
    for i in range(1, 5):
        t1 = driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[3]/td/table/tbody/tr[{i}]/td[1]").text
        t2 = driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[3]/td/table/tbody/tr[{i}]/td[2]").find_elements(By.TAG_NAME, "a")
        hrf = [_.get_attribute("href") for _ in t2]
        relations.append((t1, hrf))
    relations = func(relations)

    return relations