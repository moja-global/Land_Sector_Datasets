# A script to rasterise a shapefile to the same projection & pixel resolution as a reference image.
from osgeo import ogr, gdal
import subprocess
import os

ogr.UseExceptions()
gdalformat = 'GTiff'
datatype = gdal.GDT_Byte
burn_val = 1 #value for the output image pixels


output_image = 'ProbaV_UTM_LC100_biome_clusters_V3_global.tif'
current_directory = os.getcwd()
input_vector = os.path.join(current_directory, r'tmp_unzip_path/biome_cluster_shapefile/ProbaV_UTM_LC100_biome_clusters_V3_global.shp')
ref_image = os.path.join(current_directory, r'ref_data/WaterScarcity_GAEZ.tif')

def read_files(input_vector, ref_image):
    if not os.path.exists(input_vector):
        print("Input vector does not exist")
    else:
        Image = gdal.Open(ref_image, gdal.GA_ReadOnly)
        if Image == None:
            print("Unable to read the reference data file")
        else:
            try:
                Shapefile = ogr.Open(input_vector)
                if Shapefile:
                    Shapefile_layer = Shapefile.GetLayer()
                    convert_shp_to_tiff(Image,output_image,Shapefile_layer)
                else:
                    print("Couldn't load shapefile")
            except Exception as e:
                print(e)

def convert_shp_to_tiff(Image,output_image,Shapefile_layer):
    print("Rasterising shapefile...")
    Output = gdal.GetDriverByName(gdalformat).Create(output_image, Image.RasterXSize,
    Image.RasterYSize, 1, datatype, options=['COMPRESS=DEFLATE'])
    Output.SetProjection(Image.GetProjectionRef())
    Output.SetGeoTransform(Image.GetGeoTransform())

    # Write data to band 1
    Band = Output.GetRasterBand(1)
    Band.SetNoDataValue(0)
    gdal.RasterizeLayer(Output, [1], Shapefile_layer, burn_values=[burn_val])

    # Close datasets
    Band = None
    Output = None
    Image = None
    Shapefile = None

read_files(input_vector, ref_image)

