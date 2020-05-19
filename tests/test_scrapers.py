import pytest
from ammo_finder.scrape.pvas_scraper import PvasScraper
from ammo_finder.scrape.alpha_scraper import AlphaScraper
from ammo_finder.scrape.osloskytesenter_scraper import OsloskytesenterScraper

def test_pvas_scraper_fetch_has_data():
    scraper = PvasScraper()
    results = scraper.fetch()

    assert len(results) > 10


def test_alpha_scraper_fetch_has_data():
    scraper = AlphaScraper()

    results = scraper.fetch()

    assert len(results) > 10


def test_oslo_skytesenter_fetch_has_data():
    scraper = OsloskytesenterScraper()

    results = scraper.fetch()

    assert len(results) > 10