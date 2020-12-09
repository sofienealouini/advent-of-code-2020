import os
from itertools import combinations
from typing import List, Callable

from common.files import read_lines
from common.timing import timer


@timer
def solve(xmas_encrypted_data: List[int], hacking_method: Callable[[List[int]], int]) -> int:
    return hacking_method(xmas_encrypted_data)


def find_encryption_weakness(xmas_encrypted_data: List[int]) -> int:
    first_invalid_number: int = find_first_invalid_number(xmas_encrypted_data)
    for i in range(len(xmas_encrypted_data)):
        s = xmas_encrypted_data[i]
        acc = [xmas_encrypted_data[i]]
        j = i
        while s < first_invalid_number:
            j += 1
            acc.append(xmas_encrypted_data[j])
            s += xmas_encrypted_data[j]
            if s == first_invalid_number:
                return min(acc) + max(acc)


def find_first_invalid_number(xmas_encrypted_data: List[int]) -> int:
    for n in range(25, len(xmas_encrypted_data)):
        number_to_test: int = xmas_encrypted_data[n]
        if not any((sum(comb) == number_to_test
                    for comb in combinations(xmas_encrypted_data[n - 25:n], 2)
                    if comb[0] != comb[1])):
            return number_to_test


if __name__ == '__main__':
    input_file_path: str = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_list: List[int] = read_lines(input_file_path=input_file_path, line_type=int)

    # Part 1
    part_1_result: int = solve(input_list, hacking_method=find_first_invalid_number)
    print('Part 1 result :', part_1_result)

    # Part 2
    part_2_result: int = solve(input_list, hacking_method=find_encryption_weakness)
    print('Part 2 result :', part_2_result)
