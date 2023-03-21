import sys
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])

wget.download('https://drive.google.com/uc?export=download&id=1K4nd7alzdwMQ4lOzC8wNewKU61dxncnr')


a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[19] = date_string
a_file = open("process.py", "w")
# 2023-03-21 09-58-43.906334