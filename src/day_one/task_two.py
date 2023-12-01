from typing import Optional


def get_digit(code_input: str, index: int, is_plus: bool = True) -> (int, Optional[str]):
    if code_input[index].isdigit():
        return index, code_input[index]
    numbers: dict[str: int] = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                               "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for number in numbers.keys():
        number_length: int = len(number)
        if index + number_length <= len(code_input):
            if code_input[index: index + number_length] == number:
                return (index + number_length - 1, numbers[number]) if is_plus else (index, numbers[number])
    return (index + 1, None) if is_plus else (index -1, None)


def get_combination(code_input: str) -> int:
    left_index: int = 0
    left_value: Optional[str] = None
    right_index = len(code_input) - 1
    right_value: Optional[str] = None

    while (left_value is None or right_value is None) or left_index > right_index:
        if left_value is None:
            left_index, left_value = get_digit(code_input, left_index)

        if right_value is None:
            right_index, right_value = get_digit(code_input, right_index, False)

    if left_value is None and right_value is None:
        return 0
    if left_value is None or right_value is None:
        raise ValueError(f"Error should not end up with single None value: {code_input}."
                         f"\nleft index - value: {left_index} - {left_value}, "
                         f"right index - value: {right_index} - {right_value}")

    return (int(left_value) * 10) + int(right_value)


if __name__ == '__main__':
    sum_of_combinations: int = 0
    with open("../../data/day_one_input.txt") as file_handler:
        combination_codes: list[str] = file_handler.readlines()
        for code in combination_codes:
            combination = get_combination(code.strip())
            sum_of_combinations += combination
    print(sum_of_combinations)
