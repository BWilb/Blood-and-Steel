import test
import pytest

@pytest.mark.parametrize((input_n, test),(5, 25))

def test_square(input_n):
    assert test.square(input_n) == 25

test_square()