import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Функция capitalize.
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Функция trim.
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Test ", "Test "),
    (" april", "april"),
    ("  T x t", "T x t")
])
def test_trim_positive(input_str, expected):
    res = string_utils.trim(input_str)
    assert res == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("777", "777"),
    ("7 october", "7 october"),
])
def test_trim_negative(input_str, expected):
    res = string_utils.trim(input_str)
    assert res == expected


@pytest.mark.parametrize("input_str", [None, []])
def test_trim_negative_function_raises(input_str):
    # Ожидается ошибка: Неверный атрибут
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)


# Функция contains.
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Test ", "T", True),
    ("123", "4", False),
    ("1 Abc", " ", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "T", False),
    ("Abc", "", True),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol", [
    (None, "4"),
])
def test_contains_negative_raises(input_str, symbol):
    # Ожидается ошибка: Неверный атрибут
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, symbol)


# Функция delete.
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Lesson", "L", "esson"),
    ("Chelyabinsk", "yabinsk", "Chel"),
    ("07 october 2025", "07 october", " 2025")
])
def test_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "z", ""),
    ("   ", "7", "   "),
    ("Python", "m", "Python")
])
def test_delete_symbol_(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected_exception", [
    (None, "4", AttributeError),  # Проверяем, что вызывается AttributeError
    ("zebra", None, TypeError)    # Проверяем, что вызывается TypeError
])
def test_delete_negative_raises(string, symbol, expected_exception):
    # Проверяем, что вызывается ожидаемое исключение
    with pytest.raises(expected_exception):
        string_utils.delete_symbol(string, symbol)
