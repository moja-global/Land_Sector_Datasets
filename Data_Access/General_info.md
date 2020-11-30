## FLINT ready processed datasets

## Tabel of contents
* [General info](#general-info)
* [Data access](#data-access)
* [Data format](#data-format)
* [Geoprocessing](#geoprocessing)
* [Source and Licencing](#source-and-licencing)


## General info
Vector and raster datasets are processed to be FLINT ready. This repository will be continually updated as new datasets become available.

## Data access
Processed datasets can be accessed from a temporary google drive FLINT_Landsector_datasets - Google Drive (https://drive.google.com/drive/folders/1hFA1tnh6s3W-RyC2LCzrs_1FmKEtzc8o?usp=sharing")

## Data format
### Vector
All spatial vector datasets are processed to geojson from original format.\
Format: .geoJSON/.JSON\
Geometry: Polygon (no point or line), No Z Values\
Coordinate System: EPSG 4326 (GCS_WGS_1984)\
Topology: Free from geometrical error such as self-intersection and no overlaps.

### Raster
All raster datasets have been proessed to tiff/geotiff from original format.\
Format: .tiff\
Coordinate System: EPSG 4326 (GCS_WGS_1984)\
Unit: Degrees\
Pixel size of 0.00025 decimal degrees\
Pixel depth: TBA\
No Data: TBA

## Geoprocessing
Geoprocessing code is/will be provided for each dataset. See folder 'geoprocessing'. Most processing has been completed in arcpy, but can be converted to qgis and gdal.

## Source and licencing
Original data sources and licence information for each dataset is provided.

