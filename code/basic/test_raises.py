from rpncalc.utils import calc

import pytest

# basic/test_raises.py

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calc(3, 0, '/')


def test_raises_value_error():
    with pytest.raises(ValueError, match=r"Invalid"):
        calc(1,99, "%")
