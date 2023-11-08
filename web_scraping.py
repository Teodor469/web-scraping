from bs4 import BeautifulSoup
import requests

url = "https://trafficnews.bg/plovdiv/"
response = requests.get(url)

if response.status_code == 200:
    doc = BeautifulSoup(response.text, "html.parser")

    h3_headings = doc.find_all("h3")

    for h3 in h3_headings:
        print(h3.get_text())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

#later for that project I would like to make it so it gives you all the new articles within 24 hours