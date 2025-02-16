"""Testing the main driver code """

import pytest
from main import calculate_and_print
import sys


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 54),
        ("5", 5),
        ("10 +3", 13),
        ("10*3* 3", 90),
        ("10 / 3", 3.3333333333333335),
        ("100+5     ", 105),
        ("1+2+3", 6),
    ],
)
def test_calculator(test_input, expected):
    """Tests the printing function of the calculator"""
    assert calculate_and_print(test_input) == expected
    with pytest.raises(ZeroDivisionError):
        assert calculate_and_print("1/0") == 1


def test_from_pipe():
    oldstdin = sys.stdin
    sys.stdin = open("testdata.txt")
    assert calculate_and_print([]) is None
    sys.stdin = oldstdin
