# Python standard library imports
from sys import stderr
import typing

# Non-standard library python package imports
from bs4 import BeautifulSoup
import requests

# Internal module package imports
from ammo_finder.core.category import Category
from ammo_finder.core.product import Product


PVAS_ROOT_URL = 'https://www.pvas.no'
PRODUCT_CONTEXT_PATHS = (
    'produkter/ammunisjon/rifle',
    'produkter/ammunisjon/hagle',
    'produkter/ammunisjon/haandvaapen',
    'produkter/ammunisjon/rimfire',
)


class PvasProduct(Product):
    pass


class PvasScraper(object):
    def fetch(self):
        results = [
            ammunition_info
            for product_context_path
            in PRODUCT_CONTEXT_PATHS
            for ammunition_info
            in fetch_pvas_ammo_by_weapon_category(
                category_url_context_path=product_context_path,
            )
        ]
        return results


def fetch_pvas_ammo_by_weapon_category(
    category_url_context_path: str,
    *,
    root_url: str=PVAS_ROOT_URL,
) -> typing.List[PvasProduct]:
    """
    Collate a list all ammunition subproducts found within the scraped results
    of a weapon category's ammunition products `f"{root_url}/{category_url_context_path}"`.
    """
    compounded_url = f"{root_url}/{category_url_context_path}"
    print(f"Fetching data @ {compounded_url}", file=stderr)
    response = requests.get(compounded_url)

    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all("div", class_="ProdItem")

    list_of_ammo_types = get_ammunition_specific_data_from_html(
        html=data,
        category=Category.extract(compounded_url),
    )
    print(f"\t{len(list_of_ammo_types)} found!", file=stderr)
    return list_of_ammo_types


def get_ammunition_specific_data_from_html(
    html: typing.Dict,
    category: Category,
    *,
    root_url: str=PVAS_ROOT_URL,
) -> typing.List[PvasProduct]:
    result_list = list()
    for container in html:
        image_link = container.find("img")["src"]
        name = container.find("a", class_="ItemTitleLink")["title"]
        details_url = container.find("a", class_="ItemTitleLink")["href"]
        price_string = container.find("span", class_="Price").text

        result_list.append(
            PvasProduct(
                cat=category,
                img_url=f"{root_url}{image_link}",
                price=price_string,
                name=name,
                details_url=details_url,
            )
        )
    return result_list
