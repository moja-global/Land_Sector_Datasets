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
FLINT ready processed vector (json) and raster/grid (tiff) data described in this repo can be downloaded from Moja Global [Land Sector Datasets](https://datasets.mojaglobal.workers.dev) data library.

## Data format
### Vector
All spatial vector datasets are processed to geojson from original format.\
Format: .geoJSON/.JSON\
Geometry: Polygon, No Z Values\
Coordinate System: EPSG 4326 (GCS_WGS_1984)\
Topology: Free from geometrical error such as self-intersection and no overlaps.

### Raster
All raster datasets have been proessed to tiff/geotiff from original format.\
Format: .tiff\
Coordinate System: EPSG 4326 (GCS_WGS_1984)\
Unit: Degrees\
Pixel size: various but padded to the nearest 1 degree e.g. 0.001 or 0.00025
Tiled: various or mosaic
Pixel depth: various
No Data: various

## Geoprocessing
Geoprocessing code is/will be provided for each dataset. Most processing has been completed in arcpy or gdal, but can be converted to qgis.

## Source and licencing
Original data sources and licence information for each dataset is provided.
