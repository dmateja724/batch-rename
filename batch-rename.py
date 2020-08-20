import os
import datetime
import shutil

# enter the username associated with your account
user_name = ''
folder_names = []
dir = f'C:\\Users\\{user_name}\\Videos\\Captures'
destination_dir = f'C:\\Users\\{user_name}\\Nextcloud\\COD Captures'
now = datetime.datetime.now()

# this function will check the string passed in if each character is an
# ascii character
def is_ascii(string):
    return all(ord(c) < 128 for c in string)

def rename_files(path, destination_path):
    os.rename(path, destination_path)

def create_new_folder_check(path):
    if not os.path.exists(path):
        os.mkdir(path)

def track_folders_created(folder_name):
    if not folder_name in folder_names:
        folder_names.append(folder_name)
    else:
        pass

def move_files():
    for folder_name in folder_names:
        home_path = os.path.join(dir, folder_name)
        shutil.move(home_path, destination_dir)

def encode_and_rename_files():
    with os.scandir(dir) as dir_entries:
        for entry in dir_entries:

            path = entry.path

            if not is_ascii(entry.name):
                encoded_file_name = entry.name.encode('ascii', 'ignore')
                decoded_file_name = encoded_file_name.decode()
                file_split = decoded_file_name.split(' ')
                new_file_name = file_split[5] + ' ' + file_split[6]
                folder_name = file_split[5].split(f'{now.year}-')[1]
                folder_path = os.path.join(dir, folder_name)
                destination_path = os.path.join(dir, folder_name, new_file_name)

                create_new_folder_check(folder_path)
                track_folders_created(folder_name)

                try:
                    rename_files(path, destination_path)
                except Exception as err:
                    print(err)
            else:
                pass

def main():
    if user_name == '':
        print('*******************************************')
        print('****** Please fill in the user_name  ******')
        print('******    at the top of this file    ******')
        print('*******************************************')
    else:
        encode_and_rename_files()
        move_files()

if __name__ == "__main__":
    main()