import os


def files_list(directory, ext):
    files_name = []
    for filename in os.listdir(directory):
        if filename.endswith(ext):
            files_name.append(filename)
    return files_name

