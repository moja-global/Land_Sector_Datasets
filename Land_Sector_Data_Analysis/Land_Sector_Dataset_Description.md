### Moja Global's Land Sector Dataset Description

In most files, there is a field called **geometry**. These fields represent vector geometry and are used to represent the spatial components of geographic features with discrete boundaries.
#### DECLARATION: Any field already described in a current section is ignored in the subsequent sections to avoid field description redundancy.

The Land Sector Dataset is divided into five main categories; which are:

1. [Administrative](https://datasets.mojaglobal.workers.dev/0:/Administrative/)
2. [Biodiveersity, AgroClimatic and Ecological Zones](https://datasets.mojaglobal.workers.dev/0:/Bioclimatic&EcologicalZones/)
3. [Climate](https://datasets.mojaglobal.workers.dev/0:/Climate/)
4. [Land Cover](https://datasets.mojaglobal.workers.dev/0:/LandCover/)
5. [Soil](https://datasets.mojaglobal.workers.dev/0:/Soil/)



# 1. ADMINISRTATIVE
The administrative directory has three subdirectories as explained below.


### 1.1   Bounderies

> In this directory, there are files containing Political boundaries which are the dividing lines between countries, states, provinces, counties, and cities. These lines, more often called borders, are created by people to separate areas governed by different groups. Sometimes, political boundaries follow  boundaries, but most of the time you can't see them.



> The bounderies are in two levels. 

##### 1.1.1 The directories with Level 2 contain bounderies at the country level including the Global Ecological Zone bounderies for each country as well as the World Soil Resourcess' boundaries; 
>* The general notation of files is : **COUNTRY_AL4_country.json**( implying the country code followed by Administrative Level 2, followed by the country name).
The files are made up of twelve (12) important fields: as explained below:
>1. **country:** refers to the name of the country
>2. **ISO3166_2:** (ISO standard codes of administrative divisions and subdivisions) In other words - Administrative Divisions of Countries
>3. **name:** name of the level 2 country
>4. **enname:** English name of country
>5. **locname:** Local name of country
>6. **offname:** official name
>7. **boundary:** type of boundary
>8. **wikidata:** wikidata code
>9. **wikimedia:** wikimedia name
>10. **timestamp** the time the data was colledcted
>11. **adnminlevel:** administrative level 2
>12. **geometry**

*  The notation of files with the general form: **COUNTRY_AL4_country_GEZ.json**(implying country code followed by administrative level 2, followed by country name; with GEZ: Global Economic Zone). The files have 08 fields. Some of which are:
> 1. **gez_name:** Global Economic Zone name
> 2. **gez_code:** Global Economic Zone standard code
> 3. **gez_abbrev:** Global Economic Zone standard abbreviation



*   The notation of files with the general form: **COUNTRY_AL4_country_WSR.json**(implying country code followed by administrative level 2, followed by country name; with WSR: World Soil Resources). The files have 08 fields
>1. **country:** refers to the name of the country
>2. **ISO3166_2:** (ISO standard codes of administrative divisions and subdivisions) In other words - Administrative Divisions of Countries
>3. **name:** name of the level 4 state
>4. **SNAME:** soil name standard code
>5. **mg_code:** the soil major group code
>6. **IPCC:** soil names(The Intergovernmental Panel on Climate Change)
>7. **adnminlevel:** administrative level
>8. **geometry**



#####  1.1.2 The directories with Level 4 contain boundaries of each state level grouped by country as well as the Ecological Zone boundaries and the World Soil Resources boundary for eeach state. At Level 4:
*   The general notation of files is : **COUNTRY_AL4_STATE-NAME.json**( implying the country name followed by Administrative Level 4, follwed by the statename).
The files are made up of eight (08) fields(	**country,	ISO3166_2,	name,	SNAME,	mg_code,	IPCC,	adminlevel,	geometry**)


*  The notation of files with the general form: **COUNTRY_AL4_STATE-NAME_GEZ.json**(implying country name followed by administrative level 4, followed by state name; with GEZ: Global Economic Zone). The files have 08 fields(**country,	ISO3166_2,	name,	gez_name,	gez_code,	gez_abbrev,	adminlevel	geometry**)



*   The notation of files with the general form: **COUNTRY_AL4_STATE-NAME_WSR.json**(implying country name followed by administrative level 4, followed by state name; with WSR: World Soil Resources). The files have 08 fields(	**country,	ISO3166_2,	name,	SNAME,	mg_code,	IPCC,	adminlevel,	geometry**)




*   THe general notation of files is : **COUNTRY_AL4_STATE-NAME.json**( implying the country name followed by Administrative Level 4, follwed by the statename).
The files are made up of eight (08) important fields: as explained below:
> 1. **country:** refers to the name of the country
> 2. **ISO3166_2:** (ISO standard codes of administrative divisions and subdivisions) In other words - Administrative Divisions of Countries
> 3. **name:** name of the level 4 state
> 4. **SNAME:** soil name standard code
> 5. **mg_code:** the soil major group code
> 6. **IPCC:** soil names(The Intergovernmental Panel on Climate Change)
> 7. **adnminlevel:** administrative level
> 8. **geometry**





*  The notation of files with the general form: **COUNTRY_AL4_STATE-NAME_GEZ.json**(implying country name followed by administrative level 4, followed by state name; with GEZ: Global Economic Zone). The files have 08 fields. Some of which are:
> 1. **gez_name:** Global Economic Zone name
> 2. **gez_code:** Global Economic Zone standard code
> 3. **gez_abbrev:** Global Economic Zone standard abbreviation



*   The notation of files with the general form: **COUNTRY_AL4_STATE-NAME_WSR.json**(implying country name followed by administrative level 4, followed by state name; with WSR: World Soil Resources). The files have 08 fields(	**country,	ISO3166_2,	name,	SNAME,	mg_code,	IPCC,	adminlevel,	geometry**)




> We also have two files that contain the world's country boundaries and the world's states boundaries respectively.




### 1.2.   Protected Areas
>This directory contains the boundary dataset for **World Database of Protected Areas WDPA** ezpecially data on Other Effective Area-Based Conservation Measures (WDOECM). A detailed description of the files within can be found[ here](http://wdpa.s3.amazonaws.com/WDPA_Manual/English/WDPA_Manual_1_4_EN_FINAL.pdf).

### 1.3   Roads
>This directory combines the best available roads data by country into a global roads coverage, using the UN Spatial Data Infrastructure Transport (UNSDI-T) version 2 as a common data model. All country road networks have been joined topologically at the borders, and many countries have been edited for internal topology. Source data for each country are provided in the [documentation](https://sedac.ciesin.columbia.edu/downloads/docs/groads/groads-v1-documentation.pdf).



# 2. Biodiveersity, AgroClimatic and Ecological Zones

This directory is made up of two sub-directories and five files. The five files are:

##### 2.1.1  CI_BiodiversityHotspots.geojson: This file contains global conservation international Biodiversity Hotspots. It is made up of 06 fields:

>> **1. OBJECTID**: the object identifier

>> **2. NAME**: Standard name of Hotzone

>> **3. Type**:  type of hot zone eith outer limit or hotspot area

>> **4. shape_Length**: reoresents the length of the polygon

>> **5. Shape_Area** represents the area of the polygon

>> **6. geometry**

##### 2.1.2  GlobalCriticalHabitatScreening.tif: This screening layer shows the global spatial distribution of likely or potential Critical Habitat, as defined by the International Finance Corporation’s Performance Standard 6 (IFC PS6) criteria.

##### 2.1.3 HoldridgeLifeZones.json: The Holdridge life zones system is a global bioclimatic scheme for the classification of land areas. This file contains:

>>**1. FID**: 

>>**2. AREA**: 

>> **3. PERIMETER**: 

>> **4. HOLDRIG_**: 

>> **5. HOLDRIG_ID**: 

>> **6. ZONE**: 

>> **7. CASE_**: 

>> **8. FREQUENCY**: 

>> **9. SYMBOL**: 	

>> **10. geometry**: 


##### 2.1.4 TerrestrialEcoregionsoftheWorld_WWF.geojson: This file conatains Terrestrial Ecological Regions of the world and has the following fields:

	OBJECTID_1	OBJECTID	AREA	ECO_NAME	REALM	BIOME	ECO_NUM	ECO_ID	ECO_SYM	GBL_STAT	G200_REGIO	G200_NUM	G200_BIOME	G200_STAT	area_km2	eco_code	BIOME_1	GBL_STAT_1	REALM_1	Shape_Length	Shape_Area	geometry


##### 2.1.5 WorldDrylandDataset_2007_UNCCD_CBD_2014.json: empty file


There are two subdirectories:

 ### 2.2 Global AgroEcological Zones: 

This directory contains 12 geotiff files with various Land Resources(cultivated, domestic land cover, forest land), Protected areas(restricted agro areas, types), Soil resources(dominant soils, nutrient availability, rain fed terrain suitaiblity, rooting conditions), Terrain slope index and Water scarcity. files
and 3 subdirectories. The 03 subdirectories:
##### 2.2.1 Agro Climate: it contains geotiff files for growing period length, temperature growing period, thermal climate and thermal zones.

##### 2.2.2 Fisher 2008 GAEZ: contains geotiff files about Barren sparsely vegetated land, build up land, irrigated cultivated land, rainfed cultivated land, total cultivated land, forest land, grass shrub woodland and water bodies. The asc directory contains ASCII Raster files(.asc) variants of some of of the geotiff files.

##### 2.2.3 originals: This directory contails the zipped(compressed) files versions of the geotiff and/or .asc files.

### 2.3 Global Ecological Zones:  

This directory contains one file for the global ecological zone as well as 02 subdirectories that contain the json files of ECological zones grouped by country and state respectiviely. The attributes of the files in this section are the smae as those of the GEZ files of section 1.1.1.


# 3. Climate

The Climate directory contains the Koppen Geiger climate shift from 1901 to 2100. The files within this subdirectory have the follwing attributes:

	OBJECTID	ID	GRIDCODE	Shape_Length	Shape_Area	geometry

  some files within the subdirectory have the suffixes: 
  >A1FI (fossil fuel intensive),

  >A1 ( new and efficient technologies), 

  >A2 (a very heterogenic world with focus on family values and local traditions),

  >B1 (a world without materialism and launch of
clean technologies), 

  >B2 (a world with focus on local solutions for economic and ecological sustainability),  


Within the climate directory the files:

>  **IPCC_ClimateZoneMap.tif:** Contains the geotiff IPCC climate zone map.

>  **IPCC_ClimateZoneMap_Vector.geojson:** contains the vectorised format fo the geotiff IPCC climate zone map. This file has the properties: 
	CLASS_NAME	geometry

>  **KoppenGeigerClimateShifts.zip**: This file contains the zips of the Koppen Geiger Climate shifts.


# 4. Land Cover


> The Land ccover directory has four principal subdirectories:


### 4.1 Biomass Carbon: The Biomas Carbon is further subdivided into:

#####4.1.1 Above Ground Live Biomass: 
This directory conains a zip file( AboveGroundLiveBiomassTiles.zip) with dataset on all living biomass above the soil including stem, stump, branches, bark, seeds and foliage.

##### 4.1.2 Avitabile Pan Tropical Biomass:
This directory contains Avitabile's Above ground biomass geotiff and zip files

##### 4.1.3 Geo Carbon Global Forest Biomass Maps: 
Contains geo carbon geotiff and zip file maps(global forest biomass, above ground biomass, and forest above ground biomass)

##### 4.1.4 Global Biomass
This directory has 03 global biomass subdirectories containing tiles for above ground biomass, growing stock volums and originals. The file names in these sub directories directly imply the tiles of interest.


### 4.2 Forest
This directory contains subdirectories:

##### 4.2.1 Managed Forest Concessions: 
Within this directory there are files containing managed forest concessions of 10 countries including the global geojson file for managed forest concessions. These files have the following properties.
  **id,	OBJECTID,	country,	name,	company,	group_comp,	group_coun,	legal_term,	status,	province,	source,	last_updat,	Shape_Leng,	AREA_GEO,	Shape_Length,	Shape_Area, and	geometry**

 ##### 4.2.2 Pan Tropical Forest Strata
  Contains geotiff files of Pan tropical forest strata for Africa(AFR), South America(SAM) and Southeast Asia(SEA) as well as their relative zip files.

 ##### 4.2.3 Planted forests
  This data is from The Spatial Database of Planted Trees(SDPT). It contains data on 43 countries. Each file has the follwing properties:
  	**final_id,	iso,	country,	org_name,	common_name,	species,	species_simp,	plant_ag,	timber_ag,	ever_dec,	conifer_broad,	hard_soft,	size,	source,	year,	geometry**

 ##### 4.2.4 Wood Fiber Concessions
Contains files on the wood fiber concessions of 03 countries and 01 file for the world. The files have the following properties: 
**OBJECTID_1.	OBJECTID.	group_comp.	NAME,	type,	COUNTRY,	area_ha,	source,	Last_updat,	gfwid,	Shape_Leng,	source_typ,	year,	FID_,	source_t_1,	Shape_Le_1,,	Shape_Le_2,	Shape_Length,	Shape_Area,	geometry.**


### 4.3 Forest Loss
Forest Loss contains 03  subdirectories:
##### 4.3.1 Hansen Global Forest Change
This directory contains 04 principal subdirectories(d**atamask, gain, lossy year and tree cover**). In these directories are geotiff tiles with the names implying the interest

##### 4.3.2 Intact Forest Landscapes
This directory contains zips and geojson files for Intact forst lanscapes. The notation of the files carry the year of recording.

##### 4.3.3 Terra i Forest Loss
It contains the terra i forest loss data for the country Uganda.

### 4.4 Land Use
This directory contains Global Food Security-Support Analysis Data. The subdirectories contain tiled files with GFSAD Global Crop Land Crop Extent data. These files notations contain the year as well as the regions of interest which are: Africa( GFSAD30AFCE_2015_resampledTiles), Australia-New_Zealand-China-Mongolia( GFSAD30AUNZCNMOCE_2015_resampledTiles), Europe-Centra_Asia-Russia-Middle_East( GFSAD30EUCEARUMECE_2015_resampledTiles), North America( GFSAD30NACE_2010_resampledTiles), South America( GFSAD30SACE_2015_resampledTiles) and Southeast-and-Northeast Asia( GFSAD30SEACE_2015_resampledTiles).



# 5. Soil
This directory contains 03 subdirectories and 02 files( Global soil organic carbon). The three subdirectories are:

### 5.1 Harmonised World Soil Database(HWSD)
This directory contains data tables with the follwing properties:

ID	MU_GLOBAL	MU_SOURCE1	MU_SOURCE2	ISSOIL	SHARE	SEQ	SU_SYM74	SU_CODE74	SU_SYM85	SU_CODE85	SU_SYM90	SU_CODE90	T_TEXTURE	DRAINAGE	REF_DEPTH	AWC_CLASS	PHASE1	PHASE2	ROOTS	IL	SWR	ADD_PROP	T_GRAVEL	T_SAND	T_SILT	T_CLAY	T_USDA_TEX_CLASS	T_REF_BULK_DENSITY	T_BULK_DENSITY	T_OC	T_PH_H2O	T_CEC_CLAY	T_CEC_SOIL	T_BS	T_TEB	T_CACO3	T_CASO4	T_ESP	T_ECE	S_GRAVEL	S_SAND	S_SILT	S_CLAY	S_USDA_TEX_CLASS	S_REF_BULK_DENSITY	S_BULK_DENSITY	S_OC	S_PH_H2O	S_CEC_CLAY	S_CEC_SOIL	S_BS	S_TEB	S_CACO3	S_CASO4	S_ESP	S_ECE


### 5.2 Soil Quality Crop Production
Contains a zip file the HWSD Soil Quality Crop Production.

### 5.3 World Soil Resources(WSR)
This directory contains 02 subdirectories: 
 ##### 5.3.1 WSR by Country
Contains files whose notation indicate the country of interest. The properties are the same as in 1.1.1.

 ##### 5.3.2 WSR by State
Contains files of states' soil resources. The properties are the same as in 1.1.1.


