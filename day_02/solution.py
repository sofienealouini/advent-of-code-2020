import os
from typing import List, Tuple, Callable

from utils import read_lines


def split_line(line: str) -> Tuple[str, str, int, int]:
    positions, letter_with_colon, password = line.split(' ')
    low_position, high_position = [int(pos) for pos in positions.split('-')]
    control_letter = letter_with_colon[:-1]
    return password, control_letter, low_position, high_position


def check_validity_old_policy(password: str, control_letter: str, low_position: int, high_position: int) -> bool:
    return low_position <= password.count(control_letter) <= high_position


def check_validity_new_policy(password: str, control_letter: str, low_position: int, high_position: int) -> bool:
    return (password[low_position - 1] == control_letter) != (password[high_position - 1] == control_letter)


def count_valid(input_sequence: List[str], check_function: Callable[[str, str, int, int], bool]) -> int:
    return sum((check_function(*split_line(line)) for line in input_sequence))


if __name__ == '__main__':

    input_file_path: str = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_list: List[str] = read_lines(input_file_path=input_file_path, line_type=str)

    # Part 1
    result_old_policy: int = count_valid(input_sequence=input_list, check_function=check_validity_old_policy)
    print('Part 1 result :', result_old_policy)

    # Part 2
    result_new_policy: int = count_valid(input_sequence=input_list, check_function=check_validity_new_policy)
    print('Part 2 result :', result_new_policy)
