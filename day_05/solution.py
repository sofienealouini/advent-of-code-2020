import os

from common.timing import timer


@timer
def solve() -> int:
    return 1


if __name__ == '__main__':
    input_file_path: str = os.path.join(os.path.dirname(__file__), 'input.txt')

    # Part 1
    part_1_result = solve()
    print('Part 1 result :', part_1_result)

    # Part 2
    part_2_result = solve()
    print('Part 2 result :', part_2_result)
