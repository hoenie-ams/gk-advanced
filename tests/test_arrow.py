import pytest

from src.exercises.arrow import invoice


def test_invoice():
    assert invoice("pulp_fiction", 6) == 50


def test_invoice_tomorrow_never_dies():
    assert invoice("tomorrow_never_dies", 1) == 12


def test_non_existing_movie():
    with pytest.raises(LookupError):
        invoice("Nederlandse Troep", 1)
