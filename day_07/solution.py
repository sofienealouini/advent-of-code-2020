import os
from functools import reduce
from typing import List, Dict, Tuple, Set, Callable, Generator

from common.files import read_lines
from common.timing import timer


@timer
def count_bags(bag_color: str,
               plain_text_rules: List[str],
               count_method: Callable[[str, Dict[str, List[Tuple[int, str]]]], int]) -> int:
    rule_dict: Dict[str, List[Tuple[int, str]]] = build_rule_dictionary(plain_text_rules)
    return count_method(bag_color, rule_dict)


def count_all_sub_bags(bag_color: str, rule_dict: Dict[str, List[Tuple[int, str]]]) -> int:
    sub_bags_with_counts: List[Tuple[int, str]] = rule_dict[bag_color]
    return sum([sub_bag[0] * (1 + count_all_sub_bags(sub_bag[1], rule_dict))
                for sub_bag in sub_bags_with_counts])


def count_distinct_containers(bag_color: str, rule_dict: Dict[str, List[Tuple[int, str]]]) -> int:
    return sum((bag_color in find_distinct_sub_bags(color, rule_dict) for color in rule_dict))


def find_distinct_sub_bags(bag_color: str, rule_dict: Dict[str, List[Tuple[int, str]]]) -> Set[str]:
    sub_bags: Set[str] = set((sub_bag[1] for sub_bag in rule_dict[bag_color]))
    sub_sub_bags: Generator[Set[str], None, None] = (find_distinct_sub_bags(sub_bag, rule_dict) for sub_bag in sub_bags)
    return sub_bags.union(reduce(lambda x, y: x.union(y), sub_sub_bags, set()))


def build_rule_dictionary(rules: List[str]) -> Dict[str, List[Tuple[int, str]]]:
    return reduce(lambda x, y: {**x, **y}, (parse_rule(rule) for rule in rules))


def parse_rule(rule: str) -> Dict[str, List[Tuple[int, str]]]:
    tokens = rule.replace('.', '').replace(',', '').split()
    main_color = ' '.join([tokens[0], tokens[1]])
    res = {main_color: []}
    for i in range(len(tokens)):
        if tokens[i].isnumeric():
            sub_bag_number = int(tokens[i])
            sub_bag_color = ' '.join([tokens[i + 1], tokens[i + 2]])
            res[main_color].append((sub_bag_number, sub_bag_color))
    return res


if __name__ == '__main__':
    input_file_path: str = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_list: List[str] = read_lines(input_file_path=input_file_path, line_type=str)

    # Part 1
    part_1_result: int = count_bags('shiny gold', input_list, count_distinct_containers)
    print('Part 1 result :', part_1_result)

    # Part 2
    part_2_result: int = count_bags('shiny gold', input_list, count_all_sub_bags)
    print('Part 2 result :', part_2_result)
