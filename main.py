from scrape.pvas_scraper import PvasScraper

pvas = PvasScraper()

result = pvas.fetch()

for el in result:
    print(el)