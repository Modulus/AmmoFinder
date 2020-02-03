from scrape.pvas_scraper import PvasScraper
import pytest
from core.category import Category


# @pytest.mark.paramerize("data", [ "/produkter/ammunisjon/rifle", "/produkter/ammunisjon/hagle", "/produkter/ammunisjon/haandvaapen", "/produkter/ammunisjon/rimfire"])
def test_generate_category_rifle():
    url = "/produkter/ammunisjon/rifle"

    result = PvasScraper.generate_category(url)

    assert result != None
    assert result == Category.RIFLE

def test_generate_category_shotgun():
    url =  "/produkter/ammunisjon/hagle"

    result = PvasScraper.generate_category(url)

    assert result != None
    assert result == Category.SHOTGUN        

def test_generate_category_shotgun():
    url =  "/produkter/ammunisjon/haandvaapen"

    result = PvasScraper.generate_category(url)

    assert result != None
    assert result == Category.HANDGUN            

def test_generate_category_rimfire():
    url = "/produkter/ammunisjon/rimfire"    

    result = PvasScraper.generate_category(url)

    assert result != None
    assert result == Category.RIMFIRE      

def test_genrate_category_has_incorrect_value_raises_value_error():
    with pytest.raises(ValueError):
        result = PvasScraper.generate_category("notexistingstuffs")


def test_fetch_has_data():
    scraper = PvasScraper()

    result = scraper.fetch()

    assert result != None
    assert len(result) > 10
    for x in result:
        print(str(x))

