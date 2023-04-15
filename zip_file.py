import os
import zipfile
import pytest
import csv


def test_mk_zip_archive(): #создаем архив в папке resources
    path_files_for_test = os.path.abspath('files_for_test')
    with zipfile.ZipFile(os.path.join(os.path.abspath('resources'), 'zip_for_test'), 'w') as zf:
        file_to_zip = os.listdir(path_files_for_test) #список файлов в архив из папки files_for_test
        for file in file_to_zip:
            add_file = os.path.join(path_files_for_test, file)
            zf.write(add_file)
        assert str(zf).endswith('zip_for_test')

def test_csv():
    with zipfile.ZipFile(os.path.join(os.path.abspath('resources'), 'zip_for_test'), 'r') as archive:
        for file in archive.namelist():
            if file.endswith('csv'):
                print(file)







