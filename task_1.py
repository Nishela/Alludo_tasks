
""""
The function input is a list of strings of the form: ['hel', 'low', 'frog', 'hello', 'lohel', 'hlelo', 'leh', ]
The function must process the strings and group them according to the full anagram.
and return a list with lists of anagrams of the original list [['hel', 'leh'], ['low'], ['frog'], ['hello', 'lohel', 'hlelo']]

Further optimize the algorithm to complexity O(n)
"""

from collections import defaultdict


def my_func(data: list) -> list[list, ...]:
    result = defaultdict(list)
    for item in data:
        result[tuple(sorted(item))].append(item)
    return list(result.values())


if __name__ == '__main__':
    input_data = ['hel', 'low', 'frog', 'hello', 'lohel', 'hlelo', 'leh', ]
    output_data = [['hel', 'leh'], ['low'], ['frog'], ['hello', 'lohel', 'hlelo']]

    assert my_func(input_data) == output_data
