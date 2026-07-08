def _validate(number: int) -> None:
    """Raise a clear error if ``number`` isn't a whole number.

    ``bool`` is deliberately rejected even though it's technically an
    ``int`` subclass in Python, since checking parity of True/False
    is almost certainly a mistake on the caller's part.
    """
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError(
            f"expected an int, got {type(number).__name__!r} "
            f"({number!r}). Floats and other numeric types aren't "
            "supported to avoid ambiguity around what counts as "
            "'even' or 'odd'."
        )


def is_it_even_tho(number: int) -> bool:
    """Return True if ``number`` is even.

    :param number: the whole number to check.
    :raises TypeError: if ``number`` is not an ``int``.
    """
    _validate(number)
    return number % 2 == 0


def is_it_odd_tho(number: int) -> bool:
    """Return True if ``number`` is odd.

    :param number: the whole number to check.
    :raises TypeError: if ``number`` is not an ``int``.
    """
    _validate(number)
    return number % 2 != 0