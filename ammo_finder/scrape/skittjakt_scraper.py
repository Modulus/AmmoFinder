import requests
from bs4 import BeautifulSoup


class SkittjaktScraper(object):
    def __init__(self):
        self.root_url = "https://www.skittjakt.no/ammunisjon/"
        self.urls = [
            "salong",
            "hagle",
            "handvapen",
            "luftvapen"
            "rifle"
        ]

    def fetch(self):
        elements = []
        for url in self.urls:
            compounded_url = f"{self.root_url}{self.url}"

            response = requests.get(compounded_url)

            soup = BeautifulSoup(response.content, "html.parser")

            data = soup.find_all("div", class_="AddProductImage")

            for div in data:
                details_url = div.find("a")["href"]
                image_url = div.find("img", class_="lazy")