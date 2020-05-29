#!/usr/bin/env python3

# Internal module package imports
from ammo_finder.scrape.alpha_scraper import AlphaScraper
from ammo_finder.scrape.pvas_scraper import PvasScraper
from ammo_finder.scrape.osloskytesenter_scraper import OsloskytesenterScraper
from ammo_finder.scrape.skittjakt_scraper import SkittjaktScraper


## DO NOT MOVE THIS, this is just for testing this app is not a console application!!!!

if __name__ == "__main__":
    # pvas_scraper = PvasScraper()
    # pvas_results = pvas_scraper.fetch()
    #
    # # for el in pvas_results:
    # #     print(el)
    #
    # print(f"Found {len(pvas_results)} ammo types from pvas.no")
    #
    # alpha = AlphaScraper()
    # alpha_results = alpha.fetch()
    #
    # # for el in alpha_results:
    # #     print(el)
    #
    # print(f"Found {len(alpha_results)} ammo types from 2alpha.no")
    # oslo = OsloskytesenterScraper()
    # oslo_results = oslo.fetch()
    #
    # # for el in alpha_results:
    # #     print(el)
    #
    # print(f"Found {len(oslo_results)} ammo types from 2alpha.no")
    # for el in oslo_results:
    #     print(el)


    skitt = SkittjaktScraper()
    skitt_results = skitt.fetch()

    # for el in alpha_results:
    #     print(el)

    print(f"Found {len(skitt_results)} ammo types from 2alpha.no")
    for el in skitt_results:
        print(el)

