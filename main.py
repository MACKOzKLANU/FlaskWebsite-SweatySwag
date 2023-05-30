import requests
from bs4 import BeautifulSoup
import pandas as pd
 
url = "https://sweatyswag.pl"
response = requests.get(url)
 
soup = BeautifulSoup(response.content, "html.parser")
 
items = soup.find_all("li", {"class" : "grid__item"})
 
# print(items)
print(items)
 
results = []

for item in items:
    gif = item.find("a", {"class" : "header__heading-link link link--text focus-inset"})
    imageURLl = item.find("img", {"class" : "motion-reduce"})
    imageURL = imageURLl.get("src")
    title = item.find("a", {"class" : "full-unstyled-link"}).text.strip()
    views = item.find("span",{"class" : "price-item price-item--regular"}).text.strip()
    # views = "".join(filter(str.isdigit, views))
 
    result = {
        "imageURL" : imageURL,
        "title" : title,
        "views" : views
    }
 
    results.append(result)
 
df = pd.DataFrame(results)
 
df.to_csv("sweaty.csv", index = False)