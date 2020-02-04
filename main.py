from scrape.pvas_scraper import PvasScraper
from scrape.alpha_scraper import AlphaScraper

pvas = PvasScraper()

result = pvas.fetch()

for el in result:
    print(el)


print(f"Found {len(result)} ammo types from pvas.no")    

alpha = AlphaScraper()

result = alpha.fetch()
for el in result:
    print(el)

print(f"Found {len(result)} ammo types from 2alpha.no")        