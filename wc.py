"""Count specified tokens in file."""

import argparse
from math import inf


def main():
    """Unix wc as-is."""
    parser = argparse.ArgumentParser(usage=__doc__)

    parser.add_argument('-w', '--words', help='Count words', action='store_true')
    parser.add_argument('-l', '--lines', help='Count lines', action='store_true')
    parser.add_argument('-c', '--chars', help='Count chars', action='store_true')

    parser.add_argument(
        '-L',
        '--max-line-length',
        help='Print max line length',
        type=int,
        default=inf,
    )

    parser.add_argument('file', help='File to read')

    a = parser.parse_args()

    if not a.words and not a.chars and not a.lines:
        a.words = True

    words_count = 0
    lines_count = 0
    chars_count = 0

    with open(file=a.file, mode='r') as file:
        for line in file:
            chars_count_local = 0
            lines_count += 1
            word_len = 0

            for i in range(min(len(line), a.max_line_length)):
                char = line[i]
                chars_count += 1
                chars_count_local += 1

                if char.isalnum():
                    word_len += 1
                elif word_len > 0:
                    words_count += 1
                    word_len = 0

    margin = max(
        map(
            lambda s: len(str(s)),
            [words_count, lines_count, chars_count],
        )
    )

    result = []

    if a.words:
        result.append(__format_result('Words', words_count, margin))

    if a.lines:
        result.append(__format_result('Lines', lines_count, margin))

    if a.chars:
        result.append(__format_result('Chars', chars_count, margin))

    print('\n'.join(result))


def __format_result(caption, number, margin):
    return '{0}: {1:{2}}'.format(caption, number, margin)


if __name__ == '__main__':
    main()
