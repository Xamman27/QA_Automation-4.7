import os
import zipfile
#simple_zip_pdf = zipfile.ZipFile(os.path.abspath('resources'),'w')
#print(os.path.join(os.path.dirname('QA_Automation-4.7'), 'resources'))
#zip_pdf = zipfile.ZipFile(os.path.join(os.path.abspath('resources'), 'zip_pdf'))
#zip_pdf.write(os.path.join(os.path.abspath('resources'), 'pdf_example'))

with zipfile.ZipFile(os.path.join(os.path.abspath('resources'),'archive'),'w') as zf:
    zf.write(os.path.join(os.path.abspath('resources')),'pdf_exapmple')