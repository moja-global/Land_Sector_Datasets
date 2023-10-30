# MAPPING PROTOTYPE FOR SUSTAINABLE DEVELOPMENT GROWTH(SDG)



This is the prototype for mapping the Sustainable Development Goals (SDG) in the administrative dataset.


The Sustainable Development Goal in alignment with the administrative dataset category that was chosen gare No 11 and No 13


#### SDG Goal 11:


Sustainable Cities and Communities- the goal of this SDG is to make cities and human settlements inclusive, safe, resilient and sustainable.


#### SDG Goal 13:
Climate Action - the goal of this SDG is to take urgent action to combat climate and its impacts.




## ADMINISTRATIVE DATASET


The administrative dataset is a geospatial data which contains the global road data, protected area data, and boundary datasets.


### GLOBAL ROAD DATA


#### Dataset Attribute:
The Global Road dataset has the following features: Geometry, Object Id, Onme, Fclass, Srftpe, Isseasonal, Cuntprac, Gdwthrprac, Sum_Length_Km. The 'FClass' feature ranges from 0, 1, 2,3 ,4,5 and 6 and it contains types of the road such as unspecified-highway, Primary, Secondary, Tertiary, Local/Urban and Trail respectively.


#### Mapping Explanation:
The attributes within the 'FClass' column was mapped with SDG 11 based on the substantial impact of these attributes on the achievement of the Sustainable Development Goal. SDG 11, which focuses on 'Sustainable Cities and Communities,'


SDG 11 aims to make cities and human settlements inclusive, safe, resilient, and sustainable. Transportation infrastructure is crucial for development, and it directly ties to the goal of creating sustainable and accessible cities. The different types of roads can play a significant role in achieving this goal.


### CLIMATE DATA


#### Dataset Attribute:


The Climate dataset has the following columns: Geometry and class_names.


#### Mapping Explanation:


The values in the class_names of the climate dataset represent the different climate zones: Temperate Moist, Warm Temperate Dry, Cool Temperate Moist, Cool Temperate Dry, Polar Moist, Polar Dry, Boreal Moist, Boreal Dry and Tropical Montane and are mapped to SDG 13- Climate Action. All of the values in the class_name attributes were mapped because of their relevance to the SDG.


The SDG No 13 aims at making efforts to reduce greenhouse gas emissions, enhance climate resilience, and promote climate education and awareness. The connection to SDG 13 signifies the relevance of climate data in the pursuit of sustainable and responsible actions to mitigate climate change and promote environmental resilience.


### PROTECTED AREA DATASET


#### Data Attributes:


The protected area dataset columns includes: WDPAID, WDPA_PID, PA_DEF, NAME, ORIG_NAME, DESIG, DESIG_ENG, DESIG_TYPE, IUCN_CAT, INT_CRIT, MARINE,REP_M_AREA, GIS_M_AREA, REP_AREA, GIS_AREA, NO_TAKE,NO_TK_AREA, STATUS, STATUS_YR, GOV_TYPE, OWN_TYPE,MANG_AUTH, MANG_PLAN, VERIF, METADATAID, SUB_LOC,PARENT_ISO, ISO3, SUPP_INFO, CONS_OBJ, geometry.


**STATUS**: This is the attribute mapped to the SDG. It describes the status of protected areas or specific sites of cultural or natural significance.
   


#### Mapping Explanation:


The 'STATUS' attribute in the protected area dataset provides information about the status of various protected areas or sites of cultural or natural significance. Mapping this attribute to SDG 11, focuses on Sustainable Cities and Communities.


The Designated, Established and the Inscribed status indicates that the area has been officially designated for protection. This SDG 11 aligns with the goal of ensuring sustainable urbanisation and safe, inclusive, resilient cities and communities. 


#### Reference 


[Sustainable Development Goal](https://www.fao.org/3/CA3121EN/ca3121en.pdf)




```python


```



