# Land Sector Datasets
This Repo is bringing together datasets that can be useful for land sector management. The range of datasets is going beyond what is needed to run FLINT. For each dataset information is provided on content and licence.


## Maintainers Reviewers Ambassadors Coaches

The following people are Maintainers Reviewers Ambassadors or Coaches

<table><tr><td align="center"><a href="https://github.com/gmajan"><img src="https://avatars0.githubusercontent.com/u/8733319?v=4" width="100px;" alt="Guy Janssen"/><br /><sub><b>Guy Janssen</b></sub></a><br /><a href="#maintenance-gmajan" title="Maintenance">🚧</a></td><td align="center"><a href="https://github.com/mtbdeligt"><img src="https://avatars3.githubusercontent.com/u/16447169?v=4" width="100px;" alt="mtbdeligt"/><br /><sub><b>mtbdeligt</b></sub></a><br /><a href="https://github.com/moja-global/About-moja-global/commits?author=mtbdeligt" title="Documentation">📖</a></tr></table>

**Maintainers** review and accept proposed changes  
**Reviewers** check proposed changes before they go to the Maintainers  
**Ambassadors** are available to provide training related to this repository  
**Coaches** are available to provide information to new contributors to this repository  

## Processed datasets
FLINT ready processed vector (json) and raster/grid (tiff) data described in this repo can be downloaded from Moja Global[Land Sector Datasets](https://datasets.mojaglobal.workers.dev/) data library.

### Formats
To be FLINT ready, vector datasets must be in geoJSON vector format, with no overlapping parts or topological error such as self intersections. Code is provided to systematically process the original data sources into this format, but please note this may change the content of the data e.g. where there are two overlapping polygons with different attribution, one will arbitrarily win over the other. We have also attempted to clean up small gaps and slithers systematically, but it is still recommended that manual checking and editing is completed depending on your project requirements.

To be FLINT ready, rasters or grids must be in tiff or geoTiff format, with the same extent and resolution equal to or a multiple of the overall simulation resolution, padded to the nearest 1 degree lat/lon. These can be mosaic or tiled. We provide gdal code to resample the grids and tiles to different extents and resolutions. There are a range of continous and discrete grids available in the data library.

## Licence information
Please review individual dataset licence terms and conditions. Please note, while all care has been taken to ensure data is open data available for use, individual datasets will have their own licence conditions and citation requirements.
