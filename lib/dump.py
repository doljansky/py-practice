"""Dump contents to filename."""


def dump(filename, chars, lines, words, words_unique, top, top_end):
    """Execute dumping."""
    with open(filename, 'w') as file:
        fl = len(str(max([chars, len(words), lines])))

        words_rendered = __render_list(words)
        words_unique_rendered = __render_list(words_unique)
        top_rendered = __render_list(top)
        top_end_rendered = __render_list(top_end)

        contents = """\
In file:
    Chars {0:{fl}}
    Lines {1:{fl}}
    Words {2:{fl}}

Contents:

{3}

Count by words:

{4}

Top start:

{5}

Top end:

{6}""".format(
            chars,
            lines,
            len(words),
            words_rendered,
            words_unique_rendered,
            top_rendered,
            top_end_rendered,
            fl=fl,
        )
        file.write(contents)


def __render_list(list):
    return '\n'.join(list)
