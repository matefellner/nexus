"""
Unittest for blackjack card score function

filename must be test_mytestfile

and function is test_mycase
"""

from blackjack import card_score
import pytest


@pytest.mark.parametrize(
    "cards,score", [("KK", 20), ("JKQ", 0), ("AK", 21), ("AA", 12)]
)
def test_simple_usecase(cards, score):
    """
    Simple test for proper inputs
    """
    assert card_score(cards) == score


def test_value_error_is_raised_with_not_string():
    """
    Simple test for value errors, input bad type
    """
    with pytest.raises(ValueError):
        card_score(2)


def test_value_error_is_raised_with_short_string():
    """
    Simple test for value errors, length of string
    """
    with pytest.raises(ValueError):
        card_score("A")
