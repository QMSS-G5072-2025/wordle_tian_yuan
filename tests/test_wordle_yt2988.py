from wordle_yt2988.wordle_yt2988 import (
    validate_guess,
    check_guess,
)

import pytest

def test_validate_guess():
    """validate_guess should accept 5-letter alphabetic words, case-insensitive."""
    assert validate_guess("crane") is True
    assert validate_guess("CRANE") is False
    assert validate_guess("cat") is False
    assert validate_guess("abc12") is False


def test_check_guess_basic():
    """check_guess should return correct colors for simple cases."""
    result = check_guess("crane", "crane")
    assert result == [
        ("c", "green"),
        ("r", "green"),
        ("a", "green"),
        ("n", "green"),
        ("e", "green"),
    ]