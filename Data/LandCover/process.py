import sys
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])



wget.download('https://zenodo.org/record/5879022/files/FML_v3-2_with-colorbar.tif?download=1')




a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[25] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-04-15 00-39-59.996798