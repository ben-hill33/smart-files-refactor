import os
from shutil import move


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
    # lets create a function that creates files labeled above if they don't already exist
    try:
        for folder in directories:
            if not os.path.isdir(folder):
                os.mkdir(folder)

    except OSError as error:
        print(error)


# def get_non_hidden_files_except_current_file(root_dir):
#     return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]

def get_files(root_dir):
    files = []
    for file in os.listdir(root_dir):
        print(file)
        if os.path.isfile(root_dir + file):
            print('ITS WORKING')
            files.append(file)
    return files


def move_files(files):
    for file in files:
        # file moved and overwritten if already exists
        if file.endswith(doc_types):
            move(file, '{}/{}'.format(documents_dir, file))
            print('file {} moved to {}'.format(file, documents_dir))
        elif file.endswith(media_types):
            move(file, '{}/{}'.format(media_dir, file))
            print('file {} moved to {}'.format(file, media_dir))
        elif file.endswith(software_types):
            move(file, '{}/{}'.format(software_dir, file))
            print('file {} moved to {}'.format(file, others_dir))
        else:
            move(file, '{}/{}'.format(others_dir, file))
            print('file {} moved to {}'.format(file, others_dir))


if __name__ == "__main__":
    create_dir(folders_to_create)
    # print(os.listdir(root_dir))
    files = get_files(root_dir)

    # files = get_non_hidden_files_except_current_file(root_dir)
    # print(files)
    move_files(files)
