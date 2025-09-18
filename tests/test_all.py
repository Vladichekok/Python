import pytest
from src.string_utils import smogtether_upper
from src.generator_utils import even_odd_generator

def test_smogtether_upper():
    assert smogtether_upper() == [ch.upper() for ch in "smogtether"]

def test_even_odd_generator():
    gen = even_odd_generator()
    assert next(gen) == "Paired"
    assert next(gen) == "Unpaired"
    assert next(gen) == "Paired"
