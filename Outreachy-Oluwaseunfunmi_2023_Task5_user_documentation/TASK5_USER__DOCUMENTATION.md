## LAND SECTOR MANAGEMENT, EXPLORATORY DATA ANALYSIS, ATTRIBUTE MAPPING, AND GEOSPATIAL ANALYSIS USER GUIDE

## INTRODUCTION
Charting the Path to Sustainability: Integrating Land Sector Data with Sustainable Development Goals project offers a meaningful opportunity to bridge land sector data with global sustainability targets, empowering users to make data-driven decisions aligned with broader development objectives.
This user guide is dedicated to SDGs mapping and attribute assessment, followed by the development of mapping mechanisms, visualization design.

## TABLE OF CONTENTS
**TASK 1: LAND SECTOR MANAGEMENT AND EXPLORATORY DATA ANALYSIS**
**TASK 2: ATTRIBUTE-SDG MAPPING PROTOTYPE**
**TASK 3: GEOSPATIAL ANALYSIS**
**TASK 4: VISUALIZATION PROTOTYPE**

## TASK 1: LAND SECTOR MANAGEMENT AND EXPLORATORY DATA ANALYSIS
**Aim: bringing together datasets that can be useful for land sector management.**
- A  given country/region/province/state/city was selected from the Land Sector Data repository. In this case, Nigeria and Oyo state dataset was selected.
- **Libraries imported** include: GeoPandas, Matplotb, Numpy, and Rasterio
- **Dataset**: Administrative boundary, planted forest, soil types, geoecological zones, climate, Biodiversity hotspot
- Each dataset was imported into jupyter notebook environment, data exploration, visualization and analysis was carried out on the corresponding data
- The task was uploaded to github.

## TASK 2: ATTRIBUTE-SDG MAPPING PROTOTYPE

- Land Sector repository was fork and clone to the computer
- Preferred dataset (soil, climate, geoecological zones) was selected from the data library
- A prototype was developed for mapping specific attributes from the preferred dataset to two (2) relevant SDGs.
- Soil data was mapped to SDG 2: Zero hunger and SDG 15: Life on land, Climate zone data was mapped to SDG 6: Clean Water and Sanitation, and geoecological zone dataset was mapped to SDG 14: Life below water and SDG 15: life on Land.
- Mapping function was created and applied. Then the mapping was visualized using bar charts.
- Documentation was done for mapping explanation and the result obtained.
- The newly mapped dataset and updated documentation was committed, signed off using **git commit -s -m** , and pushed to github using **git push origin master** and a new pull request was raised.

## TASK 3: GEOSPATIAL ANALYSIS

- Geospatial analysis is carried out on the dataset imported into jupyter notebook environment to identify patterns or trends.
- Libaries imported are: pandas, geopandas, matplotlib, seaborn, shapely.geometry
- On biodiversity hotspot data, geospatial analysis carried out include spatial query, perimeter and area analysis, density analysis, hotspot analysis, spatial autocorrelation.
- Data visualization is done using Histogram,bar chat, box plot, scatter plot, choropleth map.
- On soil dataset, univariate analysis, Spatial Overlay of World Soil Resources on Biodiversity Hotspots was done.
- Data was visualized using barchat, pie chart, choropleth map
- Brief report on spatial patterns or correlations discovered was documented.
- The task was committed, signed off and pushed to github.

## TASK 4: VISUALIZATION PROTOTYPE
    
- Libaries imported are: geopandas, matplotlib, seaborn, plotly, pandas.
- A prototype for the data visualization component was developed
- data visualization that represent the mapped relationships between land attributes and SDGs was created and represented using heat map, bar chat, box plot, pie chart, stacked bar plot, and scatter plot.
- The task was committed, signed off and pushed to github.