## Data general info

## Tabel of contents
* [General info](#general-info)
* [Data access](#data-access)
* [Data format](#data-format)
* [Geoprocessing](#geoprocessing)
* [Source and Licencing](#source-and-licencing)

## General info
Vector and raster land sector datasets are processed from multiple sources with the intention to be FLINT ready. This repo will contain source, licence and geoprocessing info on each dataset and processed data is available via #data-access. This repository will be continually updated as new datasets become available.

## Data access
Processed datasets can be accessed from moja-global Land Sector Datasets - Google Drive (https://drive.google.com/drive/folders/1HHpzw8ySHv3-SkSw9aIJrJTpAFVIQpaP?usp=sharing)

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
Pixel size: no restriction\
Pixel depth: TBA\
No Data: TBA

## Geoprocessing
Geoprocessing code is/will be provided for each dataset. See folder 'geoprocessing'. Most processing has been completed in arcpy, but can be converted to qgis and gdal.

## Source and licencing
Original data sources and licence information for each dataset is provided.
