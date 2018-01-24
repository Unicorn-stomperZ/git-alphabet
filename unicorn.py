#!/usr/bin/env python
# coding: utf-8

"""
unicorn is a french and a 'what the fuck' wrapper around the git CLI

inspired by brouberol/marcel <https://github.com/brouberol/marcel/blob/master/marcel.py>
"""

import subprocess
import sys

__version__ = '0.0.1'

# TODO: Move translation to dedicated file
TRANSLATIONS = {
    # Commands
    u'attends': u'stash'
}

BASE_COMMAND = 'get'


def replace_command(command):
    """Replace the executable itself for given values of the first command."""
    if len(command) > 1:
        command[0] = BASE_COMMAND
    return command


def translate_command(command):
    """Translate the french parts of the command to git syntax."""
    command = replace_command(command)
    return [TRANSLATIONS.get(chunk, chunk) for chunk in command if chunk]


def main():  # pragma: no cover
    """Run git commands from unicorn syntax."""
    subprocess.call(translate_command(sys.argv))


if __name__ == '__main__':  # pragma: no cover
    main()