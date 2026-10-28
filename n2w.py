"""Program for stringier."""

from math import log, floor


def number_to_word(number):
    """Convert number to worded string."""
    if number == 0:
        return 'zero'

    return __render(__parse_number(number))


def __parse_number(number):
    """Parse number."""
    rank = 1
    current = number
    node_current = None

    while current > 0:
        digit = current % 10
        node = {'type': __rank_to_type(rank), 'quantifier': digit, 'child': None}

        if node_current:
            if node_current['type'] == node['type']:
                quantifier = node_current['quantifier']
                quantifier_power = floor(log(quantifier, 10))
                quantifier_rank = 10 ** (quantifier_power + 1)
                node_current['quantifier'] = digit * quantifier_rank + quantifier
            else:
                node['child'] = node_current
                node_current = node
        else:
            node_current = node

        current //= 10
        rank += 1

    return node_current


def __render(parsed):
    current = parsed
    result = []

    while current:
        type_ = current['type']
        child = current['child']
        quantifier = current['quantifier']
        quantifier_powered = quantifier * 10

        if type_ in numbers_complex:
            result.append(number_to_word(quantifier))
            result.append(type_)

        if type_ == 'ten':
            quantifier_child = child['quantifier']
            number = quantifier_powered + quantifier_child

            if number in numbers_simple:
                result.append(numbers_simple[number])
                break
            elif quantifier_powered in numbers_simple:
                result.append(numbers_simple[quantifier_powered])

        if type_ == 'digit' and quantifier in numbers_simple:
            result.append(numbers_simple[quantifier])

        current = child

    return ' '.join(result)


def __rank_to_type(rank):
    if rank > 12:
        return 'trillion'
    elif rank > 9:
        return 'billion'
    elif rank > 6:
        return 'million'
    elif rank > 3:
        return 'thousand'
    elif rank > 2:
        return 'hundred'
    elif rank > 1:
        return 'ten'
    return 'digit'


numbers_simple = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


numbers_complex = set(['trillion', 'billion', 'million', 'thousand', 'hundred'])


__run = __name__ == '__main__'
if __run:
    print(number_to_word(1555550))
