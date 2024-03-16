import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def scrape_main_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    items = soup.find_all('div', class_='thumbnail')
    return items

def scrape_category_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    items = soup.find_all('div', class_='thumbnail')
    return items

def items_to_dataframe(items):
    data = []
    for item in items:
        data.append(item.get_text())

    df = pd.DataFrame(data, columns=['Item Details'])
    return df

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def main():
    main_url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    main_items = scrape_main_page(main_url)
    main_df = items_to_dataframe(main_items)
    save_to_csv(main_df, 'main_page_items.csv')

    categories = ['computers', 'phones', 'monitors']
    for category in categories:
        category_url = f'{main_url}/category/{category}'
        category_items = scrape_category_page(category_url)
        category_df = items_to_dataframe(category_items)
        save_to_csv(category_df, f'{category}_items.csv')

if __name__ == '__main__':
    main()
