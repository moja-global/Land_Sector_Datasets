import sys
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])

wget.download('https://esdac.jrc.ec.europa.eu/projects/RenewableEnergy/Data/Climate_Zone.zip')


zipfile.ZipFile('Climate_Zone.zip').extractall()

zipfile.ZipFile('Climate_Zone.zip').close()

a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[25] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-06-03 08-08-58.731600