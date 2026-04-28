from func import *
import string
import os


valid_file_extensions = ['txt', 'doc', 'odt']

files_to_merge = []
has_file_paths = False
while not has_file_paths:
    file = input('Please enter file path of file to be merged: ')
    if check_if_path(file):
        if file.split('.')[-1] in valid_file_extensions:
            files_to_merge.append(file)
            check = input('Would you like to add another file to merge? (y/n): ')
            if 'n' in check.lower():
                has_file_paths = True
        else:
            print('Error: Invalid file extension.')
    else:
        print('Error: Invalid file path.')


chars_not_accepted = list(string.punctuation)
chars_not_accepted.append('\n')
chars_not_accepted.append(' ')
chars_not_accepted.remove('_')

name = ''
name_picked = False
while not name_picked:
    name = input('Please enter name you would like to use for merged file (A-Z, a-z, _, 1-9): ')
    if any(i in name for i in chars_not_accepted):
        print('Error: Invalid character(s).')
    else:
        name_picked = True


path = input('Please enter path where you want to save the merged file: ')
if not os.path.exists(path):
    os.makedirs(path)


with open(os.path.join(path, f"{name}.txt"), 'w') as merged_file:
    for i in files_to_merge:
        with open(i, 'r') as file:
            file_content = file.read()
            merged_file.write(f'{file_content}\n\n')
