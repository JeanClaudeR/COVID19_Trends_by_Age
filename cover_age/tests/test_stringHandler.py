"""
test_helpers: Testing helper functions
=======================================

"""

import pytest
from utils.stringHandler import delete_spaces

example_strings = [
        "I love banana",
        "Team spirit"
    ]
expected_strings = ["Ilovebanana",
        "Teamspirit"
        ]

@pytest.fixture
def expected_stripped():
    pairs = []
    for i in zip(example_strings, expected_strings):
        pairs.append(i)
    return pairs

# should run the test 
# with pytest -v to get details if failing

def test_delete_spaces(expected_stripped):
    for input, output in expected_stripped:
        assert delete_spaces(input) == output


        