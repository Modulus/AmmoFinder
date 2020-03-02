#!/usr/bin/env python3

# Internal module package imports
from ammo_finder.scrape.alpha_scraper import AlphaScraper
from ammo_finder.scrape.pvas_scraper import PvasScraper


def main():
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
