import arcpy
import os
import sys
import subprocess
import wget
import zipfile
import datetime

# implement pip as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
#'gdal-utils'])

wget.download('https://databasin2-filestore.s3.amazonaws.com/68635d7c77f1475f9b6c1d1dbe0a4c4c/download/68635d7c77f1475f9b6c1d1dbe0a4c4c_1_lpk_en.zip?Signature=I2CF0MsszsnEffGoZQdxRIP3sRE%3D&Expires=1685952584&AWSAccessKeyId=AKIAI4RK5BEPK3FCQPUQ')


zipfile.ZipFile('Terrestrial Ecoregions of the World.zip').extractall()

zipfile.ZipFile('Terrestrial Ecoregions of the World.zip').close()

#folder of feature classes to process
in_folder = r"C:\data\terrestrial_ecosystems"
scr_folder = os.path.join(in_folder, "scratch.gdb")
workspace = in_folder
out_folder = r"C:\data\json"
outjson = os.path.join(out_folder, fcname)

# Set environments
arcpy.env.workspace = workspace
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
arcpy.env.outputZFlag = "Disabled"
arcpy.env.overwriteOutput = True

# Execute CreateFileGDB
scr = arcpy.CreateFileGDB_management(in_folder, "scratch")

featureclasses = arcpy.ListFeatureClasses()
    
print(featureclasses)

# Iterate through all datasets, repair and convert to json
for fc in featureclasses:
    fcname = os.path.join(os.path.splitext(fc)[0])
        
    # Process: Make Feature Layer (Make Feature Layer) (management)
    fLayer = "project_Layer"
    arcpy.management.MakeFeatureLayer(fc, fLayer)
    
    # Process: Union - fill gaps and find overlaps
    projectUnion = os.path.join(scr_folder, "projectUnion")
    arcpy.analysis.Union(fLayer, projectUnion, "ALL", None, "NO_GAPS")

    # Process: Multipart To Singlepart - explode into single parts
    projectUnionSingle = os.path.join(scr_folder, "projectUnionSingle")
    arcpy.management.MultipartToSinglepart(projectUnion, projectUnionSingle)
        
    # Process: Select - select overlaps and slithers smaller than 0.00001 degrees (this may need to be checked)
    unionSelect = os.path.join(scr_folder, "unionSelect")
    arcpy.analysis.Select(projectUnionSingle, unionSelect, "Shape_Area <= 0.000006")
    
    # Process: Dissolve - dissolve slithers and overlaps to single features
    dissolveSlither = os.path.join(scr_folder, "dissolveSlither")
    arcpy.management.Dissolve(unionSelect, dissolveSlither, None, None,"SINGLE_PART")

    # Process: Erase overlaps
    removeSlither = os.path.join(scr_folder, "removeSlither")
    arcpy.analysis.Erase(fLayer, dissolveSlither, removeSlither)

    # Process: Append small slithers and gap fills to be merged into coincident polygons with largest boundary
    appendSlither = arcpy.management.Append(dissolveSlither, removeSlither, "NO_TEST")
     
    # Process: Eliminate slither by merge into coincident polygons with largest boundary
    eliminateSlither = os.path.join(scr_folder, "eliminateSlither")
    selectSlither = arcpy.management.SelectLayerByAttribute(appendSlither, "NEW_SELECTION", "OBJECTID IS NULL")
    arcpy.management.Eliminate(selectSlither, eliminateSlither, "LENGTH")
    print('repairing...')
    
    # Process: Repair Geometry (non-simple geometry)
    geomRepair = arcpy.management.RepairGeometry(eliminateSlither, "DELETE_NULL", "OGC")[0]
    
    # Process: Features To JSON
    arcpy.conversion.FeaturesToJSON(eliminateSlither, outjson, "NOT_FORMATTED", "NO_Z_VALUES", "NO_M_VALUES", "GEOJSON", "WGS84", "USE_FIELD_NAME")
    
    print(outjson, ' json complete')
    
arcpy.Delete_management(scr_folder)
arcpy.AddMessage("All done!")
print('done')

a_file = open("preprocess.py", "r")
value = datetime.datetime.now()
date_string = value.strftime('# %Y-%m-%d %H-%M-%S.%f')
list_of_lines = a_file.readlines()
list_of_lines[96] = date_string
a_file = open("preprocess.py", "w")
a_file.writelines(list_of_lines)
a_file.close()

