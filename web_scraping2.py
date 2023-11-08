from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

url = "https://trafficnews.bg/plovdiv/"
response = requests.get(url)

if response.status_code == 200:
    doc = BeautifulSoup(response.text, "html.parser")

    article_elements = doc.find_all("article", class_="col-4 relative")

    current_time = datetime.now()
    time_window = timedelta(hours=24)

    for article in article_elements:
        publication_date_text = article.find("span", class_="time").get_text()

        publication_date = datetime.strptime(publication_date_text, "%H:%M")
        publication_datetime = current_time.replace(hour=publication_date.hour, minute=publication_date.minute)
        time_difference = current_time - publication_datetime

        if time_difference <= time_window:
            article_title = article.find("h3").get_text()
            article_link = article.find("a", href=True)["href"]
            print("Article Title:", article_title)
            print("Article Link:", article_link)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
