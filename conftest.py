import os
import zipfile


path_zip = os.path.join(os.path.abspath('resources'), 'zip_for_test')
with zipfile.ZipFile(path_zip, 'r') as archive:
    for file in archive.namelist():
        if file.endswith('pdf'):
            print(file)
        elif file.endswith('csv'):
            print(file)
        elif file.endswith('xls'):
            print(file)