import os
import zipfile
import csv


def mk_zip_archive(path_to_zip): #создаем архив в папке resources
    with zipfile.ZipFile(os.path.join(os.path.abspath('resources'), 'zip_for_test'), 'w') as zf:
        file_to_zip = os.listdir(path_to_zip) #список файлов в архив из папки files_for_test
        for file in file_to_zip:
            add_file = os.path.join(path_to_zip, file)
            zf.write(add_file)

#
#
# with zipfile.ZipFile(path_zip, 'r') as zfolder:
#      for i in zfolder.namelist():
#          print(i)
path_files_for_test = os.path.abspath('files_for_test')
mk_zip_archive(path_files_for_test)#функция архивирования файлов
path_zip = os.path.join(os.path.abspath('resources'), 'zip_for_test')