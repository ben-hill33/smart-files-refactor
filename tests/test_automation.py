import pytest
import pytest_watch
import os
from automation import create_dir, user, folders_to_create, move_files
from pathlib import Path

def test_does_create_file():
    test = [f'/Users/{user}/Downloads/test']
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected
    

def test_create_document_folder():
    test = [f'/Users/{user}/Downloads/documents']
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


def test_create_media_folder():
    test = [f'/Users/{user}/Downloads/media']
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


def test_create_software_folder():
    test = [f'/Users/{user}/Downloads/software']
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


def test_create_other_folder():
    test = [f'/Users/{user}/Downloads/others']
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected

def test_create_dir_is_list():
    test = f'/Users/{user}/Downloads/others'
    with pytest.raises(TypeError) as e:
        create_dir(test)
    assert str(e.value) == 'Must be a list!'

# test move_files method
def test_move_file_document():
    test = f'/Users/{user}/Downloads/test.txt'
    Path(test).touch()
    move_files(['test.txt'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/documents/test.txt')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/documents/test.txt')

def test_move_file_media():
    test = f'/Users/{user}/Downloads/test.jpg'
    Path(test).touch()
    move_files(['test.jpg'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/media/test.jpg')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/media/test.jpg')

def test_move_file_software():
    test = f'/Users/{user}/Downloads/test.exe'
    Path(test).touch()
    move_files(['test.exe'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/software/test.exe')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/software/test.exe')

def test_move_file_others(): 
    test = f'/Users/{user}/Downloads/test.zip'
    Path(test).touch()
    move_files(['test.zip'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/others/test.zip')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/others/test.zip')