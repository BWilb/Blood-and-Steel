import unittest
from datetime import timedelta
import simple_nation_ai_pop_test

import pytest

import globe_relations.globe
from game.ai.nation_ai import NationAI
from globe_relations.globe import Globe

class AITesting:
    def __init__(self):
        self.nation = simple_nation_ai_pop_test.NationAI()

    @pytest.mark.parametrize(
        ("input_n", "expected"),
        (
            (1.5, True),
            (-1.5, True),
            (-10.34, False),
            (10.5, True),
            (100, False)
        )
    )
    def test_population_function(self):
        #pop_growth = (self.nation.population - self.nation.past_population) / ((self.nation.population + self.nation.past_population / 2))

        assert self.nation.check_population_growth(1.5) == self.nation.birth_enhancer
        assert self.nation.check_population_growth(-1.5) == self.nation.birth_enhancer
        assert self.nation.check_population_growth(-10.34) == (not self.nation.birth_control)
        assert self.nation.check_population_growth(10.5) == self.nation.birth_control
        assert self.nation.check_population_growth(100) == (not self.nation.birth_enhancer)
        assert self.nation.check_population_growth(5.5) == self.nation.birth_enhancer
        assert self.nation.check_population_growth(4.5) == self.nation.birth_control


def test_population():
    test1 = AITesting()
    test1.test_population_function()

test_population()

"""class TestLegacy(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.nation = simple_nation_ai_pop_test.NationAI()
    def test(self):
        self.assertEqual(self.nation.check_population_growth(1.5), self.nation.birth_enhancer)"""