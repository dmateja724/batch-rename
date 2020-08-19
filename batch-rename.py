import os
import datetime

# TODO: for ease of use we'll want to create folders appropriate to the dates
# that the videos were created on for easy orgranization
# TODO: for ease of use as a option we'll want to push those folders after being
# renamed and put into folders


# this is the path to the folder where the videos are being held
now = datetime.datetime.now()
userName = 'dmate'
dir = f'C:\\Users\\{userName}\\Videos\\Captures'
currentDate = ''

# this function will check the string passed in if each character is an
# ascii character
def is_ascii(string):
    return all(ord(c) < 128 for c in string)


with os.scandir(dir) as dir_entries:
    for entry in dir_entries:
        path = entry.path


        if not is_ascii(entry.name):
            encodedFileName = entry.name.encode('ascii', 'ignore')
            decodedFileName = encodedFileName.decode()
            fileSplit = decodedFileName.split(' ')
            newFileName = fileSplit[5] + ' ' + fileSplit[6]
            folderName = fileSplit[5].split(f'{now.year}-')[1]
            newPath = os.path.join(dir, newFileName)

            if currentDate != folderName
            # try:
            #     os.mkdir()

            # this part works, uncomment when ready
            # try:
            #     os.rename(path, newPath)
            # except Exception as err:
            #     print(err)

        else:
            pass
