import pytest

from anagrams import find_anagrams


def test_find_anagrams():
    actual = find_anagrams('dog')
    expected = ['dog', 'god']
    assert sorted(actual) == sorted(expected)
