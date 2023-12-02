from day_two.task_one import GameChecker


class TestGameChecker:
    game_checker = GameChecker(12, 13, 14)

    def test_get_values_single_digit(self):
        assert self.game_checker.get_values("1 red, 2 green, 3 blue") == (1, 2, 3)

    def test_get_values_double_digit(self):
        assert self.game_checker.get_values("1 red, 24 green, 3 blue") == (1, 24, 3)

    def test_get_values_out_of_order(self):
        assert self.game_checker.get_values("3 blue, 1 red, 2 green") == (1, 2, 3)

    def test_get_values_one_missing(self):
        assert self.game_checker.get_values("1 red,  3 blue") == (1, 0, 3)

    def test_get_values_with_game_preface(self):
        assert self.game_checker.get_values("Game 4: 1 red, 2 green, 3 blue") == (1, 2, 3)

    def test_is_valid_game_example_one(self):
        assert self.game_checker.is_valid_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == True

    def test_is_valid_game_example_two(self):
        assert self.game_checker.is_valid_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == True

    def test_is_valid_game_example_three(self):
        assert self.game_checker.is_valid_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == False

    def test_is_valid_game_example_four(self):
        assert self.game_checker.is_valid_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == False

    def test_is_valid_game_example_five(self):
        assert self.game_checker.is_valid_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == True