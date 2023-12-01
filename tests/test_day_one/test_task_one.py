from src.day_one.task_one import get_combination


class TestGetCombination:
    def test_example_one(self):
        assert get_combination("1abc2") == 12

    def test_example_two(self):
        assert get_combination("pqr3stu8vwx") == 38

    def test_example_three(self):
        assert get_combination("a1b2c3d4e5f") == 15

    def test_example_four(self):
        assert get_combination("treb7uchet") == 77
