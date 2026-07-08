from am_i_even_or_odd import (is_it_even_tho, is_it_odd_tho)

def test_even():
    assert is_it_even_tho(2) is True
    assert is_it_even_tho(12) is True
    assert is_it_even_tho(3) is False


def test_odd():
    assert is_it_odd_tho(3) is True
    assert is_it_odd_tho(13) is True
    assert is_it_odd_tho(0) is False