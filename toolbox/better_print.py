from rich import print, pretty
from rich.console import Console

console = Console()

_LINES = []

_DEFAULT_NAME = "default"
TABS = 0

_TEMP_LINES = []


def printx(*args, name=_DEFAULT_NAME, tabs=TABS, style=None, temp=False):
    s = ""
    for i in range(tabs):
        s += "  "

    args = [str(arg) for arg in args]

    line = {
        "text": f'{s}{" ".join(args)}',
        "style": style,
        "name": name,
    }

    if temp:
        _TEMP_LINES.append(line)
    else:
        _LINES.append(line)


def print_lines(verbose_names=None, tabs=TABS, clear=True):
    s = ""
    for i in range(tabs):
        s += "  "

    for line in _LINES:
        if verbose_names is None or line["name"] in verbose_names:
            console.print(f'{s}{line["text"]}', style=line["style"])

    if clear:
        clear_lines()


def add_temp():
    global _LINES
    _LINES += _TEMP_LINES
    clear_temp()


def clear_temp():
    _TEMP_LINES.clear()


def clear_lines(name=None):
    global _LINES

    if name is None:
        _LINES.clear()
    else:
        lines_temp = []
        for line in _LINES:
            if line["name"] != name:
                lines_temp.append(line)
        _LINES = lines_temp
