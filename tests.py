import os, json
import time
import functools
import re
from toolbox.utils import strip_tags
from toolbox.managers import SoundsManager
from toolbox.better_print import printx, print_lines

OUTPUT_DIR = ".output"


def test_sounds_manager():
    SoundsManager.play_beep()
    SoundsManager.play_success()


def test_better_print():
    class VerboseName:
        IMAGES = "images"
        SPAN = "span"
        QUESTION = "question"

    printx("hej", style="red")
    printx("ho", tabs=1)
    printx("image text", name=VerboseName.IMAGES)
    print_lines(tabs=1)
    print_lines(verbose_names=[VerboseName.IMAGES], tabs=1)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    test_sounds_manager()
    test_better_print()


if __name__ == "__main__":
    main()
