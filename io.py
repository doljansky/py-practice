"""Looped reading line."""

from sys import stdin, stdout


def ping_pong():
    """Read line in pingpong style."""
    lines = []

    while True:
        in_ = stdin.readline()

        if in_.count('stop') > 0:
            break

        lines.append(in_)

    lines_readed = len(lines)
    margin = max(len(str(lines_readed)), 3)

    out = '\n\nLines readed: {lines_readed:*>{margin}}\n{lines}'.format(
        lines_readed=lines_readed, margin=margin, lines=''.join(lines)
    )

    stdout.write(out)


if __name__ == '__main__':
    ping_pong()
