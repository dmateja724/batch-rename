import os
import datetime

# TODO: for ease of use we'll want to create folders appropriate to the dates
# that the videos were created on for easy orgranization
# TODO: for ease of use as a option we'll want to push those folders after being
# renamed and put into folders


# this is the path to the folder where the videos are being held
now = datetime.datetime.now()
user_name = 'dmate'
dir = f'C:\\Users\\{user_name}\\Videos\\Captures'
move_dir = ' '


# this function will check the string passed in if each character is an
# ascii character
def is_ascii(string):
    return all(ord(c) < 128 for c in string)

def rename_files(path, destination_path):
    os.rename(path, destination_path)

def create_new_folder_check(path):
    if not os.path.exists(path):
        os.mkdir(path)

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
            # destination_path = os.path.join(dir, folder_name, new_file_name)


            create_new_folder_check(folder_path)

            try:
               rename_files(path, destination_path)
            except Exception as err:
                print(err)

        else:
            pass
