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
FLINT ready processed vector (json) and raster/grid (tiff) data described in this repo can be downloaded from Moja Global [Land Sector Datasets](https://datasets.mojaglobal.workers.dev/) data library.

### Formats
To be FLINT ready, vector datasets must be in geoJSON vector format, with no overlapping parts or topological error such as self intersections. Code is provided to systematically process the original data sources into this format, but please note this may change the content of the data e.g. where there are two overlapping polygons with different attribution, one will arbitrarily win over the other. We have also attempted to clean up small gaps and slithers systematically, but it is still recommended that manual checking and editing is completed depending on your project requirements.

To be FLINT ready, rasters or grids must be in tiff or geoTiff format, with the same extent and resolution equal to or a multiple of the overall simulation resolution, padded to the nearest 1 degree lat/lon. These can be mosaic or tiled. We provide gdal code to resample the grids and tiles to different extents and resolutions. There are a range of continous and discrete grids available in the data library.

## Licence information
Please review individual dataset licence terms and conditions. Please note, while all care has been taken to ensure data is open data available for use, individual datasets will have their own licence conditions and citation requirements.

## Community Analyses

| [![Example 01](example_thumbnail.png)](https://nbviewer.org/github/derha/moja-global/blob/main/carpathian_montane_forests.ipynb) | -
| [![Example 02](example_thumbnail.png)](https://nbviewer.org/github/Shubhams-2002/MojaGlobalDatasets/blob/main/Moja_global_datasets_done.ipynb) | -
| [![Example 03](example_thumbnail.png)](https://nbviewer.org/github/Shubhams-2002/MojaGlobalDatasets/blob/main/WesternGhats.ipynb) | -
| [![Example 04](example_thumbnail.png)](https://nbviewer.org/github/thushariii/MojaGlobal2022/blob/main/sinharaja_Rain_forest.ipynb) | 

| [![Example 05](example_thumbnail.png)](https://nbviewer.org/github/coloeus-monedula/moja-global-22/blob/main/forest.ipynb) | -
| [![Example 06](example_thumbnail.png)](https://nbviewer.org/github/maazingly/Outreachy-mojaglobal-EDA-NZ/blob/main/Geo%20EDA%20-%20New%20Zealand.ipynb) | -
| [![Example 07](example_thumbnail.png)](https://nbviewer.org/github/Iman-L/Outreachy_iman_linje_2022/blob/main/2.%20Forest%20Types%20of%20Malawi.ipynb) | -
| [![Example 08](example_thumbnail.png)](https://nbviewer.org/github/aldeav/Outreachy_Ananyashree_2022/blob/main/1_Data_Analysis.ipynb) |

| [![Example 09](example_thumbnail.png)](https://nbviewer.org/github/mHienp/mojaglobal/blob/main/Yukon%20Interior%20dry%20forests.ipynb) | -
| [![Example 10](example_thumbnail.png)](https://nbviewer.org/github/Boluwape/Outreachy_Boluwape_2022./blob/main/2022-10_Contribution-Outreachy/Moja_Global_Datasets_Crossriver_Forest_In_Nigeria.ipynb) | -
| [![Example 11](example_thumbnail.png)](https://nbviewer.org/github/Boluwape/Outreachy_Boluwape_2022./blob/main/Growth_curves_data.ipynb) | -
| [![Example 12](example_thumbnail.png)](https://nbviewer.org/github/Hafsah2020/Outreachy_Hafsah_Anibaba_2022/blob/main/favourite_forest_analysis.ipynb) | 

| [![Example 13](example_thumbnail.png)](https://nbviewer.org/github/Hafsah2020/Outreachy_Hafsah_Anibaba_2022/blob/main/global_forest_analysis.ipynb) | -
| [![Example 14](example_thumbnail.png)](https://nbviewer.org/github/saranda-2811/moja-global22/blob/main/cite.ipynb) | -
| [![Example 15](example_thumbnail.png)](https://nbviewer.org/github/saranda-2811/moja-global22/blob/main/moja_global_forest1.ipynb) | -
| [![Example 16](example_thumbnail.png)](https://nbviewer.org/github/anamika-yadav99/moja-global_task/blob/main/Forest_analysis.ipynb) |

| [![Example 17](example_thumbnail.png)]() | -
| [![Example 18](example_thumbnail.png)]() | -
| [![Example 19](example_thumbnail.png)]() | -
| [![Example 20](example_thumbnail.png)]() |

| [![Example 21](example_thumbnail.png)]() | -
| [![Example 22](example_thumbnail.png)]() | -
| [![Example 23](example_thumbnail.png)]() | -
| [![Example 24](example_thumbnail.png)]() |
