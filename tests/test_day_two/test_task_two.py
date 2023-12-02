from day_two.task_two import CubePowerChecker


class TestCubePowerChecker:
    def test_get_values_single_digit(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_values("1 red, 2 green, 3 blue") == (1, 2, 3)

    def test_get_values_double_digit(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_values("1 red, 24 green, 3 blue") == (1, 24, 3)

    def test_get_values_out_of_order(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_values("3 blue, 1 red, 2 green") == (1, 2, 3)

    def test_get_values_one_missing(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_values("1 red,  3 blue") == (1, 0, 3)

    def test_get_values_with_game_preface(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_values("Game 4: 1 red, 2 green, 3 blue") == (1, 2, 3)

    def test_get_power_example_one(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48

    def test_get_power_example_two(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_power("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 12

    def test_get_power_example_three(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_power("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 1560

    def test_get_power_example_four(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_power("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 630

    def test_get_power_example_five(self):
        game_checker: CubePowerChecker = CubePowerChecker()
        assert game_checker.get_power("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 36
