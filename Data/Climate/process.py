import sys
import subprocess
import wget
import zipfile
import datetime
import os


# Download the zip file
zip_url = 'https://esdac.jrc.ec.europa.eu/projects/RenewableEnergy/Data/Climate_Zone.zip'
zip_file_path = wget.download(zip_url)

zipfile.ZipFile('Climate_Zone.zip').extractall()

zipfile.ZipFile('Climate_Zone.zip').close()

# Convert from .rst to tif and apply WGS84 and resample to 0.005
gdalwarp_cmd = 'gdalwarp -s_srs EPSG:4326 -t_srs EPSG:4326 -dstnodata 255.0 -tr 0.05 0.05 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff "CLIMATE_ZONE.rst" "IPCC_ClimateZoneMap.tif"'
os.system(gdalwarp_cmd)

# Convert to polygon
gdal_polygonize_cmd = 'python3 -m gdal_polygonize IPCC_ClimateZoneMap.tif IPCC_ClimateZoneMap.geojson -b 1 -f "GeoJSON" IPCC_ClimateZoneMap CLASS_NAME'
os.system(gdal_polygonize_cmd)

# Check Topology - Run fix geometries in QGIS
qgis_cmd = 'qgis --nologo --code "import processing\n\nparams = {\'INPUT\': \'IPCC_ClimateZoneMap.geojson\', \'OUTPUT\': \'Fixed_ClimateZoneMap.geojson\'}\nprocessing.run(\'native:fixgeometries\', params)"'
os.system(qgis_cmd)

# Update the "process.py" file with a timestamp
a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[37] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()
# 2023-06-08 07-56-27.600821