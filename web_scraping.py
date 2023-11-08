from bs4 import BeautifulSoup
import requests

# Make a GET request to the webpage
url = "https://trafficnews.bg/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    doc = BeautifulSoup(response.text, "html.parser")

    # Find all "h3" headings on the page
    h3_headings = doc.find_all("h3")

    # Extract and print the text of each "h3" heading
    for h3 in h3_headings:
        print(h3.get_text())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
