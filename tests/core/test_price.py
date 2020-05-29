from ammo_finder.core.price import extract_price


import pytest


@pytest.mark.parametrize(
    "price,expected", [
        ("          170,-          ", 170),
        ("         1 170,-          ", 1170),
        ("          10 999,23,-          ", 10999.23),
        ("         Fra 1 170,-          ", 1170),
        ("         fra 1 170,-          ", 1170),
    ]
)
def test_skitt_jakt_price_returns_number(price, expected):

    result = extract_price(price)

    assert type(result) == float
    assert result == expected