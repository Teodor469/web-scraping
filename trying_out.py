import requests

url = "https://trafficnews.bg/"
response = requests.get(url)

while response.status_code == 200:
    print("Request successful")
    print(response.text)
else:
    print(f"Request failed: {response.status_code}")