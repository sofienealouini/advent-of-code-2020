import os
from itertools import combinations
from typing import List

from utils import read_lines


def find_tuple(input_sequence: List[int], tuple_size: int, expected_sum: int) -> tuple:
    sorted_input = sorted(input_sequence)
    for combination in combinations(sorted_input, tuple_size):
        if sum(combination) == expected_sum:
            return combination


if __name__ == '__main__':

    input_file_path: str = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_list: List[int] = read_lines(input_file_path=input_file_path, line_type=int)

    # Part 1
    a, b = find_tuple(input_sequence=input_list, tuple_size=2, expected_sum=2020)
    print('Part 1 result :', a * b)

    # Part 2
    c, d, e = find_tuple(input_sequence=input_list, tuple_size=3, expected_sum=2020)
    print('Part 2 result :', c * d * e)
