import os
from itertools import product
from typing import List, Tuple, Dict, Union

from solutions.python.common.files import INPUTS_FOLDER, read_list_of_lists
from solutions.python.common.timing import timer


def alter_rule_zero(clean_rules: Dict[int, List[str]], n: int) -> str:
    pass


@timer
def part_1(clean_rules: Dict[int, List[str]], messages: List[str]) -> int:
    counter = 0
    for message in messages:
        if message in clean_rules[0]:
            counter += 1
    return counter


def transform_to_clean_rules(parsed_rules: Dict[int, Union[str, List[Tuple[int, ...]]]]) -> Dict[int, List[str]]:
    clean_rules = {
        121: ['a'],
        125: ['b']
    }

    while 0 not in clean_rules:
        for r in parsed_rules:
            current_rule = parsed_rules[r]
            if (r not in clean_rules) and all(e in clean_rules for t in current_rule for e in t):
                new_rule_r = []
                for t in current_rule:
                    new_rule_r.extend([''.join(c) for c in product(*map(lambda e: clean_rules[e], t))])
                clean_rules[r] = new_rule_r
    return clean_rules


def references_already_processed(rule_id: int,
                                 parsed_rules: Dict[int, Union[str, List[Tuple[int, ...]]]],
                                 clean_rules: Dict[int, str]) -> bool:
    return all(reference in clean_rules for tup in parsed_rules[rule_id] for reference in tup)


def parse_raw_rules(raw_rules: List[str]) -> Dict[int, Union[str, List[Tuple[int, ...]]]]:
    return dict([parse_raw_rule(raw_rule) for raw_rule in raw_rules])


def parse_raw_rule(raw_rule: str) -> Tuple[int, Union[str, List[Tuple[int, ...]]]]:
    rule_number, rule_value = raw_rule.split(': ')
    if rule_value in ('"a"', '"b"'):
        return int(rule_number), rule_value.replace('"', '')
    else:
        return int(rule_number), [tuple(int(ref) for ref in pair.split(' ')) for pair in rule_value.split(' | ')]


if __name__ == "__main__":
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_19', 'input.txt')
    raw_rules_list, messages_list = read_list_of_lists(input_file_path=input_file_path)

    cleaned_rules = transform_to_clean_rules(parse_raw_rules(raw_rules_list))

    # Part 1
    part_1_result: int = part_1(clean_rules=cleaned_rules, messages=messages_list)
    assert part_1_result == 203
    print('Part 1 result :', part_1_result)

    # Part 2
    # part_2_result: int = solve(raw_rules=raw_rules_list, messages=messages_list)
    # assert part_2_result == 0
    # print('Part 2 result :', part_2_result)
