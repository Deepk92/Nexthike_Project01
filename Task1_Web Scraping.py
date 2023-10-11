# First import the BeautifulSoup and the requests library

from bs4 import BeautifulSoup
import requests

# Define the URL to scrape

url = "https://www.python.org/"

# Send an HTTP get request

response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the elements you want to scrape (articles)

    articles = soup.select(".blog-widget li")

    # Create a text file and write the scraped content to it

    with open("scrap.txt", "w", encoding="utf-8") as f:
        for article in articles:
            title = article.a.text.strip()
            f.write(title + "\n")
    print("Data Scrapped and Saved to scrap.txt")

else:
    print("Failed to retrieve the data from the website")





