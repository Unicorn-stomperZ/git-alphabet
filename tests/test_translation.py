# coding: utf-8

"""Test suite of the unicorn <--> git translation"""

import pytest

from unicorn import (
    translate_command,
    replace_command,
)


@pytest.mark.parametrize('command, expected', [
    (['unicorn', 'attends'], ['git', 'stash']),
])
def test_translate_command(command, expected):
    """Check the marcel --> git command translation."""
    assert translate_command(command) == expected


@pytest.mark.parametrize('command, expected', [
    (['unicorn', 'attends'], ['git', 'attends']),
])
def test_replace_command(command, expected):
    """Check the logic behing the command replacement."""
    assert replace_command(command) == expected
