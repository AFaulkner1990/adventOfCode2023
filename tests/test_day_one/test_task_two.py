from src.day_one.task_two import get_combination


class TestGetCombination:
    def test_example_one(self):
        assert get_combination("1abc2") == 12

    def test_example_two(self):
        assert get_combination("pqr3stu8vwx") == 38

    def test_example_three(self):
        assert get_combination("a1b2c3d4e5f") == 15

    def test_example_four(self):
        assert get_combination("treb7uchet") == 77

    def test_example_five(self):
        assert get_combination("two1nine") == 29

    def test_example_six(self):
        assert get_combination("eightwothree") == 83

    def test_example_seven(self):
        assert get_combination("abcone2threexyz") == 13

    def test_example_eight(self):
        assert get_combination("xtwone3four") == 24

    def test_example_nine(self):
        assert get_combination("4nineeightseven2") == 42

    def test_example_ten(self):
        assert get_combination("zoneight234") == 14

    def test_example_eleven(self):
        assert get_combination("7pqrstsixteen") == 76
