import requests
from bs4 import BeautifulSoup

from ammo_finder.core.category import Category
from ammo_finder.core.product import Product

from ammo_finder.core.logger import get_logger
from ammo_finder.core.price import extract_price

logger = get_logger("Skittjakt")


class SkittjaktScraper(object):

    def __init__(self):
        self.root_url = "https://www.skittjakt.no/ammunisjon/"
        self.prefix_url = "https://www.skittjakt.no/"

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
            logger.info(f"Extracting from url: {url}")
            compounded_url = f"{self.root_url}{url}"

            response = requests.get(compounded_url)

            soup = BeautifulSoup(response.content, "html.parser")

            data = soup.find_all("div", class_="Layout3Element")

            for div in data:
                try:
                    product_div = div.find("div", class_="AddProductImage")
                    details_url = self.prefix_url + product_div.find("a")["href"]
                    image_url = extract_attribute_value(self.prefix_url, div, "data-original", "lazy")

                    name = extract_attribute_value(self.prefix_url, div, "title", "lazy")
                    price_raw = div.find("span", class_="AddPriceLabel").text
                    price = extract_price(price_raw)

                    product = Product(
                        cat=Category.extract(compounded_url),
                        img_url=image_url,
                        name=f"{name}",
                        details_url=details_url,
                        price=price
                    )
                    elements.append(product)
                except AttributeError as e:
                    logger.error(f"Failed to extract data: {e} at url: {compounded_url}")

        return elements


def extract_attribute_value(prefix, div, attribute="data-original", class_="nothing"):
    image = div.find("img", class_=class_)
    if image:
        return prefix + image[attribute]
    else:
        return None

