import test
import pytest
import unittest
@pytest.mark.parametrize(
    ('input_n', 'expected'),
    (
            (5, 25),
            (3, 9),
    )
)

def test_square(input_n, expected):
    assert test.square(input_n) == expected

class TestSquare:
    def test_square(self):
        assert test.square(3) == 9

class TestLegacy(unittest.TestCase):
    def test(self):
        self.assertEqual(test.square(3), 9)