import pytest
import pytest_watch
import os
from crontab import CronTab
import click
from automation import create_dir, user, folders_to_create, move_files, add_cron_job, command, every_minute, hourly, daily, weekly, monthly
from scripts.smart_files import *
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

# test for dupe files
def test_dupe_files_documents(): 
    if os.path.isfile(f'/Users/{user}/Downloads/documents/test.txt'):
        os.remove(f'/Users/{user}/Downloads/documents/test.txt')
    test = f'/Users/{user}/Downloads/test.txt'
    Path(test).touch()
    move_files(['test.txt'])
    Path(test).touch()
    move_files(['test.txt'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/documents/test_1.txt')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/documents/test_1.txt')
    os.remove(f'/Users/{user}/Downloads/documents/test.txt')

def test_dupe_files_media(): 
    if os.path.isfile(f'/Users/{user}/Downloads/media/test.jpg'):
        os.remove(f'/Users/{user}/Downloads/media/test.jpg')
    test = f'/Users/{user}/Downloads/test.jpg'
    Path(test).touch()
    move_files(['test.jpg'])
    Path(test).touch()
    move_files(['test.jpg'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/media/test_1.jpg')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/media/test_1.jpg')
    os.remove(f'/Users/{user}/Downloads/media/test.jpg')

def test_dupe_files_software(): 
    if os.path.isfile(f'/Users/{user}/Downloads/software/test.exe'):
        os.remove(f'/Users/{user}/Downloads/software/test.exe')
    test = f'/Users/{user}/Downloads/test.exe'
    Path(test).touch()
    move_files(['test.exe'])
    Path(test).touch()
    move_files(['test.exe'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/software/test_1.exe')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/software/test_1.exe')
    os.remove(f'/Users/{user}/Downloads/software/test.exe')

def test_dupe_files_others(): 
    if os.path.isfile(f'/Users/{user}/Downloads/others/test.zip'):
        os.remove(f'/Users/{user}/Downloads/others/test.zip')
    test = f'/Users/{user}/Downloads/test.zip'
    Path(test).touch()
    move_files(['test.zip'])
    Path(test).touch()
    move_files(['test.zip'])
    actual = os.path.isfile(f'/Users/{user}/Downloads/others/test_1.zip')
    expected = True
    assert actual == expected 
    os.remove(f'/Users/{user}/Downloads/others/test_1.zip')
    os.remove(f'/Users/{user}/Downloads/others/test.zip')

# Crontab
def test_crontab_every_minute():
    job = add_cron_job(every_minute)
    actual = job[:9]
    expected = "* * * * *"
    assert actual == expected

def test_crontab_every_hour():
    job = add_cron_job(hourly)
    actual = job[:7]
    expected = "@hourly"
    assert actual == expected

def test_crontab_every_day():
    job = add_cron_job(daily)
    actual = job[:6]
    expected = "@daily"
    assert actual == expected

def test_crontab_weekly():
    job = add_cron_job(weekly)
    actual = job[:7]
    expected = "@weekly"
    assert actual == expected

def test_crontab_monthly():
    job = add_cron_job(monthly)
    actual = job[:8]
    expected = "@monthly"
    assert actual == expected

