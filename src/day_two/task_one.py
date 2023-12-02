import re

class GameChecker:
    def __init__(self, max_red: int, max_green: int, max_blue: int):
        self.max_red = max_red
        self.max_green = max_green
        self.max_blue = max_blue

    def is_valid_hand(self, no_red: int, no_green: int, no_blue: int) -> bool:
        return no_red <= self.max_red and no_green <= self.max_green and no_blue <= self.max_blue

    def get_values(self, game_input: str) -> tuple[int, int, int]:
        red: re.Match = re.search(r"\d+(?=\sred)", game_input)
        green: re.Match = re.search(r"\d+(?=\sgreen)", game_input)
        blue: re.Match = re.search(r"\d+(?=\sblue)", game_input)

        return int(red.group()) if red else 0, int(green.group()) if green else 0, int(blue.group()) if blue else 0

    def is_valid_game(self, game_input: str) -> bool:
        for hand in game_input.strip().split(";"):
            no_red, no_green, no_blue = self.get_values(hand)
            if not self.is_valid_hand(int(no_red), int(no_green), int(no_blue)):
                return False
        return True


if __name__ == '__main__':
    no_valid_games: int = 0
    with open("../../data/day_two_input.txt") as file_handler:
        game_data: list[str] = file_handler.readlines()

    game_checker: GameChecker = GameChecker(12, 13, 14)

    for game in game_data:
        if game_checker.is_valid_game(game):
            no_valid_games += int(re.search(r"(?<=Game\s)\d+", game).group())

    print(no_valid_games)
