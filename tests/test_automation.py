import pytest
import pytest_watch
import os
from automation import create_dir, user, folders_to_create


def test_does_create_file():
    test = [f'/Users/{user}/Downloads/test']
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


# def test_raise_error_if_file_exists():
#     test = f'/Users/{user}/Downloads/test'
#     create_dir(test)
#     actual = create_dir(test)
#     expected = '/Users/benshomefolder/Downloads/test'
#     assert actual == expected

def test_create_document_folder():
    test = f'/Users/{user}/Downloads/document'
    create_dir(test)
    actual = os.path.isdir(test)
    expected = True
    assert actual == expected


def test_create_media_folder():
    test = f'/Users/{user}/Downloads/media'
    create_dir(test)
    actual = os.path.isdir(test)
    expected = True
    assert actual == expected


def test_create_software_folder():
    test = f'/Users/{user}/Downloads/software'
    create_dir(test)
    actual = os.path.isdir(test)
    expected = True
    assert actual == expected


def test_create_other_folder():
    test = f'/Users/{user}/Downloads/others'
    actual = os.path.isdir(test)
    expected = True
    assert actual == expected
