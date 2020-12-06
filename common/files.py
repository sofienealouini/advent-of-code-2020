from typing import List


def read_lines(input_file_path: str, line_type: type) -> list:
    with open(input_file_path, 'r') as input_file:
        return [line_type(line) for line in input_file.read().splitlines()]


def read_blocks(input_file_path: str) -> List[str]:
    with open(input_file_path, 'r') as input_file:
        return [block.replace('\n', ' ') for block in input_file.read().split('\n\n')]


def read_list_of_lists(input_file_path: str) -> List[List[str]]:
    with open(input_file_path, 'r') as input_file:
        return [block.split('\n') for block in input_file.read().split('\n\n')]
