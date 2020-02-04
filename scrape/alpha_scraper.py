from bs4 import BeautifulSoup
import requests

from core.category import Category
from core.product import Product




class AlphaScraper(object):

    def __init__(self):
        self.root_url = "https://www.2alfa.no/ammunisjon/ladet-ammo"
        self.urls = ["/rifle.html", "/pistol.html"]


    def fetch(self):
        elements = []
        for url in self.urls:
            compounded_url = f"{self.root_url}{url}"
            # print(f"Fetching data @ {compounded_url}")
            response = requests.get(compounded_url)

            # 2Alpha has a bit more cryptioc site setup
            soup = BeautifulSoup(response.content, "html.parser")
            data = soup.find_all("div", class_="ut2-gl__body")

            for container in data:
                # Extract image info
                image_div = container.find("div", class_="ut2-gl__image")

                image_url = image_div.find("img", class_="ty-pict")["src"]

                # Get the first anchor which has the details link
                details_url = image_div.find("a")["href"]

                # Extract name
                name_div = container.find("div", class_="ut2-gl__name")
                name = name_div.find("a")["title"]

                # Extract price
                price_div = container.find("div", class_="ut2-gl__price")
                price_str = price_div.find("span", class_="ty-price-num").text

                product = Product(
                    cat = Category.extract(compounded_url),
                    img_url = image_url,
                    price = price_str,
                    name = name,
                    details_url = details_url
                )
                elements.append(product)
        return elements                



