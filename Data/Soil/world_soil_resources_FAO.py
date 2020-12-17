# World Soil Resources Base Map FAO 2014

# Processed data access Access: https://drive.google.com/drive/folders/1HHpzw8ySHv3-SkSw9aIJrJTpAFVIQpaP  Folder: /World_datasets/Soil

=====================================

# Data source
#Original spatial data sourced from: http://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/other-global-soil-maps-and-databases/
#World Soil Resources Coverage in Geographic Projection (ARC/Info Export format) "wsrll"
#Reports: http://www.fao.org/soils-portal/data-hub/soil-classification/world-reference-base/en/

# Description
#The World Resource Base Map of World Soil Resources is available at 1:25 000 000 scale. This is the most general digital map of the World's soils, now using the international standard soil classification WRB. Available as a graphic or digital coverage.
#Soil Type underpins the processes for estimating the changes in SOC as a result of changes to land use. Soil Type, when used in conjunction with climate data, is used for determining the IPCC Tier 1 SOC reference levels.

# Licence
#FAO encourages the use, reproduction and dissemination of material in this information product. Except where otherwise indicated, material may be copied, downloaded and
#printed for private study, research and teaching purposes, or for use in non-commercial products or services, provided that appropriate acknowledgement of FAO as the source
#and copyright holder is given and that FAO’s endorsement of users’ views, products or services is not implied in any way.
#All requests for translation and adaptation rights, and for resale and other commercial use rights should be

# Attribution
#IUSS Working Group WRB. 2015. World Reference Base for Soil Resources 2014, update 2015. International soil classification system for naming soils and creating legends for soil maps. World Soil Resources Reports No. 106. FAO, Rome.

# Coordinate system EPSG: 4326 (GCS_WGS_1984)

# Pre-processing: Check Topology - manual in GIS, remove overlaps, fix gaps

=====================================

# Geoprocessing: Repair geometry (ArcGIS or QGIS) & convert to geojson

# Import arcpy module
import arcpy, os

# Local variables:
input = "C:/folder/wsrll.shp"
Output_Coordinate_System = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
output = "C:/folder/world_soil_resources_wgs84.geojson"

# Process: Repair Geometry
arcpy.RepairGeometry_management(input, "DELETE_NULL")

# Process: Features To JSON
arcpy.env.outputCoordinateSystem = Output Coordinate System
arcpy.FeaturesToJSON_conversion(input, output, "NOT_FORMATTED", "NO_Z_VALUES", "NO_M_VALUES", "GEOJSON")
Output_has_Z_Values = "Disabled"
