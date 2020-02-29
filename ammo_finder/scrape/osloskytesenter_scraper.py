from bs4 import BeautifulSoup
import requests

from ammo_finder.core.category import Category
from ammo_finder.core.product import Product


class OsloskytesenterScraper(object):

    def __init__():
        self.root_url = "https://osloskytesenter.no/"
        self.urls = [
            "/produktkategori/ammunisjon-kassesalg/",
            "/produktkategori/ammunisjon/22lr-og-salongpatroner/",
            "/produktkategori/ammunisjon/haglepatroner/",
            "/produktkategori/ammunisjon/handvapenpatroner/",
            "/produktkategori/ammunisjon/riflepatroner/"
            ]
