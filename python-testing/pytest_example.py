import pytest


def count_punctuation_marks(string: str) -> int:
    total_count = 0
    for sym in ",.::'":
        total_count += string.count(sym)
    return total_count


def test_empty_string():
    assert count_punctuation_marks("") == 0


def test_no_punctuation():
    assert count_punctuation_marks("Hello World") == 0


def test_single_punctuation():
    assert count_punctuation_marks("Hello World!") == 1


def test_multiple_punctuation():
    assert count_punctuation_marks("Hello, World! How are you?") == 3


def test_edge_case():
    assert count_punctuation_marks("!!!") == 3


def test_all_punctuation():
    assert count_punctuation_marks(".,:;!?") == 6
