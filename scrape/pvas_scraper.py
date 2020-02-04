from bs4 import BeautifulSoup
import requests

from core.category import Category
from core.product import Product


root_url = "https://www.pvas.no"
urls = ["/produkter/ammunisjon/rifle", "/produkter/ammunisjon/hagle", "/produkter/ammunisjon/haandvaapen", "/produkter/ammunisjon/rimfire"]

class PvasScraper(object):

   
    def fetch(self):
        elements = []
        for url in urls:
            compounded_url = f"{root_url}{url}"
            print(f"Fetching data @ {compounded_url}")
            response = requests.get(compounded_url)

            soup = BeautifulSoup(response.content, "html.parser")

            data = soup.find_all("div", class_="ProdItem")



            for container in data:
                # print(container)
                image_link = container.find("img")["src"]
                # print(image_link)
                name = container.find("a", class_="ItemTitleLink")["title"]
                # print(title)
                details_url = container.find("a", class_="ItemTitleLink")["href"]
                # print(title_link)
                price_string = container.find("span", class_="Price").text
                # print(price_string)


                product = Product(
                    cat = Category.extract(compounded_url), 
                    img_url = f"{root_url}{image_link}",
                    price = price_string,
                    name = name,
                    details_url = details_url
                    )

          
                elements.append(product)

        return elements

