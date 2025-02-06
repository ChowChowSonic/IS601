"""Tests the arg parsing capabilities of the calculator module."""
from calculator import parse_args

def test_argparse():
    """Tests the arg parsing capabilities of the calculator module."""
    assert parse_args("1+2+3", "+4") == [1, "+", 2, "+", 3, "+", 4]
    assert parse_args("5-6*7/8") == [5, "-", 6, "*", 7, "/", 8]
    assert parse_args("9^10") == [9, "^", 10]
