import sys
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])




zipfile.ZipFile('Global Soil Organic Carbon Density in kg Carbon_m2 to 1 meter depth.zip').extractall()

zipfile.ZipFile('Global Soil Organic Carbon Density in kg Carbon_m2 to 1 meter depth.zip').close()

a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[25] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-04-10 10-04-53.854162