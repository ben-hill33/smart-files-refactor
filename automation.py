import os
from shutil import move
from pathlib import Path

user = os.getenv('USER')

root_dir = f'/Users/{user}/Downloads/'

media_dir = f'/Users/{user}/Downloads/media/'

documents_dir = f'/Users/{user}/Downloads/documents/'

others_dir = f'/Users/{user}/Downloads/others/'

software_dir = f'/Users/{user}/Downloads/software/'


# category by file types
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
media_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

folders_to_create = [root_dir, media_dir,
                     documents_dir, others_dir, software_dir]


def create_dir(directories: list):
    if type(directories) != list:
        raise TypeError('Must be a list!')
    try:
        for folder in directories:
            if not os.path.isdir(folder):
                os.mkdir(folder)
    except OSError as error:
        print(error)


def get_files(root_dir):
    files = []
    for file in os.listdir(root_dir):
        if os.path.isfile(root_dir + file) and not file.startswith('.'):
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
            print(f"file {file} moved to {documents_dir}")
        elif file.endswith(media_types):
            if os.path.isfile(media_dir + file):
                old_file_name = file
                file = handle_dupe_files(media_dir, file)
                os.rename(root_dir + old_file_name, root_dir + file)
            move(root_dir + file, media_dir)
            print(f"file {file} moved to {media_dir}")
        elif file.endswith(software_types):
            if os.path.isfile(software_dir + file):
                old_file_name = file
                file = handle_dupe_files(software_dir, file)
                os.rename(root_dir + old_file_name, root_dir + file)
            move(root_dir + file, software_dir)
            print(f"file {file} moved to {software_dir}")
        else:
            if os.path.isfile(others_dir + file):
                old_file_name = file
                file = handle_dupe_files(others_dir, file)
                os.rename(root_dir + old_file_name, root_dir + file)
            move(root_dir + file, others_dir)
            print(f"file {file} moved to {others_dir}")


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

def check_if_job_exists(job):
    python_path = sys.executable
    script_path = os.path.realpath(__file__)
    command = f"{python_path} {script_path}"

    if str(job) == f"* * * * * {command}":
        print("Every minute crontab already exists", item)
        return True
    elif str(job) == f"0 * * * * {command}":
        print("Hourly crontab job already exists", item)
        return True
    elif str(job) == f"0 0 * * * {command}":
        print("Daily crontab job already exists", item)
        return True
    elif str(job) == f"0 0 1 * * {command}":
        print("Monthly crontab job already exists", item)
        return True

    return False


def cron_min():
    python_path = sys.executable
    script_path = os.path.realpath(__file__)
    cron = CronTab(user=user)
    command = f"{python_path} {script_path}"
    commands = cron.find_command(command)
    exists = False
    for item in commands:
        if str(item) == f"* * * * * {command}":
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
    python_path = sys.executable
    script_path = os.path.realpath(__file__)
    cron = CronTab(user=user)
    command = f"{python_path} {script_path}"
    commands = cron.find_command(command)
    exists = False
    for item in commands:
        if str(item) == f"0 * * * * {command}":
            print("crontab actually exists", item)
            exists = True
            break
    if not exists:
        job = cron.new(command=command)
        job.hour.every(1)
        job.enable()
        cron.write()
        print("crontab does not exist and added successfully!")
