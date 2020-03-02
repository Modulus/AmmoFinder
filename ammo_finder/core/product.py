# Python standard library imports
import json

# Internal module package imports
from ammo_finder.core.category import Category


class Product(object):
    def __init__(self, cat, img_url, name, details_url, price):
        self.category = cat
        self.img_url = img_url
        self.name = name
        self.details_url = details_url
        self.price = price

    def get_dict(self):
        return {
            "category" : str(self.category),
            "img_url" : self.img_url,
            "name" : self.name,
            "details_url" : self.details_url,
            "price": self.price,
        }

    def __repr__(self):
        return str(json.dumps(self.get_dict()))

    def __str__(self):
        return str(json.dumps(self.get_dict()))

    # def __str__(self):
    #     return f"Category: {self.category}"
