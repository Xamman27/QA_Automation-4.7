import os
import zipfile

path_to_zip = os.path.abspath('files_for_test')
file_to_zip = os.listdir(path_to_zip)

with zipfile.ZipFile(os.path.join(os.path.abspath('resources'), 'zip_for_test'), 'w') as zf:
    for file in file_to_zip:
        add_file = os.path.join(path_to_zip, file)
        zf.write(add_file)
