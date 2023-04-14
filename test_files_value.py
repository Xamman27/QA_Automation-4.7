import pytest
import os
import csv
import zipfile

def test_csv():
    with zipfile.ZipFile(os.path.join(os.path.abspath('resources'), 'zip_for_test')) as zf:
        with zf.open('csv_example', 'r') as zfile:
            zfile = csv.reader(zfile)
            for r in zfile:
                print(r)



