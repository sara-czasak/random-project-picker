import os


def check_if_path(path):
    if os.path.exists(path):
        return True
    else:
        return False
