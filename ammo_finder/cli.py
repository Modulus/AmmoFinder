#!/usr/bin/env python3

# Internal module package imports
from ammo_finder.scrape.alpha_scraper import AlphaScraper
from ammo_finder.scrape.pvas_scraper import PvasScraper


def main():
    pvas_scraper = PvasScraper()
    pvas_results = pvas_scraper.fetch()

    # for el in pvas_results:
    #     print(el)

    print(f"Found {len(pvas_results)} ammo types from pvas.no")

    alpha = AlphaScraper()
    alpha_results = alpha.fetch()

    # for el in alpha_results:
    #     print(el)

    print(f"Found {len(alpha_results)} ammo types from 2alpha.no")
