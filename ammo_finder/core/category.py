# Python standard library imports
from enum import Enum


class Category(Enum):
    RIFLE = 1
    HANDGUN = 2
    RIMFIRE = 3
    SHOTGUN = 4
    AIR = 5

    @staticmethod
    def extract(url):
        if "rifle" in url:
            return Category.RIFLE
        elif "hagle" in url:
            return Category.SHOTGUN
        elif "haandvaapen" in url or "handvapen" in url or "pistol" in url:
            return Category.HANDGUN
        elif "rimfire" in url or "22lr" in url or "salong" in url:
            return Category.RIMFIRE
        elif "air" in url or "luft" in url or "luftvapen" in url:
            return Category.AIR
        else:
            raise ValueError("Category incorrect!")
