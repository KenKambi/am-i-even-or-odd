import pytest

from am_i_even_or_odd import is_it_even_tho, is_it_odd_tho


def test_even():
    assert is_it_even_tho(2) is True
    assert is_it_even_tho(12) is True
    assert is_it_even_tho(3) is False


def test_odd():
    assert is_it_odd_tho(3) is True
    assert is_it_odd_tho(13) is True
    assert is_it_odd_tho(100) is False


def test_zero_is_even():
    assert is_it_even_tho(0) is True
    assert is_it_odd_tho(0) is False


def test_negative_numbers():
    assert is_it_even_tho(-4) is True
    assert is_it_odd_tho(-3) is True
    assert is_it_even_tho(-3) is False


@pytest.mark.parametrize("bad_value", [4.0, "4", None, [4], (4,), 4 + 0j])
def test_non_int_raises_type_error(bad_value):
    with pytest.raises(TypeError):
        is_it_even_tho(bad_value)
    with pytest.raises(TypeError):
        is_it_odd_tho(bad_value)


@pytest.mark.parametrize("bool_value", [True, False])
def test_bool_raises_type_error(bool_value):
    # bool is technically an int subclass in Python, but treating
    # True/False as numbers here would be a footgun for callers.
    with pytest.raises(TypeError):
        is_it_even_tho(bool_value)