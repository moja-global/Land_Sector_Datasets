import sys
import subprocess
import wget
import zipfile
import datetime
import os


# Download the zip file
zip_url = 'https://esdac.jrc.ec.europa.eu/projects/RenewableEnergy/Data/Climate_Zone.zip'
zip_file_path = wget.download(zip_url)

# Extract the zip file to a folder with the same name
folder_path = os.path.splitext(zip_file_path)[0]
os.makedirs(folder_path, exist_ok=True)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(folder_path)


# Convert from .rst to tif and apply WGS84 and resample to 0.005
gdalwarp_cmd = 'gdalwarp -t_srs EPSG:4326 -dstnodata 255.0 -tr 0.005 0.005 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff Climate_Zone/CLIMATE_ZONE.rst IPCC_ClimateZoneMap.tif'
os.system(gdalwarp_cmd)

# Convert to polygon
gdal_polygonize_cmd = 'gdal_polygonize.py IPCC_ClimateZoneMap.tif -b 1 -f "GeoJSON" IPCC_ClimateZoneMap.geojson IPCC_ClimateZoneMap CLASS_NAME'
os.system(gdal_polygonize_cmd)

# Check Topology - Run fix geometries in QGIS
qgis_cmd = 'qgis --nologo --code "import processing\n\nparams = {\'INPUT\': \'IPCC_ClimateZoneMap.geojson\', \'OUTPUT\': \'Fixed_ClimateZoneMap.geojson\'}\nprocessing.run(\'native:fixgeometries\', params)"'
os.system(qgis_cmd)

# Update the "process.py" file with a timestamp
a_file = open("process.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[41] = date_string
a_file = open("process.py", "w")
a_file.writelines(list_of_lines)
a_file.close()

