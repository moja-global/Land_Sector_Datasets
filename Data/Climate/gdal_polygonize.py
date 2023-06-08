import subprocess

input_raster = "IPCC_ClimateZoneMap.tif"
output_vector = "IPCC_ClimateZoneMap.geojson"
band_number = 1
output_format = "GeoJSON"
class_field = "CLASS_NAME"

# Build the command
command = [
    "gdal_polygonize.py",
    input_raster,
    "-b", str(band_number),
    "-f", output_format,
    output_vector,
    class_field
]

# Execute the command
subprocess.call(command)
