# Python standard library imports
from enum import Enum


class Category(Enum):
    RIFLE = 1
    HANDGUN = 2
    RIMFIRE = 3
    SHOTGUN = 4

    @staticmethod
    def extract(url):
        if "rifle" in url:
            return Category.RIFLE
        elif "hagle" in url:
            return Category.SHOTGUN
        elif "haandvaapen" in url or "handvapen" in url or "pistol" in url:
            return Category.HANDGUN
        elif "rimfire" in url:
            return Category.RIMFIRE
        else:
            raise ValueError("Category incorrect!")
