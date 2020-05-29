class JaktDepotetScraper(object):
    def __init__(self):
        self.root_url = "https://www.jaktdepotet.no/ammunisjon"
        self.urls = [
            "haglepatroner",
            "riflepatroner",
            "salongriflepatroner",
            "pistol-revolver"
        ]

    def fetch(self):
        pass