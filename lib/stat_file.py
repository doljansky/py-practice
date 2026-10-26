"""Module reader."""


def stat_file(filename):
    """Get statistics of file by words."""
    chars = 0
    lines = 0
    words = []
    words_unique = {}

    with open(filename, 'r') as file:
        for line in file:
            word = []
            lines += 1

            for char in line:
                chars += 1
                if char.isalpha():
                    word.append(char.lower())
                elif len(word):
                    word_str = ''.join(word)
                    words.append(word_str)
                    words_unique[word_str] = words_unique.get(word_str, 0) + 1
                    word = []

    words_unique_sorted = sorted(
        words_unique.items(), key=lambda field: [field[1], -len(field[0])]
    )

    top = __map_keys(words_unique_sorted[:5])
    top_end = __map_keys(reversed(words_unique_sorted[-5:]))

    words_unique = __map_keys(words_unique.items())

    return {
        'top': top,
        'top_end': top_end,
        'words': words,
        'lines': lines,
        'chars': chars,
        'words_unique': words_unique,
    }


def __map_keys(items):
    return map(lambda field: f'{field[0]} => {field[1]}', items)
