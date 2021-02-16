import pytest
import pytest_watch
import os
from automation import create_dir, user


def test_does_create_file():
    test = f'/Users/{user}/Downloads/test'
    create_dir(test)
    actual = os.path.isdir(test)
    expected = True
    assert actual == expected
