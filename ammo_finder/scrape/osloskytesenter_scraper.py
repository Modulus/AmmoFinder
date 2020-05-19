# Non-standard library python package imports
from bs4 import BeautifulSoup
import requests

# Internal module package imports
from ammo_finder.core.category import Category
from ammo_finder.core.product import Product


class OsloskytesenterScraper(object):

    def __init__(self):
        self.root_url = "https://osloskytesenter.no/"
        self.urls = [
            # "/produktkategori/ammunisjon-kassesalg/",
            "/produktkategori/ammunisjon/22lr-og-salongpatroner/",
            "/produktkategori/ammunisjon/haglepatroner/",
            "/produktkategori/ammunisjon/handvapenpatroner/",
            "/produktkategori/ammunisjon/riflepatroner/"
            ]

    def fetch(self):

        products = set()
        for url in self.urls:
            compounded_url = f"{self.root_url}{url}"
            response = requests.get(compounded_url)

            soup = BeautifulSoup(response.content, "html.parser")
            all_links = soup.find_all("a", class_="woocommerce-LoopProduct-link")
            category = Category.extract(url)

            for link in all_links:
                name = link.find("h2", class_="woocommerce-loop-product__title").text
                image_link = link.find("img")["src"]
                # price_string = link.find("span", class_="woocommerce-Price-currencySymbol")

                # TODO: Fix price string
                # currency = link.find("span", class_="woocommerce-Price-currencySymbol")
                try:
                    price_string = link.find("span", class_="woocommerce-Price-amount amount").text
                except AttributeError as e:
                    price_string = None
                    print("Failed to extract price")
                details_url = link["href"]
                print(price_string)
                products.add(
                    Product(cat=category,
                            img_url=f"{image_link}",
                            price=price_string,
                            name=name,
                            details_url=details_url
                            )
                )

        return products








