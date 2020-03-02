# Non-standard library python package imports
import pytest

# Internal module package imports
from ammo_finder.core.category import Category
from ammo_finder.scrape.pvas_scraper import PvasScraper


# @pytest.mark.paramerize("data", [ "/produkter/ammunisjon/rifle", "/produkter/ammunisjon/hagle", "/produkter/ammunisjon/haandvaapen", "/produkter/ammunisjon/rimfire"])
def test_generate_category_rifle():
    url = "/produkter/ammunisjon/rifle"

    result = Category.extract(url)

    assert result is not None
    assert result == Category.RIFLE


def test_generate_category_shotgun():
    url = "/produkter/ammunisjon/hagle"

    result = Category.extract(url)

    assert result is not None
    assert result == Category.SHOTGUN


def test_generate_category_handgun():
    url = "/produkter/ammunisjon/haandvaapen"

    result = Category.extract(url)

    assert result is not None
    assert result == Category.HANDGUN


def test_generate_category_rimfire():
    url = "/produkter/ammunisjon/rimfire"

    result = Category.extract(url)

    assert result is not None
    assert result == Category.RIMFIRE


def test_generate_category_pistol_returns_correct_category():
    url = "https://www.2alfa.no/ammunisjon/ladet-ammo/pistol.hml"

    result = Category.extract(url)

    assert result is not None
    assert result == Category.HANDGUN


def test_genrate_category_has_incorrect_value_raises_value_error():
    with pytest.raises(ValueError):
        _ = PvasScraper.generate_category("notexistingstuffs")


def test_fetch_has_data():
    scraper = PvasScraper()

    result = scraper.fetch()

    assert result is not None
    assert len(result) > 10
    for x in result:
        print(str(x))
