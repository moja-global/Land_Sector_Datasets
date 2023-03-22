import sys
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])

#run the below code in terminal with updated link and credentials to download the original dataset
#wget --auth-no-challenge --user=ImaJin --password=junior$$14 "https://databasin2-filestore.s3.amazonaws.com/a4cb6d367eae4e52a08902874f8bfedf/download/a4cb6d367eae4e52a08902874f8bfedf_1_zip_en.zip?Signature=ne2Aa6KK3wnmbjRWPPNV0TTecMw%3D&Expires=1679157927&AWSAccessKeyId=AKIAI4RK5BEPK3FCQPUQ" 



zipfile.ZipFile('Global Soil Organic Carbon Density in kg Carbon_m2 to 1 meter depth.zip').extractall()

zipfile.ZipFile('Global Soil Organic Carbon Density in kg Carbon_m2 to 1 meter depth.zip').close()

a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[25] = date_string
a_file = open("process.py", "w")
# 2023-03-22 22-22-07.682378