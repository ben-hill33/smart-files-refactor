import os
import sys
from shutil import move
from pathlib import Path
import click
from crontab import CronTab

# User Variable
user = os.getenv("USER")

# Directory Variables
root_dir = f"/Users/{user}/Downloads/"
media_dir = f"/Users/{user}/Downloads/media/"
documents_dir = f"/Users/{user}/Downloads/documents/"
others_dir = f"/Users/{user}/Downloads/others/"
software_dir = f"/Users/{user}/Downloads/software/"

# Directories List
folders_to_create = [media_dir, documents_dir, others_dir, software_dir]

# Cron Vairables
python_path = sys.executable
script_path = os.path.realpath(__file__)
cron = CronTab(user=user)
command = f"{python_path} {script_path}"
minute = f"* * * * * {command}"
hourly = f"0 * * * * {command}"
daily = f"0 0 * * * {command}"
monthly = f"0 0 1 * * {command}"

# category by file types
doc_types = (".doc", ".docx", ".txt", ".pdf", ".xls", ".ppt", ".xlsx", ".pptx")
media_types = (".jpg", ".jpeg", ".png", ".svg", ".gif", ".tif", ".tiff")
software_types = (".exe", ".pkg", ".dmg")


def create_dir(directories: list):
    if type(directories) != list:
        raise TypeError("Must be a list!")
    try:
        for folder in directories:
            if not os.path.isdir(folder):
                os.mkdir(folder)
    except OSError as error:
        print(error)


def get_files(root_dir):
    files = []
    for file in os.listdir(root_dir):
        if os.path.isfile(root_dir + file) and not file.startswith("."):
            # print('ITS WORKING')
            files.append(file)
    return files


def move_files(files):
    for file in files:
        # file moved and overwritten if already exists
        if file.endswith(doc_types):
            if os.path.isfile(documents_dir + file):
                old_file_name = file
                file = handle_dupe_files(documents_dir, file)
                os.rename(root_dir + old_file_name, root_dir + file)
            move(root_dir + file, documents_dir)
            click.secho(f"file {file} moved to {documents_dir}", fg="green")
        elif file.endswith(media_types):
            if os.path.isfile(media_dir + file):
                old_file_name = file
                file = handle_dupe_files(media_dir, file)
                os.rename(root_dir + old_file_name, root_dir + file)
            move(root_dir + file, media_dir)
            click.secho(f"file {file} moved to {media_dir}", fg="red")
        elif file.endswith(software_types):
            if os.path.isfile(software_dir + file):
                old_file_name = file
                file = handle_dupe_files(software_dir, file)
                os.rename(root_dir + old_file_name, root_dir + file)
            move(root_dir + file, software_dir)
            click.secho(f"file {file} moved to {software_dir}", fg="blue")
        else:
            if os.path.isfile(others_dir + file):
                old_file_name = file
                file = handle_dupe_files(others_dir, file)
                os.rename(root_dir + old_file_name, root_dir + file)
            move(root_dir + file, others_dir)
            click.secho(f"file {file} moved to {others_dir}", fg="magenta")


def handle_dupe_files(dir, file):
    count = 1
    split_array = file.split(".")
    file_extension = "." + split_array[1]
    begins_with = split_array[0]
    new_file_name = begins_with + "_" + str(count) + file_extension
    while os.path.isfile(dir + new_file_name):
        count += 1
        new_file_name = begins_with + "_" + str(count) + file_extension
    return new_file_name


def main():
    create_dir(folders_to_create)
    files = get_files(root_dir)
    move_files(files)


def cron_min():
    commands = cron.find_command(command)
    exists = False
    for job in commands:
        if str(job) == minute:
            print("crontab job actually exists", item)
            exists = True
            break
    if not exists:
        job = cron.new(command=command)
        job.minute.every(1)
        job.enable()
        cron.write()
        print("crontab does not exist and added successfully!")


def cron_hour():
    commands = cron.find_command(command)
    exists = False
    for job in commands:
        if str(job) == hourly:
            print("crontab actually exists", item)
            exists = True
            break
    if not exists:
        job = cron.new(command=command)
        job.hour.every(1)
        job.enable()
        cron.write()
        print("crontab does not exist and added successfully!")
