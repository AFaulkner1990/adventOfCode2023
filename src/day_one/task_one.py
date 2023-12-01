from typing import Optional


def get_combination(code_input: str) -> int:
    left_index: int = 0
    left_value: Optional[str] = None
    right_index = len(code_input) - 1
    right_value: Optional[str] = None

    while (left_value is None or right_value is None) or left_index > right_index:
        if left_value is None:
            left_char: str = code_input[left_index]
            if left_char.isdigit():
                left_value = left_char
            else:
                left_index += 1

        if right_value is None:
            right_char: str = code_input[right_index]
            if right_char.isdigit():
                right_value = right_char
            else:
                right_index -= 1

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
