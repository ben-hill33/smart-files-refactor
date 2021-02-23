import pytest
import os
from crontab import CronTab
from click.testing import CliRunner
from automation import (
    create_dir,
    user,
    folders_to_create,
    move_files,
    add_cron_job,
    command,
    every_minute,
    hourly,
    daily,
    weekly,
    monthly,
)
from scripts.smart_files import smart_files
from pathlib import Path

# @pytest.mark.skip("pending")
def test_does_create_file():
    test = [f"/Users/{user}/Downloads/test"]
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_create_document_folder():
    test = [f"/Users/{user}/Downloads/documents"]
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_create_media_folder():
    test = [f"/Users/{user}/Downloads/media"]
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_create_software_folder():
    test = [f"/Users/{user}/Downloads/software"]
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_create_other_folder():
    test = [f"/Users/{user}/Downloads/others"]
    create_dir(test)
    actual = os.path.isdir(test[0])
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_create_dir_is_list():
    test = f"/Users/{user}/Downloads/others"
    with pytest.raises(TypeError) as e:
        create_dir(test)
    assert str(e.value) == "Must be a list!"


# test move_files method
# @pytest.mark.skip("pending")
def test_move_file_document():
    test = f"/Users/{user}/Downloads/test.txt"
    Path(test).touch()
    move_files(["test.txt"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/documents/test.txt")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/documents/test.txt")


# @pytest.mark.skip("pending")
def test_move_file_media():
    test = f"/Users/{user}/Downloads/test.jpg"
    Path(test).touch()
    move_files(["test.jpg"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/media/test.jpg")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/media/test.jpg")


# @pytest.mark.skip("pending")
def test_move_file_software():
    test = f"/Users/{user}/Downloads/test.exe"
    Path(test).touch()
    move_files(["test.exe"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/software/test.exe")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/software/test.exe")


# @pytest.mark.skip("pending")
def test_move_file_others():
    test = f"/Users/{user}/Downloads/test.zip"
    Path(test).touch()
    move_files(["test.zip"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/others/test.zip")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/others/test.zip")


# test for dupe files
# @pytest.mark.skip("pending")
def test_dupe_files_documents():
    if os.path.isfile(f"/Users/{user}/Downloads/documents/test.txt"):
        os.remove(f"/Users/{user}/Downloads/documents/test.txt")
    test = f"/Users/{user}/Downloads/test.txt"
    Path(test).touch()
    move_files(["test.txt"])
    Path(test).touch()
    move_files(["test.txt"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/documents/test_1.txt")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/documents/test_1.txt")
    os.remove(f"/Users/{user}/Downloads/documents/test.txt")


# @pytest.mark.skip("pending")
def test_dupe_files_media():
    if os.path.isfile(f"/Users/{user}/Downloads/media/test.jpg"):
        os.remove(f"/Users/{user}/Downloads/media/test.jpg")
    test = f"/Users/{user}/Downloads/test.jpg"
    Path(test).touch()
    move_files(["test.jpg"])
    Path(test).touch()
    move_files(["test.jpg"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/media/test_1.jpg")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/media/test_1.jpg")
    os.remove(f"/Users/{user}/Downloads/media/test.jpg")


# @pytest.mark.skip("pending")
def test_dupe_files_software():
    if os.path.isfile(f"/Users/{user}/Downloads/software/test.exe"):
        os.remove(f"/Users/{user}/Downloads/software/test.exe")
    test = f"/Users/{user}/Downloads/test.exe"
    Path(test).touch()
    move_files(["test.exe"])
    Path(test).touch()
    move_files(["test.exe"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/software/test_1.exe")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/software/test_1.exe")
    os.remove(f"/Users/{user}/Downloads/software/test.exe")


# @pytest.mark.skip("pending")
def test_dupe_files_others():
    if os.path.isfile(f"/Users/{user}/Downloads/others/test.zip"):
        os.remove(f"/Users/{user}/Downloads/others/test.zip")
    test = f"/Users/{user}/Downloads/test.zip"
    Path(test).touch()
    move_files(["test.zip"])
    Path(test).touch()
    move_files(["test.zip"])
    actual = os.path.isfile(f"/Users/{user}/Downloads/others/test_1.zip")
    expected = True
    assert actual == expected
    os.remove(f"/Users/{user}/Downloads/others/test_1.zip")
    os.remove(f"/Users/{user}/Downloads/others/test.zip")


# Crontab
# @pytest.mark.skip("pending")
def test_crontab_every_minute():
    job = add_cron_job(every_minute)
    actual = job[:9]
    expected = "* * * * *"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_crontab_every_hour():
    job = add_cron_job(hourly)
    actual = job[:7]
    expected = "@hourly"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_crontab_every_day():
    job = add_cron_job(daily)
    actual = job[:6]
    expected = "@daily"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_crontab_weekly():
    job = add_cron_job(weekly)
    actual = job[:7]
    expected = "@weekly"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_crontab_monthly():
    job = add_cron_job(monthly)
    actual = job[:8]
    expected = "@monthly"
    assert actual == expected


#### MAKE SURE DOWNLOADS FOLDER IS EMPTY BEFORE RUNNING THESE TESTS!!!####
# Click Tests
# @pytest.mark.skip("pending")
def test_smart_files_command():
    runner = CliRunner()
    result = runner.invoke(smart_files)
    assert result.exit_code == 0
    assert "Usage: smart-files [OPTIONS] COMMAND [ARGS]..." in result.output


# @pytest.mark.skip("pending")
def test_show_files_command():
    test = f"/Users/{user}/Downloads/test.zip"
    Path(test).touch()
    runner = CliRunner()
    result = runner.invoke(smart_files, ["show-files"])
    assert result.exit_code == 0
    assert "Files not yet sorted:" in result.output
    os.remove(f"/Users/{user}/Downloads/test.zip")


# @pytest.mark.skip("pending")
def test_show_files_command_empty():
    runner = CliRunner()
    result = runner.invoke(smart_files, ["show-files"])
    assert result.exit_code == 0
    assert "All files have been sorted!" in result.output


# @pytest.mark.skip("pending")
def test_run_command():
    test = f"/Users/{user}/Downloads/test.zip"
    Path(test).touch()
    runner = CliRunner()
    result = runner.invoke(smart_files, ["run"])
    assert result.exit_code == 0
    assert "Running Smart-files..." in result.output
    assert "Moving Files Now..." in result.output
    assert "Smart-files run complete!" in result.output
    os.remove(f"/Users/{user}/Downloads/others/test.zip")


# @pytest.mark.skip("pending")
def test_run_command_empty():
    runner = CliRunner()
    result = runner.invoke(smart_files, ["run"])
    assert result.exit_code == 0
    assert "There aren't any files to move. Great Job!" in result.output


# @pytest.mark.skip("pending")
def test_cron_daily_command():
    print(os.system("crontab -l"))
    os.system("crontab -r")
    runner = CliRunner()
    result = runner.invoke(smart_files, ["cron", "-d"])
    assert result.exit_code == 0
    assert "Your cron job has been added successfully!" in result.output
    os.system("crontab -r")


# @pytest.mark.skip("pending")
def test_cron_hourly_command():
    print(os.system("crontab -l"))
    os.system("crontab -r")
    runner = CliRunner()
    result = runner.invoke(smart_files, ["cron", "-h"])
    assert result.exit_code == 0
    assert "Your cron job has been added successfully!" in result.output
    os.system("crontab -r")


# @pytest.mark.skip("pending")
def test_cron_weekly_command():
    print(os.system("crontab -l"))
    os.system("crontab -r")
    runner = CliRunner()
    result = runner.invoke(smart_files, ["cron", "-w"])
    assert result.exit_code == 0
    assert "Your cron job has been added successfully!" in result.output
    os.system("crontab -r")


# @pytest.mark.skip("pending")
def test_cron_monthly_command():
    print(os.system("crontab -l"))
    os.system("crontab -r")
    runner = CliRunner()
    result = runner.invoke(smart_files, ["cron", "-o"])
    assert result.exit_code == 0
    assert "Your cron job has been added successfully!" in result.output
    os.system("crontab -r")


# @pytest.mark.skip("pending")
def test_cron_minute_command():
    print(os.system("crontab -l"))
    os.system("crontab -r")
    runner = CliRunner()
    result = runner.invoke(smart_files, ["cron", "-m"])
    assert result.exit_code == 0
    assert "Your cron job has been added successfully!" in result.output
    os.system("crontab -r")


# @pytest.mark.skip("pending")
