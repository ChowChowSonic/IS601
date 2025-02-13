"""Test case for the tokenizer"""

from calculator.tokenizer import Tokenizer


def test_tokenizer():
    """Test function for the tokenizer"""
    t = Tokenizer("1234+ 0")
    assert t.get_token() == 1234
    assert t.get_token() == "+"
    assert t.get_token() == 0
    assert t.get_token() == ""
    assert t.get_string() == "1234+0"
    assert t.has_next() is False
