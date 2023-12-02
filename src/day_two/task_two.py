import re
from typing import Optional


class CubePowerChecker:
    def __init__(self):
        self.max_red: Optional[int] = None
        self.max_green: Optional[int] = None
        self.max_blue: Optional[int] = None

    def get_values(self, game_input: str) -> tuple[int, int, int]:
        red: re.Match = re.search(r"\d+(?=\sred)", game_input)
        green: re.Match = re.search(r"\d+(?=\sgreen)", game_input)
        blue: re.Match = re.search(r"\d+(?=\sblue)", game_input)

        return int(red.group()) if red else 0, int(green.group()) if green else 0, int(blue.group()) if blue else 0

    def get_power(self, game_input: str) -> int:
        for hand in game_input.strip().split(";"):
            no_red, no_green, no_blue = self.get_values(hand)
            if no_red > 0:
                if self.max_red is None or self.max_red < no_red:
                    self.max_red = no_red
            if no_green > 0:
                if self.max_green is None or self.max_green < no_green:
                    self.max_green = no_green
            if no_blue > 0:
                if self.max_blue is None or self.max_blue < no_blue:
                    self.max_blue = no_blue

        power: int = 1
        if self.max_red:
            power *= self.max_red
        if self.max_green:
            power *= self.max_green
        if self.max_blue:
            power *= self.max_blue
        return power


if __name__ == '__main__':
    with open("../../data/day_two_input.txt") as file_handler:
        game_data: list[str] = file_handler.readlines()

    sum_of_power = 0
    for game in game_data:
        cube_power_checker: CubePowerChecker = CubePowerChecker()
        sum_of_power += cube_power_checker.get_power(game)

    print(sum_of_power)
