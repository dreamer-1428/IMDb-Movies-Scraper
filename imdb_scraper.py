from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.imdb.com/chart/top/")
time.sleep(5)

from selenium.webdriver.common.by import By
movies = []
movie_elements = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

for movie in movie_elements[:10]:
    title = movie.find_element(By.CSS_SELECTOR, "h3").text
    rating = movie.find_element(By.CSS_SELECTOR, "span[aria-label^='IMDb rating']").text
    movies.append({"Title": title, "Rating": rating})

df = pd.DataFrame(movies)
df.to_csv("imdb_top_movies.csv", index=False)
print("Data saved to imdb_top_movies.csv!")

driver.quit()

print("Page loaded successfully!")
driver.quit()
