import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("skypro", "Skypro"),
        ("", ""),
        ("a", "A"),
        ("A", "A"),
        ("123abc", "123abc"),
        (" skypro", " skypro")])
def test_capitalize(input_text, expected_output):
    assert string_utils.capitalize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("   skypro", "skypro"),
        ("", ""),
        ("   ", ""),
        ("skypro", "skypro"),
        (" skypro", "skypro")])
def test_trim(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Skypro", "S", True),
        ("Skypro", "U", False),
        ("", "a", False),
        ("Sky Pro", " ", True),
        ("Sky123", "1", True),
        ("SkyPro", "", True)])
def test_contains(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("", "a", ""),
        ("SkyPro", "x", "SkyPro"),
        ("Sky123", "1", "Sky23")])
def test_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
