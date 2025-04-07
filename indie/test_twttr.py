import pytest

from twttr import remove_vowels

def test_word():
    assert remove_vowels('aeiou') == ''

def test_uppercase():
    assert remove_vowels('AEIOU') == ''

def test_phrase():
    assert remove_vowels('THE last ONE') == 'th lst n'