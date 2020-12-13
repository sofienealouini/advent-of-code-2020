import os
from functools import reduce
from math import gcd
from typing import List, Tuple

from common.timing import timer


@timer
def first_synchronized_departure(earliest_departure: int, buses_with_offsets: List[Tuple[int, int]]) -> int:
    departure: int = earliest_departure
    all_synchronized = False
    while not all_synchronized:
        synchronized_buses: List[int] = find_synchronized_buses(departure, buses_with_offsets)
        all_synchronized = len(synchronized_buses) == len(buses_with_offsets)
        if all_synchronized:
            return departure
        time_to_next_departure: int = 1 if synchronized_buses == [] else least_common_multiple(synchronized_buses)
        departure = departure + time_to_next_departure


def find_synchronized_buses(departure: int, buses_with_offsets: List[Tuple[int, int]]) -> List[int]:
    return [bus for bus, offset in buses_with_offsets if (departure + offset) % bus == 0]


def least_common_multiple(numbers: List[int]) -> int:
    return reduce(lambda a, b: a * b // gcd(a, b), numbers)


@timer
def first_bus_multiplied_by_wait_time(earliest_departure: int, buses_with_offsets: List[Tuple[int, int]]) -> int:
    departure: int = earliest_departure
    while True:
        for bus, _ in buses_with_offsets:
            if departure % bus == 0:
                wait: int = departure - earliest_departure
                return bus * wait
        departure += 1


def read_input(path: str) -> Tuple[int, List[Tuple[int, int]]]:
    with open(path, 'r') as input_file:
        lines: List[str] = input_file.read().split('\n')
        earliest_departure: int = int(lines[0])
        buses_with_offsets: List[Tuple[int, int]] = [(int(bus), offset)
                                                     for offset, bus in enumerate(lines[1].split(','))
                                                     if bus != 'x']
        return earliest_departure, buses_with_offsets


if __name__ == '__main__':
    input_file_path: str = os.path.join(os.path.dirname(__file__), 'input.txt')
    earliest, buses_with_departure_offsets = read_input(path=input_file_path)

    # Part 1
    part_1_result: int = first_bus_multiplied_by_wait_time(earliest, buses_with_departure_offsets)
    print('Part 1 result :', part_1_result)

    # Part 2
    part_2_result: int = first_synchronized_departure(1, buses_with_departure_offsets)
    print('Part 2 result :', part_2_result)
