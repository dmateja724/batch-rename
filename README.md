# batch-rename

Small app to batch rename and move video files created by Windows Captures.

The main use for this app was spawned because of the way Windows Captures and COD: MW generated file names for captures taken, and not being able to be uploaded to a NextCloud server.

There is a unicode character that gets added to the file name, that causes the file name to evaluate to a very long string (passed the character count limits). This apps purpose is to find those unicode encoded files names and rename them appropriately and then save them in unique folders.

Once the file names have been converted and organized into folders, it will then move over into the NextCloud directory to be backed up.

## To run the App

1. open terminal
2. navigate to this folder/file
3. open `batch-rename.py`
4. under `user_name` enter the username you use for windows
   - navigate to C:\Users and use the name of the folder associated with your account
5. type `python batch-rename.py` at the command prompt

## TODO:

- this is specific to unicode and COD file names and could possibly configure this to work on other types of files if the need arises
- when moving folders into the final destination
  - check if folder already exists
  - if it does then just add the files inside to the
    already existing one
- refactor function calls
- set directories dynamically instead of hardcoded values
