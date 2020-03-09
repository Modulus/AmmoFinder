# Non-standard library python package imports
import pytest

# Internal module package imports
from ammo_finder.core.category import Category
from ammo_finder.scrape.pvas_scraper import PvasScraper


# @pytest.mark.paramerize("data", [ "/produkter/ammunisjon/rifle", "/produkter/ammunisjon/hagle", "/produkter/ammunisjon/haandvaapen", "/produkter/ammunisjon/rimfire"])
def test_generate_category_rifle():
    result = Category.extract(
        "/produkter/ammunisjon/rifle"
    )
    assert result == Category.RIFLE


def test_generate_category_shotgun():
    result = Category.extract(
        "/produkter/ammunisjon/hagle"
    )
    assert result == Category.SHOTGUN


@pytest.mark.parametrize(
    'url_string',
    [
        pytest.param(
            '/produkter/ammunisjon/haandvaapen',
            id='Unknown URL string',
        ),
        pytest.param(
            'https://www.2alfa.no/ammunisjon/ladet-ammo/pistol.html',
            id='2alfa.no pistol ammo',
        ),
    ]
)
def test_generate_category_handgun(url_string: str) -> None:
    result = Category.extract(url_string)
    assert result == Category.HANDGUN


def test_generate_category_rimfire():
    result = Category.extract(
        "/produkter/ammunisjon/rimfire"
    )
    assert result == Category.RIMFIRE


def test_genrate_category_has_incorrect_value_raises_value_error():
    with pytest.raises(ValueError):
        _ = PvasScraper.generate_category("notexistingstuffs")


def test_fetch_has_data():
    scraper = PvasScraper()
    results = scraper.fetch()

    assert len(results) > 10
    # for x in result:
    #     print(str(x))
