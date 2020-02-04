from bs4 import BeautifulSoup
import requests

from core.category import Category
from core.product import Product


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